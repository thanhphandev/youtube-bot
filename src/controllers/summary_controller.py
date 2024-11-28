from fastapi import APIRouter, HTTPException
from schemas.video_schemas import VideoRequest, VideoSummaryResponse
from services.summary_video import summarize_video

router = APIRouter()

@router.post("/summarize-video", response_model=VideoSummaryResponse)
async def video_summarization(request: VideoRequest):
    try:
        summary = summarize_video(request.video_url)
        return VideoSummaryResponse(**summary)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Invalid data: {str(ve)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An internal error occurred: {str(e)}")
