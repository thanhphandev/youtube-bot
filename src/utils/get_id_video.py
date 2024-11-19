import re

def get_id_video(video_url: str) -> str:
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', video_url)
    return match.group(1) if match else None