
def retry_maker(max_retries, exc):

    def retry(func):
        counter = 0

        def decor(*args, **kwargs):
            nonlocal counter
            while counter < max_retries:
                try:
                    return func(*args, **kwargs)
                except exc:
                    counter += 1
                    print(f"Mistake number {counter}")
                    return
            print(exc.__name__)
        return decor
    return retry


@retry_maker(2, ZeroDivisionError)
def mult(a, b):
    print(a / b)


if __name__ == "__main__":
    mult(15, 1)
    mult(15, 3)
    mult(15, 0)
    mult(15, 3)
    mult(15, 5)
    mult(15, 0)
    mult(15, 3)
