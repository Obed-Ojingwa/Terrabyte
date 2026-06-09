# C:\Users\Melody\Documents\workinprog\terrabyte\backend\app\models\enrollment.py
from __future__ import annotations
import enum
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, Boolean, DateTime, ForeignKey, Integer, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.course import Course, Lesson


class EnrollmentStatus(str, enum.Enum):
    active = "active"
    completed = "completed"
    cancelled = "cancelled"
    pending = "pending"


class Enrollment(Base):
    __tablename__ = "enrollments"

    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False)
    status: Mapped[EnrollmentStatus] = mapped_column(SAEnum(EnrollmentStatus), default=EnrollmentStatus.active, nullable=False)
    enrolled_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    progress_pct: Mapped[float] = mapped_column(default=0.0, nullable=False)

    student: Mapped["User"] = relationship("User", back_populates="enrollments")
    course: Mapped["Course"] = relationship("Course", back_populates="enrollments")
    lesson_progress: Mapped[list["LessonProgress"]] = relationship("LessonProgress", back_populates="enrollment", cascade="all, delete-orphan")


class LessonProgress(Base):
    __tablename__ = "lesson_progress"

    id: Mapped[int] = mapped_column(primary_key=True)
    enrollment_id: Mapped[int] = mapped_column(ForeignKey("enrollments.id"), nullable=False)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"), nullable=False)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    watch_seconds: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime)

    enrollment: Mapped["Enrollment"] = relationship("Enrollment", back_populates="lesson_progress")
    lesson: Mapped["Lesson"] = relationship("Lesson", back_populates="progress_records")

# import uuid
# from sqlalchemy import String, Boolean, ForeignKey, Integer, DateTime
# from sqlalchemy.orm import mapped_column, Mapped, relationship
# from sqlalchemy.dialects.postgresql import UUID
# from datetime import datetime
# from app.database import Base


# class Enrollment(Base):
#     __tablename__ = "enrollments"
#     id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     student_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
#     course_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"))
#     mode: Mapped[str] = mapped_column(String(50))
#     status: Mapped[str] = mapped_column(String(50), default="pending")
#     enrolled_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#     completed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
#     student: Mapped["User"] = relationship(foreign_keys=[student_id])
#     course: Mapped["Course"] = relationship(foreign_keys=[course_id])


# class LessonProgress(Base):
#     __tablename__ = "lesson_progress"
#     id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     student_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
#     lesson_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("lessons.id", ondelete="CASCADE"))
#     is_completed: Mapped[bool] = mapped_column(Boolean, default=False)
#     watch_time_sec: Mapped[int] = mapped_column(Integer, default=0)
#     updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
