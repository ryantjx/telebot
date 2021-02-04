from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from moneyGooseBot.credentials import bot_token
from moneyGooseBot.master_mind import mainCommandHandler

def main():
    updater = Updater(bot_token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',mainCommandHandler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()