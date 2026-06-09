# C:\Users\Melody\Documents\workinprog\terrabyte\backend\app\services\payment_service.py
import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
import uuid

from app.config import settings
from app.models.payment import Payment, PaymentStatus
from app.models.enrollment import Enrollment, EnrollmentStatus
from app.models.course import Course
from app.models.user import User


PAYSTACK_BASE = "https://api.paystack.co"
HEADERS = {
    "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
    "Content-Type": "application/json",
}


async def initialize_payment(db: AsyncSession, user: User, course_id: int) -> dict:
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course or not course.is_published:
        raise HTTPException(status_code=404, detail="Course not found")

    reference = f"TB-{uuid.uuid4().hex[:12].upper()}"
    amount_kobo = int(course.price * 100)

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{PAYSTACK_BASE}/transaction/initialize",
            headers=HEADERS,
            json={
                "email": user.email,
                "amount": amount_kobo,
                "reference": reference,
                "callback_url": f"{settings.FRONTEND_URL}/payment/verify?ref={reference}",
                "metadata": {
                    "user_id": user.id,
                    "course_id": course_id,
                    "course_title": course.title,
                },
            },
        )

    if resp.status_code != 200:
        raise HTTPException(status_code=502, detail="Payment initialization failed")

    data = resp.json()["data"]

    payment = Payment(
        user_id=user.id,
        course_id=course_id,
        amount=course.price,
        status=PaymentStatus.pending,
        paystack_reference=reference,
        paystack_access_code=data["access_code"],
        paystack_authorization_url=data["authorization_url"],
    )
    db.add(payment)
    await db.flush()

    return {
        "authorization_url": data["authorization_url"],
        "reference": reference,
        "access_code": data["access_code"],
    }


async def verify_payment(db: AsyncSession, reference: str) -> dict:
    result = await db.execute(select(Payment).where(Payment.paystack_reference == reference))
    payment = result.scalar_one_or_none()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"{PAYSTACK_BASE}/transaction/verify/{reference}",
            headers=HEADERS,
        )

    if resp.status_code != 200:
        raise HTTPException(status_code=502, detail="Payment verification failed")

    ps_data = resp.json()["data"]
    ps_status = ps_data["status"]

    from datetime import datetime
    if ps_status == "success":
        payment.status = PaymentStatus.success
        payment.verified_at = datetime.utcnow()

        # Activate or create enrollment
        enroll_result = await db.execute(
            select(Enrollment).where(
                Enrollment.student_id == payment.user_id,
                Enrollment.course_id == payment.course_id,
            )
        )
        enrollment = enroll_result.scalar_one_or_none()
        if enrollment:
            enrollment.status = EnrollmentStatus.active
        else:
            enrollment = Enrollment(
                student_id=payment.user_id,
                course_id=payment.course_id,
                status=EnrollmentStatus.active,
            )
            db.add(enrollment)
    else:
        payment.status = PaymentStatus.failed

    await db.flush()
    return {"status": ps_status, "payment_id": payment.id}