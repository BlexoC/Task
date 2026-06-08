
from datetime import datetime
def validate_task_title(title):
    if not title:
        raise ValueError("Task title cannot be empty.")
def validate_task_description(description):
    if not description:
        raise ValueError("Task description cannot be empty.")
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")