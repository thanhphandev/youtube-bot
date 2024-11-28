from fastapi import APIRouter, HTTPException
from schemas.video_schemas import VideoRequest, VideoStatisticsResponse
from services.analyze_video import get_video_statistics


router = APIRouter()

@router.post("/get-statistics", response_model=VideoStatisticsResponse)
def get_thumbnail(request: VideoRequest):
    try:
        
        statistics = get_video_statistics(request.video_url)
        title = statistics['title']
        views = statistics['views']
        likes = statistics['likes']
        comments = statistics['comments']
        score = statistics['score']
        
        return VideoStatisticsResponse(
            title=title,
            views=views,
            likes=likes,
            comments=comments,
            score=score
        )
    
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Invalid data: {str(ve)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An internal error occurred: {str(e)}")