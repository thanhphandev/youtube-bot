from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes
from common.validator import Validator
from services.summary_video import summarize_video
from utils.logger import setup_logger

logger = setup_logger(__name__)

async def summary_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handler for the /summary command."""
        if not context.args:
            await update.message.reply_text("Câu lệnh không hợp lệ! Hãy gửi dưới dạng\n /summary https://youtu.be/example")
            return

        video_url = context.args[0]
        if(not Validator.is_valid_youtube_url(video_url)):
            await update.message.reply_text("URL không hợp lệ! Hãy gửi URL của video YouTube.")
            return

        try:
            await update.message.chat.send_action(ChatAction.TYPING)
            summary = summarize_video(video_url)
            logger.info(f"Video summarized successfully: {len(summary)} characters")
            await update.message.reply_text(summary)
        except Exception as e:
            logger.error(f"Quá trình tóm tắt video đã xảy ra lỗi: {e}")
            await update.message.reply_text("Đã có vấn đề xảy ra! vui lòng thử lại.")