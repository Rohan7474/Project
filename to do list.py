
tasks = []

def add_task(task):
    tasks.append({"task": task, "is_completed": False})
    print("Task added successfully!")

def view_tasks():
    if tasks:
        print("Tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "Completed" if task["is_completed"] else "Not Completed"
            print(f"{idx}. {task['task']} - {status}")
    else:
        print("No tasks found.")

def mark_as_completed(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["is_completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Main program
while True:
    print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Completed\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task description: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_number = int(input("Enter task number to mark as completed: "))
        mark_as_completed(task_number)
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.") 