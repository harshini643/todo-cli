tasks = []

def show_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

show_menu()
def view_tasks():
    for i, task in enumerate(tasks, 1):
        print(i, task)

