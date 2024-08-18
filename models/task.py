from datetime import datetime

class Task:
    def __init__(self, description, priority=None, deadline=None, reminder=None):
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.reminder = reminder
        self.completed = False

    def set_priority(self, priority):
        self.priority = priority

    def set_deadline(self, deadline_str):
        try:
            self.deadline = datetime.strptime(deadline_str, '%d.%m.%Y %H:%M')
        except ValueError:
            raise ValueError("Неверный формат даты. Ожидается: ДД.ММ.ГГГГ ЧЧ:ММ")

    def set_reminder(self, reminder_time):
        self.reminder = reminder_time
