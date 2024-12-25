def get_priority_message(task, priority):
    match priority:
        case "high":
            return f"Reminder: '{task}' is a high priority task"
        case "medium":
            return f"Reminder: '{task}' is a medium priority task"
        case "low":
            return f"Note: '{task}' is a low priority task"
        case _:
            return f"Note: '{task}' is a task"

def create_reminder():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    base_message = get_priority_message(task, priority)
    
    if time_bound.lower() == "yes":
        print(f"\n{base_message} that requires immediate attention today!")
    else:
        print(f"\n{base_message}. Consider completing it when you have free time.")

if __name__ == "__main__":
    create_reminder()