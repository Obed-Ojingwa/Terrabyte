# C:\Users\Melody\Documents\workinprog\terrabyte\backend\app\schemas\course.py
from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from app.models.course import CourseMode, CourseTier


class CourseCreate(BaseModel):
    title: str
    description: Optional[str] = None
    price: float = 0
    mode: CourseMode = CourseMode.online
    category: Optional[str] = None
    tier: CourseTier = CourseTier.beginner
    duration_days: Optional[int] = None
    duration_weeks: Optional[int] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    schedule_notes: Optional[str] = None
    what_you_learn: Optional[str] = None
    requirements: Optional[str] = None
    target_audience: Optional[str] = None
    thumbnail_url: Optional[str] = None
    is_published: bool = False
    tutor_id: Optional[int] = None


class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    mode: Optional[CourseMode] = None
    category: Optional[str] = None
    tier: Optional[CourseTier] = None
    duration_days: Optional[int] = None
    duration_weeks: Optional[int] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    schedule_notes: Optional[str] = None
    what_you_learn: Optional[str] = None
    requirements: Optional[str] = None
    target_audience: Optional[str] = None
    thumbnail_url: Optional[str] = None
    is_published: Optional[bool] = None
    tutor_id: Optional[int] = None


class CourseOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    price: float
    mode: CourseMode
    category: Optional[str]
    tier: CourseTier
    duration_days: Optional[int]
    duration_weeks: Optional[int]
    start_date: Optional[date]
    end_date: Optional[date]
    schedule_notes: Optional[str]
    what_you_learn: Optional[str]
    requirements: Optional[str]
    target_audience: Optional[str]
    thumbnail_url: Optional[str]
    is_published: bool
    tutor_id: Optional[int]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True