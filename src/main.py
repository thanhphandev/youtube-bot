from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.summary_controller import router as video_router
from controllers.thumbnail_controller import router as thumbnail_router
from controllers.statistics_controller import router as statistics_router

app = FastAPI()

# CORS setup
origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins from the specified list
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Include routers for different endpoints
app.include_router(video_router, prefix="/api/v1", tags=["Video"])
app.include_router(thumbnail_router, prefix="/api/v1", tags=["Video"])
app.include_router(statistics_router, prefix="/api/v1", tags=["Video"])

