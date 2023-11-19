from datetime import datetime
from os import path

class Task:
    def __init__(self, title, description, due_date):
        # Initialize a task object
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False  # Initially set the task as not completed
    
    def mark_as_completed(self):
        self.completed = True  # Mark the task as completed
    
    def __str__(self):
        # Represent the task as a formatted string
        status = "Completed" if self.completed else "Not Completed"
        msg = f"Title: {self.title}\n"
        msg += f"Description: {self.description}\n"
        msg += f"Due Date: {self.due_date}\n"
        msg += f"Status: {status}\n"
        return msg


class TaskManager:
    def __init__(self):
        #Initialize a TaskManager object
        self.tasks = []  # Initialize an empty list of tasks
        self.filename = "tasks.txt"  # Name of the text file to store tasks
    
    def add_task(self, task):
        # Add a task to the list of tasks
        self.tasks.append(task)
        self.save_tasks_to_file()
    
    def view_tasks(self):
        # Display all tasks in the list
        print("\nCurrent Tasks:")
        print("--------------")
        for task in self.tasks:
            print(task)
    
    def save_tasks_to_file(self):
        # Save tasks to the text file
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                # Replace spaces in title and description with underscores for file format
                title = task.title.replace(" ", "_")
                description = task.description.replace(" ", "_")
                file.write(f"{title} {description} {task.due_date} {task.completed}\n")
    
    def load_tasks_from_file(self):
        # Load tasks from the text file
        if path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    # Extract task information from each line
                    title, description, due_date, completed = line.strip().split(' ', maxsplit = 4)
                    # Replace underscores with spaces in title and description
                    title = title.replace("_", " ")
                    description = description.replace("_", " ")
                    # Add the new task to the tasks list
                    new_task = Task(title, description, due_date)
                    new_task.completed = (completed == "True")
                    self.tasks.append(new_task)

def validate_date(date_string):
    # Validate if the date has the format YYYY-MM-DD
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def main():
    task_manager = TaskManager()
    task_manager.load_tasks_from_file()  # Load tasks from the file at the beginning
    
    while True:
        print("Task Manager Menu:")
        print("------------------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print("\nTask Details:")
            print("-------------")
			
            # Get user input for task details
            title = input("Enter task title: ")
            if not title:
                print("ERROR: Task title cannot be empty.\n")
                continue
            
            description = input("Enter task description: ")
            if not description:
                print("ERROR: Task description cannot be empty.\n")
                continue
            
            due_date = input("Enter due date (YYYY-MM-DD): ")
            if not validate_date(due_date):
                print("ERROR: Invalid date format. Please type in YYYY-MM-DD format.\n")
                continue

            # Create a new task and add it to the task manager
            new_task = Task(title, description, due_date)
            task_manager.add_task(new_task)
            print("Task added successfully!\n")
        
        elif choice == "2":
            # Display all tasks in the task manager
            task_manager.view_tasks()
        
        elif choice == "3":
            # Display all tasks in the task manager for reference
            task_manager.view_tasks()

            # Get user input for the title of the task to mark as completed
            task_title = input("Enter the title of the task to mark as completed: ")

            # Find the task with the specified title
            task_to_mark = None
            for task in task_manager.tasks:
                if task.title == task_title:
                    task_to_mark = task
                    break
            
            if task_to_mark:
                # Mark the found task as completed
                task_to_mark.mark_as_completed()
                print(f"Task marked as completed!\n")
                task_manager.save_tasks_to_file()  # Save tasks after marking as completed
            else:
                print("ERROR: Task not found. Please enter a valid task title.\n")
        
        elif choice == "4":
            print("Exiting Task Manager. Goodbye!")
            task_manager.save_tasks_to_file()  # Save tasks before exiting
            break
        
        else:
            print("ERROR: Invalid choice. Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    main()
