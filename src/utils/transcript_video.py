from utils.logger import setup_logger
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
)
from utils.get_id_video import get_id_video

logger = setup_logger(__name__)

class YouTubeTranscriptExtractor:
    @staticmethod
    def extract_transcript(video_url: str, preferred_languages=None) -> dict:
        
        if preferred_languages is None:
            preferred_languages = ['vi', 'en', 'auto']

        try:
            video_id = get_id_video(video_url)
            logger.info(f"Extracting transcript for video ID: {video_id}")

            for lang_code in preferred_languages:
                try:
                    logger.info(f"Trying language: {lang_code}")
                    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang_code])
                    transcript_text = " ".join(entry['text'] for entry in transcript)
                    return {
                        "status": "success",
                        "message": "Transcript retrieved successfully.",
                        "data": {
                            "video_url": video_url,
                            "language": lang_code,
                            "transcript": transcript_text,
                        }
                    }
                except TranscriptsDisabled:
                    logger.warning(f"Transcripts are disabled for video ID: {video_id} in language: {lang_code}")
                    return {
                        "status": "error",
                        "message": "Transcripts are disabled for this video.",
                        "data": {
                            "video_url": video_url,
                        }
                    }
                except NoTranscriptFound:
                    logger.info(f"No transcript found for language: {lang_code}")
                    continue

            # No transcripts found in preferred languages
            logger.warning(f"No transcript available in preferred languages for video ID: {video_id}")
            return {
                "status": "error",
                "message": "No transcript available in the preferred languages.",
                "data": {
                    "video_url": video_url,
                }
            }
        
        except VideoUnavailable:
            logger.error(f"Video is unavailable: {video_url}")
            return {
                "status": "error",
                "message": "Video is unavailable.",
                "data": {
                    "video_url": video_url,
                }
            }
        except Exception as e:
            logger.error(f"An error occurred while extracting the transcript: {str(e)}")
            return {
                "status": "error",
                "message": f"An error occurred while extracting the transcript: {str(e)}",
                "data": {
                    "video_url": video_url,
                }
            }
