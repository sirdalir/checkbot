import sys

import logging
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler
from emoji import emojize
from telegram.ext import BaseFilter


# class FilterStats(BaseFilter):
#     def filter(self, message):
#         return 'stats' == message.text


# class FilterCount(BaseFilter):
#     def filter(self, message):
#         return 'count' == message.text


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

CHAT_ID = None
TOKEN = 'TOKEN'
bot = telegram.Bot(TOKEN)

added_emoji = {"approved": emojize(":white_check_mark:", use_aliases=True),
               "declined": emojize(":x:", use_aliases=True)}


def button(update, context):
    query = update.callback_query

    message_text = query.message['text']
    message_id = query.message['message_id']
    # Remove keyboards
    callback_data = query.data

    # If message text looks like username$exercise
    username, exercise = message_text.split("$")

    # Remove keyboards
    query.edit_message_reply_markup(reply_markup=None)

    # Add results
    # add_batch_check_result(message_id=message_id,
    #                        username=username,
    #                        exercise=exercise,
    #                        approve=True if callback_data == 'approved' else False)

    # Add emoji to message
    # query.edit_message_text(text=f"{message_text}    {added_emoji[callback_data]}")


### Commands

def stats(update, context):
    pass
    # viz = open(matplot_lib_viz(), 'rb')
    # bot.send_photo(chat_id=CHAT_ID, photo=viz)
    # viz.close()


def count(update, context):
    pass
    # viz = open(exercises_matplot_viz(), 'rb')
    # bot.send_photo(chat_id=CHAT_ID, photo=viz)
    # viz.close()


def main():
    updater = Updater(TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('stats', stats))
    updater.dispatcher.add_handler(CommandHandler('count', count))
    # updater.dispatcher.add_handler(MessageHandler(FilterStats(), stats))
    # updater.dispatcher.add_handler(MessageHandler(FilterCount(), count))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
