#Task Tracker
# Task Tracker

def add_task(task_list, task, status):
    task_list.append({'task': task, 'status': status})

def print_tasks(task_list):
    for task in task_list:
        print(f'Task: {task["task"]}, Status: {task["status"]}')

def filter_by_status(task_list, status):
    return list(filter(lambda task: task['status'] == status, task_list))

def main():
    task_list = []
    while True:
        print('\nTask Tracker')
        print('1. Add a Task')
        print('2. List all Tasks')
        print('3. Filter tasks by status')
        print('4. Exit')

        choice = input("Enter your choice: ")

        if choice == '1':
            your_task = input("Enter your task: ")
            status = input("Enter the status: ")
            add_task(task_list, your_task, status)

        elif choice == '2':
            print("\nAll Tasks")
            print_tasks(task_list)

        elif choice == '3':
            status = input("Enter the status to filter by: ")
            filtered_list = filter_by_status(task_list, status)
            print("\nFiltered Tasks")
            print_tasks(filtered_list)

        elif choice == '4':
            print("Exiting the program")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
