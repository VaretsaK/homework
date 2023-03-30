class FibonIt:
    def __init__(self, num):
        self.num = num
        self.first = 1
        self.second = 0

    def __iter__(self):
        return self

    def __next__(self):
        next_num = self.first + self.second
        if next_num >= self.num:
            raise StopIteration
        self.first, self.second = self.second, next_num
        return next_num


if __name__ == "__main__":
    fibonacci = FibonIt(20)

    for number in fibonacci:
        print(number)
