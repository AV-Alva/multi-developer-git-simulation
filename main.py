from task_manager import display_tasks, add_task


def main():
    print("=== Task Manager ===")

    add_task("Learn Git branching")
    add_task("Create Pull Request")
    add_task("Review code")
    display_tasks()


if __name__ == "__main__":
    main()