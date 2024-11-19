import re
import os
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes
from common.validator import Validator
from services.download_video import download_youtube_video
from utils.get_thumbnail import get_youtube_thumbnail
from utils.logger import setup_logger

logger = setup_logger(__name__)
MAX_FILE_SIZE_MB = 50 

async def download_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        Xử lý lệnh /download <YouTube URL>.
        """
        if not context.args:
            await update.message.reply_text(
                "Câu lệnh không hợp lệ! Hãy gửi dưới dạng:\n /download https://youtu.be/example"
            )
            return

        video_url = context.args[0]
        if(not Validator.is_valid_youtube_url(video_url)):
            await update.message.reply_text("URL không hợp lệ! Hãy gửi URL của video YouTube.")
            return
        match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', video_url)
        video_id = match.group(1)

        await update.message.chat.send_action(action=ChatAction.TYPING)
        try:
            video_path = download_youtube_video(video_url)
            thumbnail_path = get_youtube_thumbnail(video_id)

            await update.message.reply_text("Đang gửi video, vui lòng chờ...")
            caption = f"📹 Video đã được tải xuống từ: {video_url}"
            # Gửi video tới người dùng
            with open(video_path, "rb") as video_file:
                thumbnail = open(thumbnail_path, "rb") if thumbnail_path else None
                await update.message.reply_video(
                    video=video_file,
                    caption=caption,
                    supports_streaming=True,
                    thumbnail=thumbnail
                )
                if thumbnail:
                    thumbnail.close()
            os.remove(video_path)
            logger.info(f"Video sent successfully: {video_url}")

        except FileNotFoundError:
            logger.error(f"File not found for URL: {video_url}")
            await update.message.reply_text("Không tìm thấy file video sau khi tải. Vui lòng thử lại.")

        except Exception as e:
            logger.error(f"Error downloading video: {str(e)}")
            await update.message.reply_text(f"❌ Lỗi khi tải video: {str(e)}")

