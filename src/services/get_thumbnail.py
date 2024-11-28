from utils.get_id_video import get_id_video
from utils.logger import setup_logger

logger = setup_logger(__name__)

def get_thumnail_by_url(url: str):
    """
    maxresdefault: The highest available resolution (usually 1280x720), but may not always be available.
    sddefault: Standard definition (usually 640x480).
    hqdefault: High quality (usually 480x360).
    mqdefault: Medium quality (usually 320x180).
    """
    video_id = get_id_video(url)

    default_url = f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"
    medium_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
    high_url = f"https://img.youtube.com/vi/{video_id}/sddefault.jpg"
    maxres_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

    logger.info(f"Extracted thumbnail successful {url}")
    return {
        "video_url": url,
        "thumbnails": {
            "default": default_url,
            "medium": medium_url,
            "high": high_url,
            "maxres": maxres_url
        }
    }