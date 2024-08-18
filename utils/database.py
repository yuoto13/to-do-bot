tasks_dict = {}

def add_task(user_id, task):
    if user_id not in tasks_dict:
        tasks_dict[user_id] = []
    tasks_dict[user_id].append(task)

def get_tasks(user_id):
    return tasks_dict.get(user_id, [])

def delete_task(user_id, task_index):
    if user_id in tasks_dict and len(tasks_dict[user_id]) > task_index:
        del tasks_dict[user_id][task_index]

def complete_task(user_id, task_index):
    if user_id in tasks_dict and len(tasks_dict[user_id]) > task_index:
        tasks_dict[user_id][task_index].completed = True
