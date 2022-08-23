from telegram.ext import Updater, CommandHandler

def start(update, context):
	update.message.reply_text('Hi <b>{}!</b>\n in<b>This bot always help you</b>')

def main():
	updater = Updater('5533885238:AAFfxPI78pmnxsbBR2xn7Xq39mIhWb6aoJE', use_context=True)

	dispatcher = updater.dispatcher

	dispatcher.add_header(CommandHandler('start', start))

	updater.start_polling()
	updater.idle()

main()