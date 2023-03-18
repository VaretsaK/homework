class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.pages < other.pages


if __name__ == "__main__":
    book1 = Book("Moby-Dick", "Herman Melville", 338)
    book2 = Book("The Old Man and the Sea", "Ernest Miller Hemingway", 197)
    book3 = Book("Moby-Dick", "Herman Melville", 378)
    book4 = Book("A Moveable Feast", "Ernest Miller Hemingway", 232)
    book5 = Book("To Kill a Mockingbird", "Harper Lee", 366)

    all_books = [book1, book2, book3, book4, book5]

    print("Printing all objects:")
    for b in all_books:
        print(b)

    print("\nPrinting books' length:")
    for b in all_books:
        print(f"{b.title} has {len(b)} pages ")

    print("\nComparing books:")
    print(book1 == book3)

    print("\nPrinting sorted books:")
    for i in sorted(all_books):
        print(i)

    print("\nLooking for a specific book in all books we have:")
    for i in all_books:
        if "Moby-Dick" in i.title:
            print(i)

    print("\nBook with maximum pages: ", max(all_books))
    print("\nBook with minimum pages: ", min(all_books))
