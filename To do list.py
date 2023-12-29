# Simple To-Do List

def display_menu():
    print("\n====== To-Do List Menu ======")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_todo_list(todo_list):
    print("\n===== Your To-Do List =====")
    if not todo_list:
        print("No tasks found.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(todo_list, new_task):
    todo_list.append(new_task)
    print(f"Task '{new_task}' added successfully.")

def mark_completed(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        completed_task = todo_list.pop(task_index - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task index.")

def delete_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        deleted_task = todo_list.pop(task_index - 1)
        print(f"Task '{deleted_task}' deleted successfully.")
    else:
        print("Invalid task index.")

def save_to_file(file_path, todo_list):
    with open(file_path, 'w') as file:
        for task in todo_list:
            file.write(task + '\n')

def load_from_file(file_path):
    todo_list = []
    try:
        with open(file_path, 'r') as file:
            todo_list = [line.strip() for line in file]
    except FileNotFoundError:
        pass
    return todo_list

def main():
    todo_list = load_from_file("todo_list.txt")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            new_task = input("Enter the new task: ")
            add_task(todo_list, new_task)
        elif choice == '3':
            view_todo_list(todo_list)
            task_index = int(input("Enter the task index to mark as completed: "))
            mark_completed(todo_list, task_index)
        elif choice == '4':
            view_todo_list(todo_list)
            task_index = int(input("Enter the task index to delete: "))
            delete_task(todo_list, task_index)
        elif choice == '5':
            save_to_file("todo_list.txt", todo_list)
            print("Exiting the To-Do List application. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
