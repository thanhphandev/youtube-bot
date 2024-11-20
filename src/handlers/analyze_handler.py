from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes
from common.validator import Validator
from services.analyze_video import get_video_statistics
from utils.get_id_video import get_id_video
from utils.logger import setup_logger
from utils.quality_score import calculate_quality_score

logger = setup_logger(__name__)


async def analyze_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
                "Câu lệnh không hợp lệ! Hãy gửi dưới dạng:\n /analyze https://youtu.be/example"
        )
        return
    
    video_url = context.args[0]
    video_id = get_id_video(video_url)

    if(not Validator.is_valid_youtube_url(video_url)):
        await update.message.reply_text("URL không hợp lệ! Hãy gửi URL của video YouTube.")
        return
    try:
    
        await update.message.chat.send_action(action=ChatAction.TYPING)
        logger.info(f"Analyzing video: {video_id}")
        statistics_video = get_video_statistics(video_id)
        
        if not statistics_video:
            await update.message.reply_text("Không thể lấy thông tin video.")
            return
        
        title = statistics_video["title"]
        description = statistics_video["description"]
        tags = statistics_video["tags"]
        views = statistics_video["view_count"]
        likes = statistics_video["like_count"]
        comments = statistics_video["comment_count"]
        upload_date = statistics_video["upload_date"]
        score = calculate_quality_score(views, likes, comments, upload_date)
        await update.message.reply_text(
            f"📹 Tiêu đề: {title}\n"
            f"📝 Mô tả: {description}\n"
            f"🏷 Tags: {', '.join(tags)}\n"
            f"👀 Lượt xem: {views}\n"
            f"👍 Lượt thích: {likes}\n"
            f"💬 Lượt bình luận: {comments}\n"
            f"📅 Ngày tải lên: {upload_date}\n"
            f"🌟 Điểm chất lượng: {score}/ 100"
            )
    except Exception as e:
        logger.error(f"Error when analyze video: {e}")
        await update.message.reply_text("Đã có vấn đề khi phân tích video! vui lòng thử lại.")    
    