class Library:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(self.filename, "a+") as f:
                pass  # Create the file if it doesn't exist
        except IOError as e:
            print(f"Error opening file: {e}")

    def __del__(self):
        try:
            with open(self.filename, "r") as f:
                pass  # Ensure file is open for proper closing
        except IOError:
            pass  # Handle potential errors gracefully

    def list_books(self):
        try:
            with open(self.filename, "r") as f:
                books = f.readlines()
            for book in books:
                info = book.strip().split(",")
                print(f"Title: {info[0]}, Author: {info[1]}")
        except IOError as e:
            print(f"Error reading file: {e}")

    def add_book(self):
        while True:
            try:
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                release_year = int(input("Enter release year: "))
                num_pages = int(input("Enter number of pages: "))
                break
            except ValueError as e:
                print(f"Invalid input: {e}")

        book_info = f"{title},{author},{release_year},{num_pages}"
        try:
            with open(self.filename, "a") as f:
                f.write(book_info + "\n")
            print("Book added successfully!")
        except IOError as e:
            print(f"Error writing to file: {e}")

    def remove_book(self):
        title = input("Enter title of book to remove: ")
        try:
            with open(self.filename, "r") as f:
                books = f.readlines()
            new_books = []
            for book in books:
                info = book.strip().split(",")
                if info[0] != title:
                    new_books.append(book)
            with open(self.filename, "w") as f:
                f.writelines(new_books)
            print("Book removed successfully!")
        except IOError as e:
            print(f"Error reading or writing to file: {e}")

if __name__ == "__main__":
    lib = Library("books.txt")  # Replace with your desired filename

    while True:
        print("\n*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")
