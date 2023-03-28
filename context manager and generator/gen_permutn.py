from itertools import permutations


def permut_this(given_list):
    for p in permutations(given_list):
        yield p


if __name__ == "__main__":
    for i in permut_this([1, 2, 3]):
        print(i)
