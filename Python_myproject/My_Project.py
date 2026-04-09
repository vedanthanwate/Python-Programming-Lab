class Library:
    def __init__(self):
        self.books = {}  # Hash Table (Dictionary)

    def insert_book(self, isbn, title, author, year):
        self.books[isbn] = {
            "Title": title,
            "Author": author,
            "Year": year
        }
        print("Book inserted successfully!\n")

    def search_book(self, isbn):
        if isbn in self.books:
            print("\n📖 Book Found:")
            for key, value in self.books[isbn].items():
                print(f"{key}: {value}")
        else:
            print("❌ Book not found!")
        print()

    def delete_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print("🗑️ Book deleted successfully!\n")
        else:
            print("❌ Book not found!\n")

    def display_books(self):
        if not self.books:
            print("📭 Library is empty!\n")
        else:
            print("\n📚 All Books:")
            for isbn, details in self.books.items():
                print(f"\nISBN: {isbn}")
                for key, value in details.items():
                    print(f"{key}: {value}")
            print()


def main():
    library = Library()

    while True:
        print("===== Library Menu =====")
        print("1. Insert Book")
        print("2. Search Book")
        print("3. Delete Book")
        print("4. Display Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            year = input("Enter Year: ")
            library.insert_book(isbn, title, author, year)

        elif choice == '2':
            isbn = input("Enter ISBN to search: ")
            library.search_book(isbn)

        elif choice == '3':
            isbn = input("Enter ISBN to delete: ")
            library.delete_book(isbn)

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            print("👋 Exiting program...")
            break

        else:
            print("❌ Invalid choice!\n")


if __name__ == "__main__":
    main()