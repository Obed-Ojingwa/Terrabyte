# C:\Users\Melody\Documents\workinprog\terrabyte\backend\app\models\course.py
from __future__ import annotations
import enum
from datetime import datetime, date
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import String, Boolean, DateTime, Date, Text, ForeignKey, Integer, Numeric, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.enrollment import Enrollment
    from app.models.assignment import Assignment
    from app.models.exam import Exam


class CourseMode(str, enum.Enum):
    online = "online"
    physical = "physical"
    private = "private"


class CourseTier(str, enum.Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    professional = "professional"
    beginner_to_professional = "beginner_to_professional"


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False, default=0)
    mode: Mapped[CourseMode] = mapped_column(SAEnum(CourseMode), nullable=False, default=CourseMode.online)
    category: Mapped[Optional[str]] = mapped_column(String(100))
    tier: Mapped[CourseTier] = mapped_column(SAEnum(CourseTier), nullable=False, default=CourseTier.beginner)
    duration_days: Mapped[Optional[int]] = mapped_column(Integer)
    duration_weeks: Mapped[Optional[int]] = mapped_column(Integer)
    start_date: Mapped[Optional[date]] = mapped_column(Date)
    end_date: Mapped[Optional[date]] = mapped_column(Date)
    schedule_notes: Mapped[Optional[str]] = mapped_column(Text)
    what_you_learn: Mapped[Optional[str]] = mapped_column(Text)
    requirements: Mapped[Optional[str]] = mapped_column(Text)
    target_audience: Mapped[Optional[str]] = mapped_column(Text)
    thumbnail_url: Mapped[Optional[str]] = mapped_column(Text)
    is_published: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    tutor_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    tutor: Mapped[Optional["User"]] = relationship("User", back_populates="courses_tutoring")
    modules: Mapped[List["Module"]] = relationship("Module", back_populates="course", cascade="all, delete-orphan", order_by="Module.order")
    enrollments: Mapped[List["Enrollment"]] = relationship("Enrollment", back_populates="course")
    assignments: Mapped[List["Assignment"]] = relationship("Assignment", back_populates="course")
    exams: Mapped[List["Exam"]] = relationship("Exam", back_populates="course")


class Module(Base):
    __tablename__ = "modules"

    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    course: Mapped["Course"] = relationship("Course", back_populates="modules")
    lessons: Mapped[List["Lesson"]] = relationship("Lesson", back_populates="module", cascade="all, delete-orphan", order_by="Lesson.order")


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(primary_key=True)
    module_id: Mapped[int] = mapped_column(ForeignKey("modules.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    video_s3_key: Mapped[Optional[str]] = mapped_column(Text)
    duration_seconds: Mapped[Optional[int]] = mapped_column(Integer)
    order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_preview: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    module: Mapped["Module"] = relationship("Module", back_populates="lessons")
    materials: Mapped[List["Material"]] = relationship("Material", back_populates="lesson", cascade="all, delete-orphan")
    progress_records: Mapped[List["LessonProgress"]] = relationship("LessonProgress", back_populates="lesson")


class Material(Base):
    __tablename__ = "materials"

    id: Mapped[int] = mapped_column(primary_key=True)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    file_s3_key: Mapped[str] = mapped_column(Text, nullable=False)
    file_type: Mapped[Optional[str]] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    lesson: Mapped["Lesson"] = relationship("Lesson", back_populates="materials")

# import uuid
# from sqlalchemy import String, Boolean, ForeignKey, Numeric, Integer, Text, DateTime
# from sqlalchemy.orm import mapped_column, Mapped, relationship
# from sqlalchemy.dialects.postgresql import UUID
# from datetime import datetime
# from app.database import Base


# class Course(Base):
#     __tablename__ = "courses"
#     id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     title: Mapped[str] = mapped_column(String(255))
#     slug: Mapped[str] = mapped_column(String(255), unique=True, index=True)
#     description: Mapped[str | None] = mapped_column(Text, nullable=True)
#     thumbnail_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
#     price: Mapped[float] = mapped_column(Numeric(10, 2), default=0)
#     mode: Mapped[str] = mapped_column(String(50))
#     category: Mapped[str | None] = mapped_column(String(100), nullable=True)
#     level: Mapped[str | None] = mapped_column(String(50), nullable=True)
#     duration_weeks: Mapped[int | None] = mapped_column(Integer, nullable=True)
#     is_published: Mapped[bool] = mapped_column(Boolean, default=False)
#     tutor_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
#     created_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
#     created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#     updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
#     tutor: Mapped["User"] = relationship(foreign_keys=[tutor_id])
#     modules: Mapped[list["Module"]] = relationship(back_populates="course", cascade="all, delete-orphan", order_by="Module.position")


# class Module(Base):
#     __tablename__ = "modules"
#     id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     course_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"))
#     title: Mapped[str] = mapped_column(String(255))
#     position: Mapped[int] = mapped_column(Integer, default=0)
#     created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#     course: Mapped["Course"] = relationship(back_populates="modules")
#     lessons: Mapped[list["Lesson"]] = relationship(back_populates="module", cascade="all, delete-orphan", order_by="Lesson.position")


# class Lesson(Base):
#     __tablename__ = "lessons"
#     id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     module_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("modules.id", ondelete="CASCADE"))
#     title: Mapped[str] = mapped_column(String(255))
#     content: Mapped[str | None] = mapped_column(Text, nullable=True)
#     position: Mapped[int] = mapped_column(Integer, default=0)
#     duration_min: Mapped[int | None] = mapped_column(Integer, nullable=True)
#     is_preview: Mapped[bool] = mapped_column(Boolean, default=False)
#     created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#     module: Mapped["Module"] = relationship(back_populates="lessons")
#     materials: Mapped[list["Material"]] = relationship(back_populates="lesson", cascade="all, delete-orphan")


# class Material(Base):
#     __tablename__ = "materials"
#     id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     lesson_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("lessons.id", ondelete="CASCADE"))
#     title: Mapped[str] = mapped_column(String(255))
#     type: Mapped[str] = mapped_column(String(50))
#     s3_key: Mapped[str] = mapped_column(String(500))
#     is_downloadable: Mapped[bool] = mapped_column(Boolean, default=False)
#     size_bytes: Mapped[int | None] = mapped_column(Integer, nullable=True)
#     created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#     lesson: Mapped["Lesson"] = relationship(back_populates="materials")
