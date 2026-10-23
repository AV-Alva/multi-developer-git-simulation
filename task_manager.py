tasks = []

def add_task(task):
    if not task.strip():
        print("Task cannot be empty.")
        return

    tasks.append(task)
    print(f"Task added: {task}")

def display_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nTasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")