from utils.summary_ai import summarize_video_content
from utils.transcript_video import YouTubeTranscriptExtractor

def summarize_video(video_url: str) -> str:
    
    transcript = YouTubeTranscriptExtractor.extract_transcript(video_url)

    try:
        summary_content = summarize_video_content(transcript)
        return summary_content
    except Exception as e:
        return f"An error occurred during summarization: {str(e)}"
