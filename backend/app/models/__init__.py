# C:\Users\Melody\Documents\workinprog\terrabyte\backend\app\models\__init__.py
# CRITICAL: import order must be maintained to avoid NoReferencedTableError
from app.models.user import Role, User
from app.models.course import Course, Module, Lesson, Material, CourseMode, CourseTier
from app.models.assignment import Assignment, Submission, SubmissionStatus
from app.models.exam import Exam, ExamQuestion, ExamResult
from app.models.enrollment import Enrollment, LessonProgress, EnrollmentStatus
from app.models.payment import Payment, PaymentStatus
from app.models.certificate import Certificate, CertificateStatus
from app.models.notification import Notification
from app.models.blog import BlogPost
from app.models.event import Event

__all__ = [
    "Role", "User",
    "Course", "Module", "Lesson", "Material", "CourseMode", "CourseTier",
    "Assignment", "Submission", "SubmissionStatus",
    "Exam", "ExamQuestion", "ExamResult",
    "Enrollment", "LessonProgress", "EnrollmentStatus",
    "Payment", "PaymentStatus",
    "Certificate", "CertificateStatus",
    "Notification",
    "BlogPost",
    "Event",
]