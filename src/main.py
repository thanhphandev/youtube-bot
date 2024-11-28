from fastapi import FastAPI
from controllers.summary_controller import router as video_router
from controllers.thumbnail_controller import router as thumbnail_router
from controllers.statistics_controller import router as statistics_router

app = FastAPI()

app.include_router(video_router, prefix="/api/v1", tags=["Video"])
app.include_router(thumbnail_router, prefix="/api/v1", tags=["Video"])
app.include_router(statistics_router, prefix="/api/v1", tags=["Video"])


