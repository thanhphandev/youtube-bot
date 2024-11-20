from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
       
        help_text = (
            "Chức năng khả dụng:\n"
            "/summary [url] - Tóm tắt nội dung video\n"
            "/download [url] - Download YouTube video (chỉ cho phép video từ 50Mb trở xuống)\n"
            "/analyze [url] - Phân tích các chỉ số video\n"
            "/thumbnail [url] - Lấy hình thumbnail của video\n"
            "/semantic [url] - Phân tích comment video\n"
            "/help - Hiển thị trợ giúp"
        )
        await update.message.reply_text(help_text)
        