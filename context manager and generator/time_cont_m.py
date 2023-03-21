from time import time
from contextlib import contextmanager


# first way of creating time context manager
@contextmanager
def time_con_m():
    start = time()
    try:
        yield
    except Exception as e:
        # if there is an error - printing message and rising an error
        print("Something went wrong!")
        raise e
    # if there is no errors - printing message with execution time of the code
    end = time()
    print(f"Success! It took only {end - start} sec")


# second way of creating time context manager
class TimeContMan:
    def __init__(self):
        pass

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # if there is an error - printing some message and in the end of the block an error will be raised
        if exc_type:
            print("Something went wrong!")
        # if there is no errors - printing message with execution time of the code
        else:
            self.end = time()
            print(f"Success! It took only {self.end - self.start} sec")


if __name__ == "__main__":
    with time_con_m() as t:
        print(5 / 40)
    with TimeContMan() as t2:
        print(5 / 8)
