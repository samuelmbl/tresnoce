"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import os
import logging
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


bot_token = os.environ['bot_token']
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def tres_no_ce(update,context):
    chat_id = update.message.chat_id
    try:
        # args[0] should contain the time for the timer in seconds
        name = context.args[0]
        update.message.reply_text('Três no ce, {}'.format(name))

        gif_url = 'https://media0.giphy.com/media/26tPsS788ZFNT0nU4/giphy.gif'
        send_gif = 'https://api.telegram.org/bot' + bot_token + '/sendAnimation?chat_id=' + str(chat_id) + '&animation=' + gif_url
        response = requests.get(send_gif)

    except (IndexError, ValueError) as e:
        print(str(e))


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    # Create the Updater and pass it your bot's token.
    updater = Updater(bot_token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("tres", tres_no_ce,
                                  pass_args=True,
                                  pass_chat_data=True))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()