from utils.summary_ai import summarize_video_content
from utils.transcript_video import YouTubeTranscriptExtractor
from services.analyze_video import get_video_statistics
from utils.logger import setup_logger

logger = setup_logger(__name__)

def summarize_video(video_url: str):
    try:
        transcript = YouTubeTranscriptExtractor.extract_transcript(video_url)
        if transcript["status"] == "error":
            logger.error(f"Failed to extract transcript for video: {video_url}, Message: {transcript['message']}")
            return {
                "status": "error",
                "content": f"Failed to extract transcript: {transcript['message']}",
                "url": video_url
            }
        statistics = get_video_statistics(video_url)
        transcript_text = transcript["data"]["transcript"]
        summary_content = summarize_video_content(transcript_text)
        title = statistics['title']
        logger.info(f"Video summarized successfully")
        return {
            "status": "success",
            "title": title,
            "content": summary_content,
            "url": video_url
        }

    except Exception as e:
        logger.error(f"An error occurred during summarization: {str(e)}")
        return {
            "status": "error",
            "content": "An error occurred during summarization.",
            "url": video_url
        }

