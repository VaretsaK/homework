
def view():
    todo_list = open("to_do.txt", "r")
    todo_list.seek(0)
    for task in todo_list:
        print(task, end="")
    todo_list.close()


def add():
    todo_list = open("to_do.txt", "a+")
    todo_list.write(input("Your task here: "))
    todo_list.write("\n")
    todo_list.close()


if __name__ == "__main__":
    while True:
        menu = input("Choose action (Add, View, Quit): ").lower()
        try:
            if menu[0] == "a":
                add()
            elif menu[0] == "v":
                view()
            elif menu[0] == "q":
                break
            else:
                print("Wrong command!")
        except IndexError as e:
            print(e)
