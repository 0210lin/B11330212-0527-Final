import os
import json
from collections import Counter


class Library:
    def __init__(self, file_name="books.json"):
        self.file_name = file_name
        self.books = []

    def load_books(self):
        """Load books from the JSON file."""
        try:
            if os.path.exists(self.file_name):
                with open(self.file_name, "r", encoding="utf-8") as file:
                    self.books = json.load(file)
            else:
                self.books = []
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error: Failed to load books. The file may be corrupted or missing.")
            self.books = []

    def save_books(self):
        """Save books to the JSON file."""
        try:
            with open(self.file_name, "w", encoding="utf-8") as file:
                json.dump(self.books, file, ensure_ascii=False, indent=4)
        except IOError:
            print("Error: Failed to save books to file.")

    def add_book(self, title, isbn, status="available"):
        """Add a new book to the library."""
        if not self.is_isbn_exist(isbn):
            self.books.append({"title": title, "isbn": isbn, "status": status})
            print("Success")
        else:
            print("Error: ISBN already exists.")

    def is_isbn_exist(self, isbn):
        """Check if a book with the given ISBN exists."""
        return any(book["isbn"] == isbn for book in self.books)

    def show_books(self):
        """Display all books in the library."""
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                print(f"書名: {book['title']}, ISBN: {book['isbn']}, 狀態: {book['status']}")

    def borrow_book(self, isbn):
        """Borrow a book by updating its status."""
        for book in self.books:
            if book["isbn"] == isbn:
                if book["status"] == "available":
                    book["status"] = "borrowed"
                    print("Success")
                else:
                    print("Error: Book is already borrowed.")
                return
        print("Error: Book not found.")

    def print_status_summary(self):
        """Print a summary of book statuses."""
        status_count = Counter(book["status"] for book in self.books)
        for status, count in status_count.items():
            print(f"{status}: {count}")


def main():
    library = Library()
    library.load_books()
    print("=== 圖書管理系統 v1.0 ===")

    while True:
        command = input("> ").strip()

        if command == "exit":
            library.save_books()
            library.print_status_summary()
            print("系統關閉")
            break

        elif command.startswith("add "):
            try:
                _, raw_data = command.split(" ", 1)
                title, isbn, status = raw_data.split("/")
                library.add_book(title, isbn, status)
            except ValueError:
                print("Error: Invalid format. Use 'add 書名/ISBN/狀態'.")

        elif command == "show":
            library.show_books()

        elif command.startswith("borrow "):
            isbn = command[7:]
            library.borrow_book(isbn)

        else:
            print("Error: Unknown command.")


if __name__ == "__main__":
    main()