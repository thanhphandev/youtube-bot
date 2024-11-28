from pydantic import BaseModel
from enum import Enum

class VideoRequest(BaseModel):
    video_url: str

class ThubmailRequest(BaseModel):
    video_url: str
    resolution: str

class VideoSummaryResponse(BaseModel):
    content: str

class VideoThumbnailResponse(BaseModel):
    thumbnail_url: str

class VideoStatisticsResponse(BaseModel):
    title: str
    views: int
    likes: int
    comments: int
    score: float
    

