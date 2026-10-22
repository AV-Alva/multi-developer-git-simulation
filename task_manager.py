tasks = []


def display_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nTasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")