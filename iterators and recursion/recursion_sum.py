def recur_sum(num):
    number = str(num)
    if len(number) == 1:
        return num
    return int(number[-1]) + recur_sum(int(number[0:-1]))


if __name__ == "__main__":
    print(recur_sum(12345))
