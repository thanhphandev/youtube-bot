import re
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes
from common.validator import Validator
from services.analyze_video import get_video_statistics
from utils.logger import setup_logger

logger = setup_logger(__name__)


async def analyze_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
                "Câu lệnh không hợp lệ! Hãy gửi dưới dạng:\n /analyze https://youtu.be/example"
        )
        return

    video_url = context.args[0]
    if(not Validator.is_valid_youtube_url(video_url)):
        await update.message.reply_text("URL không hợp lệ! Hãy gửi URL của video YouTube.")
        return
    await update.message.chat.send_action(action=ChatAction.TYPING)
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', video_url)
    video_id = match.group(1)
    logger.info(f"Analyzing video: {video_id}")
    static_video = get_video_statistics(video_id)
    if not static_video:
        await update.message.reply_text("Không thể lấy thông tin video.")
        return
    title = static_video["title"]
    description = static_video["description"]
    tags = static_video["tags"]
    views = static_video["view_count"]
    likes =static_video["like_count"]
    comments = static_video["comment_count"]
    await update.message.reply_text(
        f"📹 Tiêu đề: {title}\n"
        f"📝 Mô tả: {description}\n"
        f"🏷 Tags: {', '.join(tags)}\n"
        f"👀 Lượt xem: {views}\n"
        f"👍 Lượt thích: {likes}\n"
        f"💬 Lượt bình luận: {comments}")