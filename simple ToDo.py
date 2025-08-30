

tasks = []  

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")


while True:
    print("\n1. Add new task")
    print("2. Show all tasks")
    print("3. Exit")
    
    choice = input("Choose (1/2/3): ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    


