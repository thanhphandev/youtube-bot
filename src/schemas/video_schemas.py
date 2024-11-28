from pydantic import BaseModel
from typing import Dict

class VideoRequest(BaseModel):
    video_url: str

class ThubmailRequest(BaseModel):
    video_url: str

class VideoSummaryResponse(BaseModel):
    title: str
    content: str

class VideoThumbnailResponse(BaseModel):
    video_url: str
    thumbnails: Dict[str, str]

class VideoStatistics(BaseModel):
    title: str
    views: int
    likes: int
    comments: int
    score: float
    upload_date: str

class VideoStatisticsResponse(BaseModel):
    url: str
    stats: VideoStatistics

    


    

