class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added")

    def remove_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
            print(f"Task {task_number} removed")
        except IndexError:
            print("Task not found")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def run(self):
        while True:
            print("\n1. Add task")
            print("2. Remove task")
            print("3. List tasks")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                task = input("Enter a task: ")
                self.add_task(task)
            elif choice == "2":
                self.list_tasks()
                task_number = int(input("Enter task number to remove: "))
                self.remove_task(task_number)
            elif choice == "3":
                self.list_tasks()
            elif choice == "4":
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    app = TodoApp()
    app.run()