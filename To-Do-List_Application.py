
tasks=[]

def add_task(task):
    tasks.append(task)
    print("Task Added Successfully")

def view_task():
    if not tasks:
        print("No Tasks found")
    else:
        print("Tasks:")
        for index,task in enumerate(tasks,start=1):
            print(f"{index}. {task}")
def mark_completed_task(index):
    if 1 <= index <= len(tasks):
        task=tasks[index - 1]
        if not task.startswith("[Completed]"):
            tasks[index - 1] = "[Completed] " + task
            print(f"Task '{task}' marked as completed.")
        else:
            print("Task is already marked as completed.")
    else:
        print("Invalid task index.")
def edit_task(index):
    if 1<=index<=len(tasks):
        new_task=input("Enter the new_task")
        tasks[index - 1] = new_task
        print(f"Task '{new_task}' edited Successfully.")
    else:
        print("Invalid")
def delete_task(index):
    if 1<=index<=len(tasks):
        task=tasks.pop(index-1)
        print(f"Task '{task}'is Deleted")
    else:
        print("Invalid")

while True:
    print("To-Do List Menu\n")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Completed Task")
    print("4. Edit Task")
    print("5. Delete Task")
    print("6. Quit")

    choice = input("Enter your Choice:")

    if choice=='1':
        task=input("Enter the task:")
        add_task(task)
    elif choice=='2':
        view_task()
    elif choice=='3':
        index=int(input("Enter the task number to mark as COMPLETED:"))
        mark_completed_task(index)
    elif choice=='4':
        index=int(input("Enter the task number to EDIT:"))
        edit_task(index)
    elif choice=='5':
        index=int(input("Enter the task number to DELETE: "))
        delete_task(index)
    elif choice=='6':
        print("Exiting Megha's To-Do List Application. GoodBye!")
        break
    else:
        print("Invalid")


