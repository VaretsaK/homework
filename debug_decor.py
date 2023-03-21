
def debug_maker(print_output):

    def debug(func):
        res = []
        count = 0

        def simple(*args, **kwargs):
            nonlocal res, count
            res.append(func(*args, **kwargs))
            print(f"Input: {(tuple(args) + tuple(kwargs.keys()))}")
            if print_output:
                print(res[count])
            count += 1
        # Ти повинен виконувати функцію у будь-якому випадку, просто ти
        # повинен записувати результат окремо і виводити лише якщо print_output вказано
        return simple
    return debug


@debug_maker(print_output=True)
def mult(a, b):
    return a * b


if __name__ == "__main__":
    mult(5, 6)
    mult(5, 3)
    mult(25, 6)
