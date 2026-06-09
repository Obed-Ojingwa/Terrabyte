# C:\Users\Melody\Documents\workinprog\terrabyte\backend\app\models\certificate.py
from __future__ import annotations
import enum
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, DateTime, Text, ForeignKey, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.course import Course


class CertificateStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    issued = "issued"


class Certificate(Base):
    __tablename__ = "certificates"

    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False)
    certificate_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    status: Mapped[CertificateStatus] = mapped_column(SAEnum(CertificateStatus), default=CertificateStatus.pending, nullable=False)
    pdf_s3_key: Mapped[Optional[str]] = mapped_column(Text)
    issued_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    requested_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    approved_by_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))

    student: Mapped["User"] = relationship("User", foreign_keys=[student_id], back_populates="certificates")
    course: Mapped["Course"] = relationship("Course")
    approved_by: Mapped[Optional["User"]] = relationship("User", foreign_keys=[approved_by_id])