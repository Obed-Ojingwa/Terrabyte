# C:\Users\Melody\Documents\workinprog\terrabyte\backend\app\services\course_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
import boto3
from app.config import settings
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseUpdate


async def list_courses(db: AsyncSession, published_only: bool = True, skip: int = 0, limit: int = 20):
    q = select(Course)
    if published_only:
        q = q.where(Course.is_published == True)
    q = q.offset(skip).limit(limit).order_by(Course.created_at.desc())
    result = await db.execute(q)
    return result.scalars().all()


async def get_course(db: AsyncSession, course_id: int) -> Course:
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


async def create_course(db: AsyncSession, data: CourseCreate) -> Course:
    course = Course(**data.model_dump())
    db.add(course)
    await db.flush()
    await db.refresh(course)
    return course


async def update_course(db: AsyncSession, course_id: int, data: CourseUpdate) -> Course:
    course = await get_course(db, course_id)
    for field, value in data.model_dump(exclude_none=True).items():
        setattr(course, field, value)
    await db.flush()
    return course


async def delete_course(db: AsyncSession, course_id: int) -> bool:
    course = await get_course(db, course_id)
    await db.delete(course)
    await db.flush()
    return True


async def get_lesson_video_url(s3_key: str) -> str:
    s3 = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION,
    )
    return s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": settings.S3_BUCKET_NAME, "Key": s3_key},
        ExpiresIn=900,  # 15 minutes
    )

# import re
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select, func
# from fastapi import HTTPException
# from app.models.course import Course
# from app.schemas.course import CourseCreate, CourseUpdate, CourseResponse, CourseListResponse


# def slugify(text: str) -> str:
#     text = text.lower().strip()
#     text = re.sub(r"[^\w\s-]", "", text)
#     return re.sub(r"[\s_-]+", "-", text)


# class CourseService:
#     def __init__(self, db: AsyncSession):
#         self.db = db

#     async def list_courses(self, search, category, mode, level, page, page_size) -> CourseListResponse:
#         query = select(Course).where(Course.is_published == True)
#         if search:
#             query = query.where(Course.title.ilike(f"%{search}%"))
#         if category:
#             query = query.where(Course.category == category)
#         if mode:
#             query = query.where(Course.mode == mode)
#         if level:
#             query = query.where(Course.level == level)
#         total = (await self.db.execute(select(func.count()).select_from(query.subquery()))).scalar()
#         query = query.offset((page - 1) * page_size).limit(page_size)
#         courses = (await self.db.execute(query)).scalars().all()
#         return CourseListResponse(
#             items=[CourseResponse.model_validate(c) for c in courses],
#             total=total, page=page, page_size=page_size,
#             total_pages=(total + page_size - 1) // page_size,
#         )

#     async def get_course(self, course_id: str) -> CourseResponse:
#         result = await self.db.execute(select(Course).where(Course.id == course_id))
#         course = result.scalar_one_or_none()
#         if not course:
#             raise HTTPException(status_code=404, detail="Course not found")
#         return CourseResponse.model_validate(course)

#     async def create_course(self, payload: CourseCreate, user) -> CourseResponse:
#         slug = slugify(payload.title)
#         count = (await self.db.execute(select(func.count()).where(Course.slug.like(f"{slug}%")))).scalar()
#         if count:
#             slug = f"{slug}-{count}"
#         course = Course(**payload.model_dump(exclude={"tutor_id"}), slug=slug, created_by=user.id, tutor_id=payload.tutor_id)
#         self.db.add(course)
#         await self.db.commit()
#         await self.db.refresh(course)
#         return CourseResponse.model_validate(course)

#     async def update_course(self, course_id: str, payload: CourseUpdate, user) -> CourseResponse:
#         result = await self.db.execute(select(Course).where(Course.id == course_id))
#         course = result.scalar_one_or_none()
#         if not course:
#             raise HTTPException(status_code=404, detail="Course not found")
#         for field, value in payload.model_dump(exclude_unset=True).items():
#             setattr(course, field, value)
#         await self.db.commit()
#         await self.db.refresh(course)
#         return CourseResponse.model_validate(course)

#     async def delete_course(self, course_id: str, user):
#         result = await self.db.execute(select(Course).where(Course.id == course_id))
#         course = result.scalar_one_or_none()
#         if not course:
#             raise HTTPException(status_code=404, detail="Course not found")
#         await self.db.delete(course)
#         await self.db.commit()
