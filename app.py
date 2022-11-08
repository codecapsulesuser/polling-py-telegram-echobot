import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hey! I respond by echoing messages. Give it a try!")

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def main():
    TOKEN = os.getenv('BOT_TOKEN')
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", start)

    dispatcher.add_handler(start_handler)

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()

if __name__ == '__main__':
    main()
