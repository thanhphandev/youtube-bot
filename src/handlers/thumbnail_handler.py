import os
from common.validator import Validator
from telegram.constants import ChatAction
from utils.get_id_video import get_id_video
from utils.logger import setup_logger
from telegram import Update
from telegram.ext import ContextTypes
from utils.get_thumbnail import get_youtube_thumbnail

logger = setup_logger(__name__)

async def thumbnail_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Câu lệnh không hợp lệ! Hãy gửi dưới dạng:\n /thumbnail https://youtu.be/example"
        )
        return

    video_url = context.args[0]
    video_id = get_id_video(video_url)

    if not Validator.is_valid_youtube_url(video_url):
        await update.message.reply_text("URL không hợp lệ! Hãy gửi URL của video YouTube.")
        return
    
    try:
        await update.message.chat.send_action(action=ChatAction.UPLOAD_PHOTO)
        thumbnail_url = get_youtube_thumbnail(video_id)
        with open(thumbnail_url, "rb") as thumbnail:
            await update.message.reply_photo(
                photo=thumbnail,
                caption=f"Đây là thumbnail của video {video_url}"
            )
            os.remove(thumbnail_url)

    except Exception as e:
        logger.error(f"Error when get thumbnail: {e}")
        await update.message.reply_text("Đã có vấn đề xảy ra khi lấy thumnail! vui lòng thử lại.")