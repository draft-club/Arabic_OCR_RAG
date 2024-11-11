import functools
import logging

def task_logger(func):
    """Decorator for logging task execution details and handling exceptions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        task_name = func.__name__
        try:
            logging.info(f"Starting task: {task_name}")
            result = func(*args, **kwargs)
            logging.info(f"Finished task: {task_name}")
            return result
        except Exception as e:
            logging.error(f"Error in task {task_name}: {str(e)}")
            raise e
    return wrapper
