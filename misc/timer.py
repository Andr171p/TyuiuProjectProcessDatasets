import time

from loguru import logger


def run_timer(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        start_time = time.time()
        task = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Время выполнения задачи {func.__name__}: {end_time - start_time} секунд...")
        return task
    return wrapper