import signal
import sys
from core.tele_bot import TelegramBot
from utils.logger import setup_logger

logger = setup_logger(__name__)

def handle_exit(signum, frame):
    print("\nExiting program...")
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, handle_exit)
    bot = TelegramBot()
    bot.run()

if __name__ == '__main__':
    main()
