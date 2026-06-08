from task_utils import add_task, mark_task_as_complete, view_pending_tasks,calculate_progress, tasks


# Define the main function3
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_task(title,description, due_date)
            title = input("Enter Title")
            description = input("Enter Description")
            due_date = input ("Enter the Due Date")
        elif choice == "2":
            mark_task_as_complete()
            view_pending_tasks()
            index = input ("Enter the index")
            try:
                mark_task_as_complete(int(index)-1)
            except ValueError:
                
        elif choice == "3":
            view_pending_tasks


        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
