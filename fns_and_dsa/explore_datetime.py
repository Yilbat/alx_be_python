from datetime import datetime, timedelta


def display_current_datetime():
  """
  Gets the current date and time and prints it in a readable format.
  """
  current_date = datetime.now()
  formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {formatted_date}")


def calculate_future_date(days):
  """
  Calculates a future date by adding a specified number of days to the current date.

  Args:
      days: The number of days to add (integer).

  Returns:
      A datetime object representing the future date.
  """
  current_date = datetime.now()
  future_date = current_date + timedelta(days=days)
  formatted_future_date = future_date.strftime("%Y-%m-%d")
  print(f"Future date: {formatted_future_date}")


if __name__ == "__main__":
  display_current_datetime()
  num_days = int(input("Enter the number of days to add to the current date: "))
  calculate_future_date(num_days)
