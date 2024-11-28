from utils.get_id_video import get_id_video
from utils.logger import setup_logger

logger = setup_logger(__name__)

def get_thumnail_by_url(url, resolution="maxresdefault"):
    """
    maxresdefault: The highest available resolution (usually 1280x720), but may not always be available.
    sddefault: Standard definition (usually 640x480).
    hqdefault: High quality (usually 480x360).
    mqdefault: Medium quality (usually 320x180).
    """
    video_id = get_id_video(url)
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/{resolution}.jpg"
    logger.info(f"Thumbnail URL: {thumbnail_url}")
    return {
        "thumbnail_url": thumbnail_url
    }