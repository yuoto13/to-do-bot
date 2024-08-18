from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Добавить задачу", callback_data='add_task')],
        [InlineKeyboardButton("Просмотреть задачи", callback_data='list_tasks')],
        [InlineKeyboardButton("Анализ продуктивности", callback_data='view_stats')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привет! Выберите действие:', reply_markup=reply_markup)

start_handler = CommandHandler('start', start)