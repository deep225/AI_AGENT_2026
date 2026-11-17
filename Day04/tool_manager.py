from tools import current_time, roll_dice, generate_password

def execute_tool(user_input):
    """Executes the specified tool and returns the result."""
    text = user_input.lower()
    if "time" in text or "clock" in text:
        return current_time()
    if "dice" in text:
        return f"Rolling dice: {roll_dice()}"
    if "password" in text:
        return f"Generated password: {generate_password(12)}"
    return None  # Return None if no tool matches the input