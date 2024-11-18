import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

class YouTubeTranscriptExtractor:
    def extract_transcript(video_url: str, preferred_languages=None):
        
        if preferred_languages is None:
            preferred_languages = ['en', 'vi', 'auto']

        try:
            match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', video_url)
            if not match:
                return "Invalid YouTube video URL"
            video_id = match.group(1)

            # Attempt to fetch transcript in preferred languages
            for lang_code in preferred_languages:
                try:
                    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang_code])
                    return " ".join(entry['text'] for entry in transcript)
                except NoTranscriptFound:
                    continue  # Try the next language if no transcript is found
                except TranscriptsDisabled:
                    return "Transcripts are disabled for this video"

            # If no transcript is available in any of the preferred languages
            return "No transcript available in the preferred languages"
        
        except Exception as e:
            return f"An error occurred while extracting the transcript: {str(e)}"
