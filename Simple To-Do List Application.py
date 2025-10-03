def add_task():
    to_add = input('What do you want to add?')
    global user_task
    user_task = []
    user_task.append(to_add)
    print('\n')
    
def view_task():
    for i in user_task:
        print(f'{i}/n')

def delete_task():
    print('Which one do you want to remove?\n')
    to_delete = int(input())
    user_task.remove(to_delete)


print('WELCOME to my program.\nWhat do you want to do?')
while True:
    options = ['\n1. Add Task', '2. View Task', '3. Delete Task', '4. Exit\n']
    for option in options:
        print(option)
    task = (input())
    if task == '4' :
        print('OK!')
        break
    else: 
        if task == '1':
            add_task()   
        elif task == '2':
            view_task()
        elif task == '3':
            delete_task()
        else:
            raise ValueError