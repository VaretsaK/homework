
def write():
    file = open("divisor.txt", "w")
    divisor = input("Type in a divisor: ")
    file.write(divisor)
    file.close()


def read():
    file_name = input("What file do you want to open: ")
    try:
        file = open(f"{file_name}.txt", "r")
        try:
            print(num / int(file.read()))
            change_divisor = input("Do you want to change the divisor: ")
            if change_divisor == "yes":
                file.write(input("Type in a divisor: "))
        except (PermissionError, ValueError) as errors:
            print(errors)
        finally:
            file.close()
    except FileNotFoundError as error:
        print(error)
    finally:
        print("The end.")


if __name__ == "__main__":
    try:
        num = int(input("Choose a number: "))
    except ValueError:
        num = 100
    write()
    read()
