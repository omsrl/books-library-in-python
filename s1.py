class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        for book in books:
            book_info = book.strip().split(",")
            print(f"Book: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = [book for book in books if title not in book]
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(updated_books)
        print("Book removed successfully.")
lib = Library()
print("*** MENU ***")
print("1) List Books")
print("2) Add Book")
print("3) Remove Book")

menu_choice = input("Enter your choice: ")

if menu_choice == "1":
    lib.list_books()
elif menu_choice == "2":
    lib.add_book()
elif menu_choice == "3":
    lib.remove_book()
else:
    print("Invalid choice.")
