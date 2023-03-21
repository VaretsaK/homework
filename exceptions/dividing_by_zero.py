
def dividing(a, b):
    try:
        return a / b
    except ZeroDivisionError as error:
        return error


if __name__ == "__main__":
    number = int(input("Enter your number: "))
    divisor = int(input("Enter your divisor: "))
    print(dividing(number, divisor))
