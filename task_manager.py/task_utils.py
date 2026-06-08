from datetime import datetime

# Import validation functions
None

# Define tasks list
tasks = []


# Implement add_task function
def add_task(title, description, due_date):
    new_task = {"title":title, "description":description, "due_date":due_date, "completed":False }
    tasks.append(new_task)
    print("Task added successfully!")


# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index <= tasks(len):
        print ("Invalid syntax")
    tasks[index]["completed"] = True
    print("Task marked as complete!")


# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    if mark_task_as_complete == False:
        print(tasks)


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) < completed:
        print("No tasks Yet")

    completed =0
    for task in tasks:
        if tasks["completed"] == True:
            completed += 1
    progress = (completed / tasks) * 100
    
    return progress
