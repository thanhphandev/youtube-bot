from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from configs.config import Config
from utils.quality_score import calculate_quality_score
from utils.get_id_video import get_id_video
from utils.logger import setup_logger

logger = setup_logger(__name__)


API_KEY = Config.YOUTUBE_API_KEY
youtube = build("youtube", "v3", developerKey=API_KEY)


def get_video_statistics(url: str):
    try:
        video_id = get_id_video(url)
        if not video_id.strip():
            logger.warning("Video ID is empty or invalid.")
            return {"error": "Invalid video ID."}

        request = youtube.videos().list(
            part="snippet,statistics",
            id=video_id
        )
        response = request.execute()
        if response["items"]:
            video = response["items"][0]
            title = video["snippet"]["title"]
            description = video["snippet"]["description"]
            tags = video["snippet"].get("tags", [])
            upload_date = video["snippet"]["publishedAt"]
            view_count = video["statistics"]["viewCount"]
            like_count = video["statistics"].get("likeCount", "0")
            comment_count = video["statistics"].get("commentCount", "0")
            score = calculate_quality_score(view_count, like_count, comment_count, upload_date)
            logger.info("Get static video successful")
            return {
                "title": title,
                "description": description,
                "tags": tags,
                "views": view_count,
                "likes": like_count,
                "comments": comment_count,
                "upload_date": upload_date,
                "score": score
            }
        else:
            logger.warning("Has no information about the video")
            return None

    except HttpError as e:
        logger.error(f"An error occurred when get static video: {e}")
        return None