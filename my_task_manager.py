import sys
import os

# Constants for task file
TASKS_FILE = 'tasks.txt'

# Function to initialize the tasks file
def init_tasks_file():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as file:
            file.write("Welcome to My Task Manager!\n")
            file.write("=================================\n")
            file.write("Here are your tasks:\n\n")

# Function to add a task
def add_task(task):
    with open(TASKS_FILE, 'a') as file:
        file.write(f"- [ ] {task}\n")
    print(f'Task "{task}" added.')

# Function to list tasks
def list_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = file.readlines()
        if tasks:
            print("Your Tasks:")
            for i, task in enumerate(tasks[3:], start=1):  # Skip the first 3 lines
                print(f"{i}. {task.strip()}")
        else:
            print("No tasks found.")
    except FileNotFoundError:
        print("No tasks found.")

# Function to remove a task
def remove_task(task_number):
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = file.readlines()
        if tasks and 4 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number + 2)  # Adjust index to skip first 3 lines
            with open(TASKS_FILE, 'w') as file:
                file.writelines(tasks)
            print(f'Task "{removed_task.strip()}" removed.')
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks found.")

def main():
    init_tasks_file()

    if len(sys.argv) < 2:
        print("Usage: python my_task_manager.py [add/list/remove] [task/task_number]")
        return

    action = sys.argv[1]

    if action == 'add':
        if len(sys.argv) > 2:
            task = ' '.join(sys.argv[2:])
            add_task(task)
        else:
            print("Usage: python my_task_manager.py add [task]")
    elif action == 'list':
        list_tasks()
    elif action == 'remove':
        if len(sys.argv) == 3 and sys.argv[2].isdigit():
            task_number = int(sys.argv[2])
            remove_task(task_number)
        else:
            print("Usage: python my_task_manager.py remove [task_number]")
    else:
        print("Usage: python my_task_manager.py [add/list/remove] [task]")

if __name__ == "__main__":
    main()
