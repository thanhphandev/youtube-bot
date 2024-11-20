import os
import yt_dlp
from utils.logger import setup_logger


logger = setup_logger(__name__)

TEMP_DIR = "downloads"


def download_youtube_video(video_url: str, resolution: str = "720p") -> str:
    try:
        
        os.makedirs(TEMP_DIR, exist_ok=True)
        ydl_opts = {
            'format': f'bestvideo[height<={resolution.rstrip("p")}]' + '+bestaudio/best',
            'outtmpl': os.path.join(TEMP_DIR, '%(id)s.%(ext)s'),
            'merge_output_format': 'mp4',  # Specify output format for merged video (mp4)
        }

        # Download the video using yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)

            file_extension = info_dict.get('ext', 'mp4')
            output_path = os.path.join(TEMP_DIR, f"{info_dict['id']}.{file_extension}")
            return output_path
        
    except Exception as e:
        logger.error(f"Error downloading video: {str(e)}")
        raise Exception(f"Error downloading video: {str(e)}") from e
