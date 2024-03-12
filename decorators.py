import logging

logger = logging.getLogger("my_logger")
file_handler = logging.FileHandler('logs.txt')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def try_except_decorator(error_message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                logger.error(f"{error_message} exception:{e}")
                return None
        return wrapper
    return decorator