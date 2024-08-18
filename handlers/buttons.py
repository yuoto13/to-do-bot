from telegram.ext import CallbackQueryHandler
from utils.database import complete_task, delete_task

def button(update, context):
    query = update.callback_query
    user_id = query.from_user.id
    data = query.data

    if data.startswith('done_task_'):
        task_index = int(data.split('_')[2])
        complete_task(user_id, task_index)
        query.answer('Задача завершена!')
    elif data.startswith('delete_task_'):
        task_index = int(data.split('_')[2])
        delete_task(user_id, task_index)
        query.answer('Задача удалена!')

    # Возвращаемся к списку задач
    from .task_management import list_tasks
    list_tasks(update, context)

button_handler = CallbackQueryHandler(button, pattern='^done_task_.*|delete_task_.*')
