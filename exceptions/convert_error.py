
def num_input():
    try:
        return int(float(input("Some num here: ")))
    except ValueError as error:
        return error


if __name__ == "__main__":
    print(num_input())
