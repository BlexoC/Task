from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks

# Define the main function
def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                add_task(title, description, due_date)
            except ValueError as error:
                print(f"Error: {error}")
        elif choice == "2":
            if not tasks:
                print("No tasks available to mark as complete.")
                continue
            print("\nAll Tasks:")
            for index, task in enumerate(tasks, start=1):
                status = "Complete" if task["completed"] else "Pending"
                print(f"{index}. {task['title']} - {status}")
            try:
                selection = int(input("Enter the task number to mark complete: "))
                mark_task_as_complete(selection - 1)
            except ValueError:
                print("Please enter a valid number.")
            except IndexError as error:
                print(f"Error: {error}")
        elif choice == "3":
            view_pending_tasks()
        elif choice == "4":
            progress = calculate_progress()
            completed = sum(1 for task in tasks if task["completed"])
            total = len(tasks)
            print(f"\nProgress: {progress}% complete")
            print(f"Completed tasks: {completed} / {total}")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
