import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackQueryHandler
from common.validator import Validator
from utils.logger import setup_logger
from services.download_video import download_youtube_video
from utils.get_id_video import get_id_video
from utils.get_thumbnail import get_youtube_thumbnail

logger = setup_logger(__name__)

async def download_command(update: Update, context):
    """Handles the /download command and sends inline buttons for video quality options."""
    if not context.args:
        await update.message.reply_text(
            "Câu lệnh không hợp lệ! Hãy gửi dưới dạng:\n /download https://youtu.be/example"
        )
        return

    video_url = context.args[0]

    # Validate YouTube URL
    if not Validator.is_valid_youtube_url(video_url):
        await update.message.reply_text("URL không hợp lệ! Hãy gửi URL của video YouTube.")
        return

    # Create inline buttons for video quality options
    keyboard = [
        [InlineKeyboardButton("480p", callback_data=f"480p|{video_url}")],
        [InlineKeyboardButton("720p", callback_data=f"720p|{video_url}")],
        [InlineKeyboardButton("1080p", callback_data=f"1080p|{video_url}")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Ask the user to choose video quality
    await update.message.reply_text(
        "Chọn chất lượng video bạn muốn tải:", reply_markup=reply_markup
    )

async def button_click_handler(update: Update, context):
    """Handles callback query when the user selects video quality."""
    query = update.callback_query
    video_quality, video_url = query.data.split("|")  # Get video quality and URL from callback_data
    video_url = video_url.strip()

    # Answer the callback query
    await query.answer()
    await query.edit_message_text(text=f"Bạn đã chọn chất lượng {video_quality}. Đang tải video...")

    try:
        # Download the video with the chosen quality
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

        os.remove(video_path)

    except Exception as e:
        logger.error(f"Error downloading video: {str(e)}")
        await query.message.reply_text(f"❌ Lỗi khi tải video: {str(e)}")


def register_handlers(dispatcher):
    """Register all the handlers."""
    dispatcher.add_handler(CallbackQueryHandler(button_click_handler))
