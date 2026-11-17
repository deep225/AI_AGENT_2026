from datetime import datetime
import string
import secrets
def current_time():
    """Returns the current time as a string in the format 'YYYY-MM-DD HH:MM:SS'."""
    return datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')

def roll_dice():
    """Generates a random number between 1 and 6 (inclusive)."""
    import random
    return random.randint(1,6)

def generate_password(length=12):
    """Generates a random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for i in range(length))
