import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update
from telegram.constants import ChatAction
from configs.config import Config
from common.validator import Validator
from utils.logger import setup_logger
from handlers.help_handler import help_command
from handlers.summary_handler import summary_command
from handlers.download_handler import download_command
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


    async def _start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
       
        await update.message.reply_text(
            "Xin chào, tôi là Youtube AI Bot được tạo bởi Phan Văn Thành. Sử dụng /help để hiển thị các chức năng khả dụng."
        )


    async def _handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handler for general text messages."""
        await update.message.reply_text("I didn't understand that. Use /help to see available commands.")

    def run(self):
        """Run the bot."""
        logger.info("Bot is starting...")
        self.app.run_polling()
