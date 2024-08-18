from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, MessageHandler, Filters
from models.task import Task
from utils.database import add_task, get_tasks, delete_task, complete_task

def add_task(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Пожалуйста, напишите описание задачи.")
    context.user_data['action'] = 'add_task_description'

def handle_message(update, context):
    user_action = context.user_data.get('action')
    user_id = update.message.from_user.id

    if user_action == 'add_task_description':
        task_description = update.message.text
        task = Task(description=task_description)
        add_task(user_id, task)
        context.user_data['task'] = task
        context.user_data['action'] = None

        keyboard = [
            [InlineKeyboardButton("Установить приоритет", callback_data='set_priority')],
            [InlineKeyboardButton("Установить срок", callback_data='set_deadline')],
            [InlineKeyboardButton("Установить напоминание", callback_data='set_reminder')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Выберите действие для задачи:', reply_markup=reply_markup)

def list_tasks(update, context):
    query = update.callback_query
    query.answer()
    user_id = query.from_user.id
    tasks = get_tasks(user_id)

    if not tasks:
        query.edit_message_text(text="У вас нет текущих задач.")
        return
    
    task_buttons = [
        [InlineKeyboardButton(f"Завершить задачу {i+1}", callback_data=f'done_task_{i}'),
         InlineKeyboardButton(f"Удалить задачу {i+1}", callback_data=f'delete_task_{i}')]
        for i, task in enumerate(tasks)
    ]
    reply_markup = InlineKeyboardMarkup(task_buttons)
    query.edit_message_text(text="Ваши задачи:", reply_markup=reply_markup)

task_management_handler = [
    CallbackQueryHandler(add_task, pattern='^add_task$'),
    MessageHandler(Filters.text & ~Filters.command, handle_message),
    CallbackQueryHandler(list_tasks, pattern='^list_tasks$')
]