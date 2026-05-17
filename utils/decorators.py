from datetime import datetime


def log_action(func):

    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Action executed: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper