
def retry_maker(max_retries, exc):

    def retry(func):
        counter = 0

        def decor(*args, **kwargs):
            nonlocal counter
            while counter < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    counter += 1
                    return f"{error} - Mistake number {counter}"
            raise exc
        return decor
    return retry


@retry_maker(3, ZeroDivisionError)
def mult(a, b):
    return a / b


if __name__ == "__main__":
    print(mult(15, 1))
    print(mult(15, 3))
    print(mult(15, 0))
    print(mult(15, 0))
    print(mult(15, 5))
    print(mult(15, 0))
    print(mult(15, 3))
