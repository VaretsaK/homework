
def num_input():
    try:
        number = float(input("Some num here: "))
    except ValueError as error:
        return error
    return int(number)


if __name__ == "__main__":
    print(num_input())
