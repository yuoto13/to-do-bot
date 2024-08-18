from threading import Timer
from telegram.ext import CallbackQueryHandler, MessageHandler, Filters
from datetime import datetime, timedelta
from utils.database import get_tasks

def set_reminder(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="За сколько времени до срока вам напомнить? Введите количество минут:")

def reminder_handler(update, context):
    user_id = update.message.from_user.id
    task = context.user_data.get('task')
    reminder_time = int(update.message.text)
    
    if task.deadline is None:
        update.message.reply_text("Сначала установите срок задачи.")
        return
    
    reminder_seconds = reminder_time * 60
    reminder_datetime = task.deadline - timedelta(seconds=reminder_seconds)
    current_time = datetime.now()

    if reminder_datetime > current_time:
        delay = (reminder_datetime - current_time).total_seconds()
        Timer(delay, send_reminder, [update, context, task]).start()
        update.message.reply_text(f"Напоминание установлено за {reminder_time} минут до срока.")
    else:
        update.message.reply_text("Указанное время для напоминания уже прошло. Пожалуйста, установите более раннее напоминание.")

def send_reminder(update, context, task):
    user_id = update.message.from_user.id
    context.bot.send_message(chat_id=user_id, text=f"Напоминание: Задача '{task.description}' должна быть завершена скоро!")

reminder_handler_list = [
    CallbackQueryHandler(set_reminder, pattern='^set_reminder$'),
    MessageHandler(Filters.text & ~Filters.command, reminder_handler)
]