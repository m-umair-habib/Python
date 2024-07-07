print("DEVELOPED_BY:")
print("\t     Muhammad Umair Habib")
print(" ")
print(" ")
print('Problem: Same some tasks as a reminder and after performing, update your file.')
print(" ")
print(" ")

def getting_task():
    tasks = []
    while True:
        user_entry = input('Enter Your Tasks OR write "done" to finish: ')
        if user_entry.lower() == 'done':
            break
        else:
            tasks.append(user_entry)
    with open('task.txt', 'w') as f:
        for task in tasks:
            f.write(task + '\n')
    print("Tasks have been saved in task.txt")

def show_task():
    with open('task.txt', 'r') as r:
        for index, line in enumerate(r, start=1):
            print(f"{index}: {line.strip()}")

def rem_task():
    with open('task.txt', 'r') as read:
        tasks = read.readlines()

    print("Remember !!! (Indexed Number always starts from 1)")
    try:
        user_input = int(input("Enter the index number of the task to remove: "))
        if 1 <= user_input <= len(tasks):
            del tasks[user_input - 1]
            with open('task.txt', 'w') as f:
                f.writelines(tasks)
            print("Task removed successfully.")
            show_task()  
        else:
            print("Invalid index number.")
    except ValueError:
        print("Please enter a valid integer index.")

getting_task()
show_task()
rem_task()
