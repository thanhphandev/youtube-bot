import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from common.validator import Validator
from telegram.ext import ContextTypes
from utils.logger import setup_logger
from services.download_video import download_youtube_video
from utils.get_id_video import get_id_video
from utils.get_thumbnail import get_youtube_thumbnail

logger = setup_logger(__name__)

async def download_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /download command and sends inline buttons for video quality options."""
    if not context.args:
        await update.message.reply_text(
            "Câu lệnh không hợp lệ! Hãy gửi dưới dạng:\n /download https://youtu.be/example"
        )
        return

    video_url = context.args[0]

    if not Validator.is_valid_youtube_url(video_url):
        await update.message.reply_text("URL không hợp lệ! Hãy gửi URL của video YouTube.")
        return

    keyboard = [
        [InlineKeyboardButton("480p", callback_data=f"480p|{video_url}")],
        [InlineKeyboardButton("720p", callback_data=f"720p|{video_url}")],
        [InlineKeyboardButton("1080p", callback_data=f"1080p|{video_url}")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Chọn chất lượng video bạn muốn tải:", reply_markup=reply_markup
    )

async def sellected_video_quality(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles callback query when the user selects video quality."""
    query = update.callback_query
    video_quality, video_url = query.data.split("|")  # Get video quality and URL from callback_data
    video_url = video_url.strip()

    await query.answer()
    await query.edit_message_text(text=f"Bạn đã chọn chất lượng {video_quality}. Đang tải video...")

    try:

        video_path = download_youtube_video(video_url, resolution=video_quality)
        video_id = get_id_video(video_url)
        thumbnail_path = get_youtube_thumbnail(video_id)

        if not video_path:
            await query.edit_message_text("Không thể tải video. Vui lòng thử lại.")
            return

        # Send the video to the user
        with open(video_path, "rb") as video_file:
            thumbnail = open(thumbnail_path, "rb") if thumbnail_path else None
            await query.message.reply_video(
                video=video_file,
                caption=f"📹 Video đã được tải xuống từ: {video_url}",
                supports_streaming=True,
                thumbnail=thumbnail,
            )
            logger.info(f"Video sent successfully: {video_url}")
            thumbnail.close() if thumbnail else None
        os.remove(video_path)
        if thumbnail_path:
            os.remove(thumbnail_path)

    except Exception as e:
        logger.error(f"Error downloading video: {e}")

