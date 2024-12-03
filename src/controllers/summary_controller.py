from fastapi import APIRouter, HTTPException
from schemas.video_schemas import VideoRequest, VideoSummaryResponse
from services.summary_video import summarize_video
from common.validator import Validator

router = APIRouter()

@router.post("/summarize-video", response_model=VideoSummaryResponse)
async def video_summarization(request: VideoRequest):
    try:
        if not request.video_url:
            raise ValueError("Required video URL")
        if Validator.is_valid_youtube_url(request.video_url) == False:
            raise ValueError("Invalid YouTube video URL")
        summary = summarize_video(request.video_url)

        title = summary.get('title', 'No Title')
        content = summary.get('content', 'No Content')
        
        return VideoSummaryResponse(
            title=title,
            content=content
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Invalid data: {str(ve)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An internal error occurred: {str(e)}")
