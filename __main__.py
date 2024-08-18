from telegram.ext import Updater
from config import TOKEN
from handlers.start import start_handler
from handlers.task_management import task_management_handler
from handlers.reminders import reminder_handler_list
from handlers.buttons import button_handler

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(start_handler)
    for handler in task_management_handler:
        dp.add_handler(handler)
    for handler in reminder_handler_list:
        dp.add_handler(handler)
    dp.add_handler(button_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()