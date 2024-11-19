import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled
from utils.get_id_video import get_id_video

class YouTubeTranscriptExtractor:
    def extract_transcript(video_url: str, preferred_languages=None) -> str:
        
        if preferred_languages is None:
            preferred_languages = ['en', 'vi', 'auto']

        try:
            video_id = get_id_video(video_url)

            for lang_code in preferred_languages:
                try:
                    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang_code])
                    return " ".join(entry['text'] for entry in transcript)
                except TranscriptsDisabled:
                    # Transcripts bị tắt ở video này
                    return "Transcripts are disabled for this video"
            # Không có transcript nào trong các ngôn ngữ khả dụng
            return "No transcript available in the preferred languages"
        
        except Exception as e:
            return f"An error occurred while extracting the transcript: {str(e)}"
