def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

        
        