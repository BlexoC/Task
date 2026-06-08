from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks

# Expose task_manager.task_utils functions through the root module
__all__ = ["add_task", "mark_task_as_complete", "view_pending_tasks", "calculate_progress", "tasks"]
