def factorial(num):
    if num == 1:
        return num
    return factorial(num - 1) * num


if __name__ == "__main__":
    print(factorial(5))
