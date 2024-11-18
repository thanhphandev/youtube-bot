import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    YOUTUBE_API_KEY=os.getenv('YOUTUBE_API_KEY')
