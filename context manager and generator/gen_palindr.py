def palindrom(n):
    for num in range(1, n + 1):
        if str(num) == str(num)[::-1]:
            yield num


if __name__ == "__main__":
    for res in palindrom(222):
        print(res)
