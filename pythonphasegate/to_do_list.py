


def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "status": "Pending"})
    print(" Task added successfully!")

def view_tasks():
    if not tasks:
        print(" No tasks available.")
    else:
        print("\n To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task['task']} - {task['status']}")

def mark_complete():
    view_tasks()
    try:
        task_no = int(input("\nEnter task number to mark as complete: "))
        tasks[task_no - 1]["status"] = "Completed"
        print(" Task marked as completed!")
    except:
        print(" Invalid task number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("\nEnter task number to delete: "))
        tasks.pop(task_no - 1)
        print(" Task deleted successfully!")
    except:
        print(" Invalid task number.")

def main():
    while True:
        print("\n To-Do List Manager ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print(" Goodbye! Keep being productive!")
            break
        else:
            print(" Invalid option. Try again!")

if __name__ == "__main__":
    main()

