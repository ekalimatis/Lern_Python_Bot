import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from settings import API_KEY

logging.basicConfig(filename = 'bot.log', level = logging.INFO)

def greet_user(update, context):
    logging.info('Start', update, context)
    update.message.reply_text('Привет')

def answer_me(update, context):
    update.message.reply_text(update.message.text)

def main():
    mybot = Updater(API_KEY, use_context = True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, answer_me))

    logging.info('Start')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()