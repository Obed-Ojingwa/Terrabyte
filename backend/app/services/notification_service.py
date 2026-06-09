# C:\Users\Melody\Documents\workinprog\terrabyte\backend\app\services\notification_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.notification import Notification


async def create_notification(db: AsyncSession, user_id: int, title: str, message: str, type: str = "info", link: str = None) -> Notification:
    notif = Notification(user_id=user_id, title=title, message=message, type=type, link=link)
    db.add(notif)
    await db.flush()
    return notif


async def get_user_notifications(db: AsyncSession, user_id: int, unread_only: bool = False):
    q = select(Notification).where(Notification.user_id == user_id)
    if unread_only:
        q = q.where(Notification.is_read == False)
    q = q.order_by(Notification.created_at.desc()).limit(50)
    result = await db.execute(q)
    return result.scalars().all()


async def mark_read(db: AsyncSession, notification_id: int, user_id: int) -> bool:
    result = await db.execute(
        select(Notification).where(Notification.id == notification_id, Notification.user_id == user_id)
    )
    notif = result.scalar_one_or_none()
    if notif:
        notif.is_read = True
        await db.flush()
        return True
    return False