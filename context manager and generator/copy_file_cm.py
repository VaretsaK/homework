import os


class TimeContMan:
    # list for a content
    file_content = []

    def __init__(self, file_to_copy, file_to_paste):
        # initializing our files
        self.file_to_copy = file_to_copy
        self.file_to_paste = file_to_paste

    def __enter__(self):
        # opening all files
        self.file1 = open(self.file_to_copy, "r+")
        self.file2 = open(self.file_to_paste, "w")
        # saving data form 1st file to our list
        for i in self.file1:
            self.file_content.append(i)
        # returning 1st file to work with it
        return self.file1

    def __exit__(self, exc_type, exc_val, exc_tb):
        # closing 1st file
        self.file1.close()
        # copying all data we had in the 1st file at the enter point
        for i in self.file_content:
            self.file2.write(i)
        # closing 2nd file
        self.file2.close()


if __name__ == "__main__":
    # files path part
    file1 = "copy_from.txt"
    file2 = "copy_to.txt"
    base_dir1 = os.path.dirname(file1)
    file_path1 = os.path.join(base_dir1, "../Files", file1)
    base_dir2 = os.path.dirname(file2)
    file_path2 = os.path.join(base_dir2, "../Files", file2)

    with TimeContMan(file_path1, file_path2) as cont:
        print(f"We have copied everything from a copy_from file into copy_to file.")
        # appending some text to our file
        cont.write("\n")
        cont.write(input("And now you can add something to the file copy_from: "))
