from datetime import datetime

# Import validation functions
from .validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    title = title.strip()
    description = description.strip()
    due_date = due_date.strip()

    if not validate_task_title(title):
        raise ValueError("Task title must be a non-empty string up to 100 characters.")
    if not validate_task_description(description):
        raise ValueError("Task description must be a non-empty string up to 250 characters.")

    if not validate_due_date(due_date):
        raise ValueError("Due date must be a valid date in YYYY-MM-DD format and not in the past.")

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
        "created_at": datetime.now().isoformat(),
    }
    tasks.append(task)
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if not tasks:
        raise IndexError("There are no tasks to update.")
    if index < 0 or index >= len(tasks):
        raise IndexError("Task number is out of range.")
    tasks[index]["completed"] = True
    print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = [task for task in tasks if not task["completed"]]
    if not pending:
        print("\nNo pending tasks.")
        return
    print("\nPending Tasks:")
    for index, task in enumerate(pending, start=1):
        print(f"{index}. {task['title']} (Due: {task['due_date']})")
        print(f"   Description: {task['description']}")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0.0
    completed_count = sum(1 for task in tasks if task["completed"])
    progress = (completed_count / len(tasks)) * 100
    return progress