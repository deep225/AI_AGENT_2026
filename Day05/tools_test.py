from tools import current_time, read_file, roll_dice, generate_password

print("Current Time:", current_time())
print("Roll Dice:", roll_dice())
print("Generated Password:", generate_password(12))
print("Read File:", read_file("data/notes.txt"))  # Example usage of the new read_file function