import os
filename = "poem.txt"
base_dir = os.path.dirname(filename)
file_path = os.path.join(base_dir, "./Files", filename)


def read():
    try:
        file = open(file_path, "r")
        for line in file:
            print(line, end="")
        file.close()
    except FileNotFoundError as error:
        print(error)


if __name__ == "__main__":
    read()
