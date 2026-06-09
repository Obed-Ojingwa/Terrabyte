# C:\Users\Melody\Documents\workinprog\terrabyte\backend\app\models\exam.py
from __future__ import annotations
import enum
from datetime import datetime
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import String, Boolean, DateTime, Text, ForeignKey, Integer, Numeric, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from app.models.course import Course
    from app.models.user import User


class Exam(Base):
    __tablename__ = "exams"

    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    duration_minutes: Mapped[int] = mapped_column(Integer, default=60, nullable=False)
    pass_score: Mapped[float] = mapped_column(Numeric(5, 2), default=70.0, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    course: Mapped["Course"] = relationship("Course", back_populates="exams")
    questions: Mapped[List["ExamQuestion"]] = relationship("ExamQuestion", back_populates="exam", cascade="all, delete-orphan")
    results: Mapped[List["ExamResult"]] = relationship("ExamResult", back_populates="exam", cascade="all, delete-orphan")


class ExamQuestion(Base):
    __tablename__ = "exam_questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    exam_id: Mapped[int] = mapped_column(ForeignKey("exams.id"), nullable=False)
    question_text: Mapped[str] = mapped_column(Text, nullable=False)
    options: Mapped[Optional[dict]] = mapped_column(JSON)  # {"A": "...", "B": "...", "C": "...", "D": "..."}
    correct_answer: Mapped[str] = mapped_column(String(10), nullable=False)
    points: Mapped[float] = mapped_column(Numeric(5, 2), default=1.0, nullable=False)
    order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    exam: Mapped["Exam"] = relationship("Exam", back_populates="questions")


class ExamResult(Base):
    __tablename__ = "exam_results"

    id: Mapped[int] = mapped_column(primary_key=True)
    exam_id: Mapped[int] = mapped_column(ForeignKey("exams.id"), nullable=False)
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    answers: Mapped[Optional[dict]] = mapped_column(JSON)  # {"question_id": "answer"}
    score: Mapped[float] = mapped_column(Numeric(5, 2), nullable=False)
    passed: Mapped[bool] = mapped_column(Boolean, nullable=False)
    started_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    submitted_at: Mapped[Optional[datetime]] = mapped_column(DateTime)

    exam: Mapped["Exam"] = relationship("Exam", back_populates="results")
    student: Mapped["User"] = relationship("User")

# import uuid
# from sqlalchemy import String, Boolean, ForeignKey, Integer, Text, DateTime, Numeric
# from sqlalchemy.orm import mapped_column, Mapped, relationship
# from sqlalchemy.dialects.postgresql import UUID, JSONB
# from datetime import datetime
# from app.database import Base


# class Exam(Base):
#     __tablename__ = "exams"
#     id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     course_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"))
#     title: Mapped[str] = mapped_column(String(255))
#     duration_min: Mapped[int] = mapped_column(Integer, default=60)
#     pass_score: Mapped[float] = mapped_column(Numeric(5, 2), default=50.0)
#     created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#     questions: Mapped[list["ExamQuestion"]] = relationship(back_populates="exam", order_by="ExamQuestion.position")
#     results: Mapped[list["ExamResult"]] = relationship(back_populates="exam")


# class ExamQuestion(Base):
#     __tablename__ = "exam_questions"
#     id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     exam_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("exams.id", ondelete="CASCADE"))
#     question: Mapped[str] = mapped_column(Text)
#     type: Mapped[str] = mapped_column(String(50))
#     options: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
#     correct: Mapped[str | None] = mapped_column(Text, nullable=True)
#     points: Mapped[int] = mapped_column(Integer, default=1)
#     position: Mapped[int] = mapped_column(Integer, default=0)
#     exam: Mapped["Exam"] = relationship(back_populates="questions")


# class ExamResult(Base):
#     __tablename__ = "exam_results"
#     id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     exam_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("exams.id", ondelete="CASCADE"))
#     student_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
#     score: Mapped[float | None] = mapped_column(Numeric(5, 2), nullable=True)
#     answers: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
#     passed: Mapped[bool] = mapped_column(Boolean, default=False)
#     taken_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#     exam: Mapped["Exam"] = relationship(back_populates="results")
