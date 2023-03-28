class VowelIt:
    def __init__(self, seq):
        self.seq = seq
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index == len(self.seq):
                raise StopIteration
            letter = self.seq[self.index]
            self.index += 1
            if letter in "aeiou":
                return letter


if __name__ == "__main__":
    word = "hello world"
    vowels = VowelIt(word)

    for vowel in vowels:
        print(vowel)
