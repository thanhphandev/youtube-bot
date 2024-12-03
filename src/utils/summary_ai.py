from groq import Groq
from configs.config import Config
from utils.logger import setup_logger

logger = setup_logger(__name__)

model_name = "llama3-70b-8192"

client = Groq(
    api_key=Config.GROQ_API_KEY
)

def summarize_video_content(content: str) -> str:
    prompt = f"Đây là nội dung video:\n\n{content}\n\n"

    try:
        
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": ("Bạn là một nhà tóm tắt nội dung video. "
                                                "Hãy tóm tắt nội dung video sau đây thành một bản tóm tắt chính xác và đầy đủ, toàn vẹn nội dung "
                                                "Luôn luôn phản hồi bằng tiếng Việt không có ngoại lệ."
                                                "no yapping, just summarizing"
                                                )},
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
            top_p=1.0,
            max_tokens=1024,
            model=model_name,
        )
        summary = response.choices[0].message.content
        return summary
    
    except Exception as e:
        logger.error(f"Error when summarizing content: {str(e)}")
        return Exception(f"An error occurred during summarization: {str(e)}")
