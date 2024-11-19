from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update
from configs.config import Config
from utils.logger import setup_logger
from handlers.help_handler import help_command
from handlers.summary_handler import summary_command
from handlers.download_handler import download_command
from handlers import download_handler
from handlers.analyze_handler import analyze_command

logger = setup_logger(__name__)

class TelegramBot:

    def __init__(self):
        self.app = Application.builder().token(Config.BOT_TOKEN).build()
        self._setup_handlers()

    def _setup_handlers(self):     
        self.app.add_handler(CommandHandler('start', self._start))
        self.app.add_handler(CommandHandler('help', help_command))
        self.app.add_handler(CommandHandler('summary', summary_command))
        self.app.add_handler(CommandHandler('download', download_command))
        self.app.add_handler(CommandHandler('analyze', analyze_command))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_message))
        download_handler.register_handlers(self.app)


    async def _start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):    
        await update.message.reply_text(
            "Xin chào, tôi là Youtube AI Bot được tạo bởi Phan Văn Thành. Sử dụng /help để hiển thị các chức năng khả dụng."
        )

    async def _handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Tôi không hiểu bạn nói gì. Sử dụng /help để hiển thị các câu lệnh khả dụng.")

    def run(self):
        logger.info("Bot is starting...Press Ctrl + C to stop.")
        self.app.run_polling()
