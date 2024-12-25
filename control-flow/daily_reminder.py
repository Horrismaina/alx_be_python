def create_reminder():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            message = f"'{task}' is a task"

    if time_bound.lower() == "yes":
        print(f"\nReminder: {message} that requires immediate attention today!")
    else:
        print(f"\nNote: {message}. Consider completing it when you have free time.")

if __name__ == "__main__":
    create_reminder()