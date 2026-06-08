# Root level wrapper for task_manager.task_utils
# This allows imports from both root and package level
from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks

__all__ = ["add_task", "mark_task_as_complete", "view_pending_tasks", "calculate_progress", "tasks"]

