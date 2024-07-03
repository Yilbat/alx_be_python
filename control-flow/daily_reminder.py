Task = input("Enter  your Task ")
priority = input("(high/medium/low) ")
time_bound = input("Is it time-bound? (yes/no) ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{Task}' is a high priority Task that requires immediate attention today!")
        else:
            print(f"Reminder: '{Task}' is a high priority Task that requires immediate attention! ")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{Task}' is a medium priority Task that requires attention today!")
        else:
            print(f"Reminder: '{Task}' is a medium priority Task that requires attention! ")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{Task}' is a low priority Task. Consider completing it at the appropriate time")
        else:
            print(f"Note: '{Task}' is a low priority Task. Consider completing it when you have free time.")
