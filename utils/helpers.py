# helpers.py

from datetime import datetime

def format_date(date: datetime) -> str:
    """
    Форматирует объект datetime в строку формата 'ДД.ММ.ГГГГ ЧЧ:ММ'.
    """
    return date.strftime('%d.%m.%Y %H:%M')

def parse_date(date_str: str) -> datetime:
    """
    Парсит строку даты в объект datetime.
    Ожидаемый формат строки: 'ДД.ММ.ГГГГ ЧЧ:ММ'.
    """
    try:
        return datetime.strptime(date_str, '%d.%m.%Y %H:%M')
    except ValueError:
        raise ValueError("Неверный формат даты. Ожидается: ДД.ММ.ГГГГ ЧЧ:ММ")

def validate_reminder_time(reminder_time: int):
    """
    Проверяет, что время напоминания является положительным числом.
    """
    if reminder_time <= 0:
        raise ValueError("Время напоминания должно быть положительным числом.")

def human_readable_priority(priority: str) -> str:
    """
    Возвращает более читабельное представление приоритета задачи.
    """
    priorities = {
        'high': 'Высокий',
        'medium': 'Средний',
        'low': 'Низкий'
    }
    return priorities.get(priority, 'Неизвестный приоритет')