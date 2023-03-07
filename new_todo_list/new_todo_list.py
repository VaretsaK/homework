
def read(tasks):
    todo = open("to_do.txt", "r")
    todo.seek(0)
    for task in todo:
        tasks.append(task[:-1])
    todo.close()


def write(tasks):
    todo = open("to_do.txt", "w")
    for item in tasks:
        todo.write(f"{item}\n")
    todo.close()


def view(tasks):
    for item in range(len(tasks)):
        print(f"{item + 1}. {tasks[item]}")


def add(tasks):
    new = input(">>> ")
    tasks.append(new)


def edit(tasks):
    view(todo_list)
    try:
        num = int(input("What task do you want to mark as DONE? Enter a number: "))
        tasks[num - 1] = f"\033[9m{tasks[num - 1]}\033[0m"
    except ValueError as ex:
        print(ex)


if __name__ == "__main__":
    todo_list = []
    read(todo_list)
    while True:
        menu = input("Choose action (Add, Edit, View, Quit): ").lower()
        try:
            if menu[0] == "a":
                add(todo_list)
            elif menu[0] == "e":
                edit(todo_list)
            elif menu[0] == "v":
                view(todo_list)
            elif menu[0] == "q":
                write(todo_list)
                break
            else:
                print("Wrong command!")
        except IndexError as e:
            print(e)
