from fastapi import APIRouter, HTTPException
from schemas.video_schemas import VideoRequest, VideoStatisticsResponse
from services.analyze_video import get_video_statistics


router = APIRouter()

@router.post("/get-video-stats", response_model=VideoStatisticsResponse)
def get_thumbnail(request: VideoRequest):
    try:
        
        statistics = get_video_statistics(request.video_url)
        title = statistics['title']
        views = statistics['views']
        likes = statistics['likes']
        comments = statistics['comments']
        upload_date = statistics['upload_date']
        score = statistics['score']
        
        return VideoStatisticsResponse(
            url=request.video_url,
            stats={
                "title": title,
                "views": views,
                "likes": likes,
                "comments": comments,
                "upload_date": upload_date,
                "score": score
            }
        )
    
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Invalid data: {str(ve)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An internal error occurred: {str(e)}")