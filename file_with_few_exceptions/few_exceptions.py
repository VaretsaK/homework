
def read_n_write(our_file):
    num = input("Choose a number: ")
    divisor = input("Type in a divisor: ")
    our_file.write(divisor)
    our_file.seek(0)
    try:
        print(int(num) / int(our_file.read()))
    except ValueError as e:
        print(e)
    finally:
        our_file.close()
        print("The end.")


if __name__ == "__main__":
    try:
        file = open("divisor.txt", "r+")
        read_n_write(file)
    except (FileNotFoundError, PermissionError) as errors:
        print(errors)
