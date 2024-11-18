from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from configs.config import Config
from utils.logger import setup_logger

logger = setup_logger(__name__)


API_KEY = Config.YOUTUBE_API_KEY
youtube = build("youtube", "v3", developerKey=API_KEY)


def get_video_statistics(video_id: str):
    try:
        # Lấy thông tin video
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
            view_count = video["statistics"]["viewCount"]
            like_count = video["statistics"].get("likeCount", "0")
            comment_count = video["statistics"].get("commentCount", "0")

            # Trả về thông tin video và các chỉ số
            return {
                "title": title,
                "description": description,
                "tags": tags,
                "view_count": view_count,
                "like_count": like_count,
                "comment_count": comment_count,
            }
        else:
            return None

    except HttpError as err:
        logger.error(f"An error occurred: {err}")
        return None