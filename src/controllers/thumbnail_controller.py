from fastapi import APIRouter, HTTPException
from schemas.video_schemas import ThubmailRequest, VideoThumbnailResponse
from services.get_thumbnail import get_thumnail_by_url

router = APIRouter()

@router.post("/get-thumbnail", response_model=VideoThumbnailResponse)
def get_thumbnail(request: ThubmailRequest):
    try:
        thumbnail = get_thumnail_by_url(request.video_url, request.resolution)
        return VideoThumbnailResponse(**thumbnail)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Invalid data: {str(ve)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An internal error occurred: {str(e)}")