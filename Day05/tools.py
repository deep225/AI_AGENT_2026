from datetime import datetime
import os
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

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    if "data" not in file_path:
        file_path = os.path.join("data", file_path)  # Prepend the "data" directory if not present
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"An error occurred while reading the file: {str(e)}"
