import os
import requests
from utils.logger import setup_logger

logger = setup_logger(__name__)

TEMP_DIR = "downloads"

def get_youtube_thumbnail(video_id: str, resolution: str = "maxresdefault") -> str:

    try:
        os.makedirs(TEMP_DIR, exist_ok=True)
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/{resolution}.jpg"
        thumbnail_path = os.path.join(TEMP_DIR, f"{video_id}_hqdefault.jpg")

        response = requests.get(thumbnail_url, stream=True)
        if response.status_code == 200:
            with open(thumbnail_path, "wb") as thumbnail_file:
                for chunk in response.iter_content(1024):
                    thumbnail_file.write(chunk)
            logger.info(f"Thumbnail downloaded: {thumbnail_path}")
            return thumbnail_path
        else:
            logger.warning(f"Failed to fetch thumbnail: {thumbnail_url} (HTTP {response.status_code})")
            return None

    except Exception as e:
        logger.error(f"Error downloading thumbnail for video ID {video_id}: {str(e)}")
        return None
