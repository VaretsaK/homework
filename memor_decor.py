
def mem_decor(func):
    result = {}

    def memorize_this(*args, **kwargs):
        keys = (tuple(args) + tuple(kwargs.keys()))
        if keys in result:
            return result[keys]
        else:
            result[keys] = func(*args, **kwargs)
        return result[keys]

    return memorize_this


@mem_decor
def multi(a, b):
    return a * b


if __name__ == "__main__":
    print(multi(5, 6))
    print(multi(5, 8))
    print(multi(5, 6))
    print(multi(5, 6))
