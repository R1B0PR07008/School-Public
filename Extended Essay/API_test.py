from datetime import datetime

# Define the target date (January 1, 2020)
target_date = datetime(2020, 1, 1)

# Get the current date and time
current_date = datetime.now()

# Calculate the difference in days
days_difference = (current_date - target_date).days

# Print the result
print(f"The number of days between now and 2020 is: {days_difference} days.")