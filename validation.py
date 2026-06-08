from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str):
        return False
    title = title.strip()
    return bool(title) and len(title) <= 100
    
def validate_task_description(description):
    if not isinstance(description, str):
        return False
    description = description.strip()
    return bool(description) and len(description) <= 250
    
def validate_due_date(due_date):
    if not isinstance(due_date, str):
        return False
    try:
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
        today = datetime.now().date()
        return due_date_obj >= today
    except ValueError:
        return False