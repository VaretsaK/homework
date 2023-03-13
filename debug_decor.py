
def debug_maker(print_input, print_output):

    def debug(func):

        def simple(*args, **kwargs):
            if print_input:
                print(f"Input: {(tuple(args) + tuple(kwargs.keys()))}")
            if print_output:
                func(*args, **kwargs)
        return simple
    return debug


@debug_maker(print_input=True, print_output=True)
def mult(a, b):
    print(a * b)


if __name__ == "__main__":
    mult(5, 6)
