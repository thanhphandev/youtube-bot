from fastapi import APIRouter, HTTPException
from schemas.video_schemas import ThubmailRequest, VideoThumbnailResponse
from services.get_thumbnail import get_thumnail_by_url
from common.validator import Validator

router = APIRouter()

@router.post("/get-thumbnail", response_model=VideoThumbnailResponse)
def get_thumbnail(request: ThubmailRequest):
    try:
        if not request.video_url:
            raise ValueError("Required video URL")
        if not Validator.is_valid_youtube_url(request.video_url):
            raise ValueError("Invalid YouTube video URL")
        
        thumbnail = get_thumnail_by_url(request.video_url)
        return VideoThumbnailResponse(**thumbnail)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Invalid data: {str(ve)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An internal error occurred: {str(e)}")