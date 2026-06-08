from datetime import datetime

def validate_task_title(title):
    if not title:
         raise ValueError ("Should be a string")
    if len(title) < 3:
        raise ValueError("Should be longer than 3 words")

    
def validate_task_description(description):
    if not description:
        raise ValueError ("Should be a string")    
    
def validate_due_date(due_date):
    if due_date is not ("^\{4}-\{3}-\{3}$"):    
        raise ValueError ("SHould be YYY-MM-DY")