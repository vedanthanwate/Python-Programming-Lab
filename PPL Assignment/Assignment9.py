# 1.class Employee
class Employee:
    def get_data(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")

    def display(self):
        print(self.name, self.age, self.salary, self.address)


class Manager(Employee):
    pass


managers = []

for i in range(2):   # change to 10 if needed
    print(f"\nEnter details of Manager {i+1}")
    m = Manager()
    m.get_data()
    managers.append(m)

print("\n--- Manager Details ---")
for m in managers:
    m.display()

# 2.Library Managment System
    class Book:
        def __init__(self, name):
            self.name = name
            self.available = True


    class Library:
        def __init__(self):
            self.books = []

        def add_book(self):
            name = input("Enter book name: ")
            self.books.append(Book(name))
            print("Book added")

        def show_books(self):
            for b in self.books:
                status = "Available" if b.available else "Not Available"
                print(b.name, "-", status)

        def lend_book(self):
            name = input("Enter book name: ")
            for b in self.books:
                if b.name == name and b.available:
                    b.available = False
                    print("Book issued")
                    return
            print("Book not available")

        def return_book(self):
            name = input("Enter book name: ")
            for b in self.books:
                if b.name == name:
                    b.available = True
                    print("Book returned")
                    return
            print("Book not found")


    lib = Library()

    while True:
        print("\n--- LIBRARY MENU ---")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Exit")

        ch = int(input("Enter choice: "))

        if ch == 5:
            break
        elif ch == 1:
            lib.add_book()
        elif ch == 2:
            lib.show_books()
        elif ch == 3:
            lib.lend_book()
        elif ch == 4:
            lib.return_book()
        else:
            print("Invalid choice")