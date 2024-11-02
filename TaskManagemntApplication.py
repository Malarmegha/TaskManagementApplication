# Task Manager Application in Python

tasks = []

def add_task():
    task = input("Enter the task: ")
    due_date = input("Enter due date (optional): ")
    tasks.append({"task": task, "due_date": due_date})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks):
        due_date = task["due_date"] if task["due_date"] else "No due date"
        print(f"{idx + 1}. {task['task']} - Due: {due_date}")
    print()

def delete_task():
    view_tasks()
    if not tasks:
        return
    task_num = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
