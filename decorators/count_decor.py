
def decor_count(func):
    counter = 0

    def simple(*args, **kwargs):
        nonlocal counter
        func(*args, **kwargs)
        counter += 1
        print(f"{counter} time(s) the function was called")
    return simple


@decor_count
def mult(a, b):
    print(f"{a} multiplied by {b} equals {a * b}")


@decor_count
def dev(a, b, c):
    print(f"{a} divided by {b} and divided by {c} equals {a / b / c}")


if __name__ == "__main__":
    mult(3, 6)
    mult(4, 6)
    mult(3, 3)
    print()
    dev(9, 3, 1)
    dev(5, 3, 1)
