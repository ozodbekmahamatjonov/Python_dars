from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, Commandler 

button = ReplyKeyboardMarkup([['Statistika']])


def start(update, context):
	update.massage.reply_text(
		'Salom{}'.format(update.message.from_user.first_name))


update = Updater('5592094640:AAEM6getZ-0jx5T4ARYVk1zvNBPosrsL8', use_context=True)
update.dispatcher.add_handler(CommandHandler('start', start))

update.start_polling()
updater.idle()