from groq import Groq
from configs.config import Config
from utils.logger import setup_logger


model_name = "llama3-70b-8192"

client = Groq(
    api_key=Config.GROQ_API_KEY
)

def summarize_video_content(content: str) -> str:
    """Tóm tắt nội dung video từ transcript."""
    prompt = f"Đây là nội dung:\n\n{content}\n\n"

    try:
        # Gửi yêu cầu tới API OpenAI để tóm tắt nội dung
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": ("Bạn là một nhà tóm tắt nội dung video. "
                                                "Hãy tóm tắt nội dung video sau đây thành một bản tóm tắt ngắn gọn và chính xác. "
                                                "Tập trung vào việc tóm tắt video không nói thêm thông tin gì:"
                                                "Chỉ phản hồi bằng tiếng Việt.")},
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
            top_p=1.0,
            max_tokens=1024,
            model=model_name,
        )
        
        # Lấy và trả về nội dung tóm tắt
        summary = response.choices[0].message.content
        return summary
    
    except Exception as e:
        return Exception(f"An error occurred during summarization: {str(e)}")
