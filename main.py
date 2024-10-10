# SIMPLE TO DO LIST APPLICATION BY VISHALL 

# Define a list to store the tasks 
tasks = []

# Function to display the menu
def display_menu():
    print("\nTask Manager By Vishall:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Function to view all tasks
def view_tasks():
    if not tasks: #Helps to check if the list is evaluated as false or true. In python, if the list[] is empty, it is considered as False in boolean context. 
        print("Your task list is empty.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1): #emmurate code is a build python function that helps you loop through a list while keeping track of the index of each item 
            print(f"{index}. {task}")

# Function to add a task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

# Function to remove a task
def remove_task():
    view_tasks()
    if tasks:
        try: #helps to catch any errors that might occur when user is asked to enter an input. 
            task_num = int(input("Enter the number of the task to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main program loop
while True:
    display_menu()
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting Task Manager application. Goodbye! by Vishall ")
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 4.")
