import logging
import telegram
from telegram.ext import Filters, Updater, MessageHandler
from settings import BOT_TOKEN


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = 'TOKEN'
bot = telegram.Bot(TOKEN)


def start(update, context):
    update.message.reply_text('Здравствуйте')


def main():
    updater = Updater(TOKEN, use_context=True)

    updater.dispatcher.add_handler(MessageHandler(Filters.text, start))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
