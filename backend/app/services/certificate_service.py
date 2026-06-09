# C:\Users\Melody\Documents\workinprog\terrabyte\backend\app\services\certificate_service.py
import io
import uuid
import boto3
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException

from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

from app.config import settings
from app.models.certificate import Certificate, CertificateStatus
from app.models.enrollment import Enrollment, EnrollmentStatus
from app.models.course import Course
from app.models.user import User


def _generate_certificate_pdf(student_name: str, course_title: str, cert_number: str, issued_date: str) -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=landscape(A4),
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )

    styles = getSampleStyleSheet()
    blue = colors.HexColor("#2563eb")

    title_style = ParagraphStyle(
        "CertTitle",
        fontSize=36,
        fontName="Helvetica-Bold",
        textColor=blue,
        alignment=TA_CENTER,
        spaceAfter=10,
    )
    subtitle_style = ParagraphStyle(
        "CertSubtitle",
        fontSize=14,
        fontName="Helvetica",
        textColor=colors.gray,
        alignment=TA_CENTER,
        spaceAfter=20,
    )
    name_style = ParagraphStyle(
        "StudentName",
        fontSize=28,
        fontName="Helvetica-Bold",
        textColor=colors.black,
        alignment=TA_CENTER,
        spaceAfter=10,
    )
    body_style = ParagraphStyle(
        "Body",
        fontSize=13,
        fontName="Helvetica",
        textColor=colors.black,
        alignment=TA_CENTER,
        spaceAfter=6,
    )
    course_style = ParagraphStyle(
        "CourseName",
        fontSize=18,
        fontName="Helvetica-Bold",
        textColor=blue,
        alignment=TA_CENTER,
        spaceAfter=20,
    )
    footer_style = ParagraphStyle(
        "Footer",
        fontSize=9,
        fontName="Helvetica",
        textColor=colors.gray,
        alignment=TA_CENTER,
    )

    story = [
        Spacer(1, 0.3 * inch),
        Paragraph("TERRABYTE ACADEMY", title_style),
        Paragraph("Certificate of Completion", subtitle_style),
        HRFlowable(width="90%", thickness=2, color=blue),
        Spacer(1, 0.3 * inch),
        Paragraph("This is to certify that", body_style),
        Spacer(1, 0.1 * inch),
        Paragraph(student_name, name_style),
        HRFlowable(width="50%", thickness=1, color=colors.lightgrey),
        Spacer(1, 0.2 * inch),
        Paragraph("has successfully completed the course", body_style),
        Spacer(1, 0.1 * inch),
        Paragraph(course_title, course_style),
        Spacer(1, 0.3 * inch),
        HRFlowable(width="90%", thickness=2, color=blue),
        Spacer(1, 0.2 * inch),
        Paragraph(f"Date of Issue: {issued_date}", body_style),
        Spacer(1, 0.1 * inch),
        Paragraph(f"Certificate No: {cert_number}", footer_style),
        Paragraph("Nigeria's Premier Tech Learning Platform | terrabyteacademy.com", footer_style),
    ]

    doc.build(story)
    return buffer.getvalue()


async def request_certificate(db: AsyncSession, student: User, course_id: int) -> Certificate:
    # Verify student is enrolled and has completed the course
    enroll_result = await db.execute(
        select(Enrollment).where(
            Enrollment.student_id == student.id,
            Enrollment.course_id == course_id,
            Enrollment.status == EnrollmentStatus.completed,
        )
    )
    enrollment = enroll_result.scalar_one_or_none()
    if not enrollment:
        raise HTTPException(status_code=400, detail="Course not completed")

    # Check if certificate already exists
    existing = await db.execute(
        select(Certificate).where(
            Certificate.student_id == student.id,
            Certificate.course_id == course_id,
        )
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Certificate already requested")

    cert_number = f"TB-CERT-{uuid.uuid4().hex[:8].upper()}"
    cert = Certificate(
        student_id=student.id,
        course_id=course_id,
        certificate_number=cert_number,
        status=CertificateStatus.pending,
    )
    db.add(cert)
    await db.flush()
    return cert


async def issue_certificate(db: AsyncSession, certificate_id: int, admin_id: int) -> Certificate:
    result = await db.execute(select(Certificate).where(Certificate.id == certificate_id))
    cert = result.scalar_one_or_none()
    if not cert:
        raise HTTPException(status_code=404, detail="Certificate not found")

    # Load student and course
    student_result = await db.execute(select(User).where(User.id == cert.student_id))
    student = student_result.scalar_one()
    course_result = await db.execute(select(Course).where(Course.id == cert.course_id))
    course = course_result.scalar_one()

    issued_date = datetime.utcnow().strftime("%B %d, %Y")
    pdf_bytes = _generate_certificate_pdf(
        student_name=student.full_name,
        course_title=course.title,
        cert_number=cert.certificate_number,
        issued_date=issued_date,
    )

    # Upload to S3
    s3 = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION,
    )
    s3_key = f"certificates/{cert.certificate_number}.pdf"
    s3.put_object(
        Bucket=settings.S3_BUCKET_NAME,
        Key=s3_key,
        Body=pdf_bytes,
        ContentType="application/pdf",
    )

    cert.status = CertificateStatus.issued
    cert.pdf_s3_key = s3_key
    cert.issued_at = datetime.utcnow()
    cert.approved_by_id = admin_id
    await db.flush()
    return cert


async def get_certificate_download_url(db: AsyncSession, certificate_id: int, student_id: int) -> str:
    result = await db.execute(
        select(Certificate).where(
            Certificate.id == certificate_id,
            Certificate.student_id == student_id,
            Certificate.status == CertificateStatus.issued,
        )
    )
    cert = result.scalar_one_or_none()
    if not cert or not cert.pdf_s3_key:
        raise HTTPException(status_code=404, detail="Certificate not available")

    s3 = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION,
    )
    url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": settings.S3_BUCKET_NAME, "Key": cert.pdf_s3_key},
        ExpiresIn=900,
    )
    return url