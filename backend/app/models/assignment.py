# C:\Users\Melody\Documents\workinprog\terrabyte\backend\app\models\assignment.py
from __future__ import annotations
import enum
from datetime import datetime
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import String, DateTime, Text, ForeignKey, Integer, Numeric, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from app.models.course import Course
    from app.models.user import User


class SubmissionStatus(str, enum.Enum):
    submitted = "submitted"
    graded = "graded"
    resubmit = "resubmit"


class Assignment(Base):
    __tablename__ = "assignments"

    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    due_date: Mapped[Optional[datetime]] = mapped_column(DateTime)
    max_score: Mapped[float] = mapped_column(Numeric(5, 2), default=100.0, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    course: Mapped["Course"] = relationship("Course", back_populates="assignments")
    submissions: Mapped[List["Submission"]] = relationship("Submission", back_populates="assignment", cascade="all, delete-orphan")


class Submission(Base):
    __tablename__ = "submissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    assignment_id: Mapped[int] = mapped_column(ForeignKey("assignments.id"), nullable=False)
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    content: Mapped[Optional[str]] = mapped_column(Text)
    file_s3_key: Mapped[Optional[str]] = mapped_column(Text)
    status: Mapped[SubmissionStatus] = mapped_column(SAEnum(SubmissionStatus), default=SubmissionStatus.submitted, nullable=False)
    score: Mapped[Optional[float]] = mapped_column(Numeric(5, 2))
    feedback: Mapped[Optional[str]] = mapped_column(Text)
    submitted_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    graded_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    graded_by_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))

    assignment: Mapped["Assignment"] = relationship("Assignment", back_populates="submissions")
    student: Mapped["User"] = relationship("User", foreign_keys=[student_id])
    graded_by: Mapped[Optional["User"]] = relationship("User", foreign_keys=[graded_by_id])

# import uuid
# from sqlalchemy import String, ForeignKey, Integer, Text, DateTime, Numeric
# from sqlalchemy.orm import mapped_column, Mapped, relationship
# from sqlalchemy.dialects.postgresql import UUID
# from datetime import datetime
# from app.database import Base


# class Assignment(Base):
#     __tablename__ = "assignments"
#     id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     course_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"))
#     tutor_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
#     title: Mapped[str] = mapped_column(String(255))
#     description: Mapped[str | None] = mapped_column(Text, nullable=True)
#     due_date: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
#     max_score: Mapped[int] = mapped_column(Integer, default=100)
#     created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#     course: Mapped["Course"] = relationship(foreign_keys=[course_id])
#     submissions: Mapped[list["Submission"]] = relationship(back_populates="assignment")


# class Submission(Base):
#     __tablename__ = "submissions"
#     id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     assignment_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("assignments.id", ondelete="CASCADE"))
#     student_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
#     s3_key: Mapped[str | None] = mapped_column(String(500), nullable=True)
#     text_response: Mapped[str | None] = mapped_column(Text, nullable=True)
#     score: Mapped[float | None] = mapped_column(Numeric(5, 2), nullable=True)
#     feedback: Mapped[str | None] = mapped_column(Text, nullable=True)
#     status: Mapped[str] = mapped_column(String(50), default="submitted")
#     submitted_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#     graded_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
#     assignment: Mapped["Assignment"] = relationship(back_populates="submissions")
#     student: Mapped["User"] = relationship(foreign_keys=[student_id])
