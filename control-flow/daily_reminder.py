
Task = input("Enter  your Task ")
Priority = input("(high/medium/low) ").lower()
Time_bound = input("Is it time-bound? (yes/no) ").lower()

match Priority:
    case "high":
        if Time_bound == "yes":
            print(f"Reminder: '{Task}' is a high Priority Task that requires immediate attention today!")
        else:
            print(f"Reminder: '{Task}' is a high Priority Task that requires immediate attention! ")

    case "medium":
        if Time_bound == "yes":
            print(f"Reminder: '{Task}' is a medium Priority Task that requires attention today!")
        else:
            print(f"Reminder: '{Task}' is a medium Priority Task that requires attention! ")
    case "low":
        if Time_bound == "yes":
            print(f"Note: '{Task}' is a low Priority Task. Consider completing it at the appropriate time")
        else:
            print(f"Note: '{Task}' is a low Priority Task. Consider completing it when you have free time.")
