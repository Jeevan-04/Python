class LibraryItem:
    def __init__(self, title, item_id, quantity):
        self.title = title
        self.item_id = item_id
        self.checked_out = False
        self.quantity = quantity

    def display_info(self):
        print(f"Item ID: {self.item_id}")
        print(f"Title: {self.title}")
        print("Status: Checked out" if self.checked_out else "Status: Available")
        print(f"Quantity Available: {self.quantity}")

    def check_out(self):
        if not self.checked_out and self.quantity > 0:
            print(f"{self.title} has been checked out.")
            self.checked_out = True
            self.quantity -= 1
        elif self.checked_out:
            print(f"{self.title} is already checked out.")
        else:
            print(f"Sorry, {self.title} is not available at the moment.")

    def check_in(self):
        if self.checked_out:
            print(f"{self.title} has been checked in.")
            self.checked_out = False
            self.quantity += 1
        else:
            print(f"{self.title} is not checked out.")


class Book(LibraryItem):
    def __init__(self, title, item_id, author, genre, quantity):
        super().__init__(title, item_id, quantity)
        self.author = author
        self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")


class DVD(LibraryItem):
    def __init__(self, title, item_id, director, runtime, quantity):
        super().__init__(title, item_id, quantity)
        self.director = director
        self.runtime = runtime

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}")
        print(f"Runtime: {self.runtime} minutes")


class Journal(LibraryItem):
    def __init__(self, title, item_id, issue_number, editor, quantity):
        super().__init__(title, item_id, quantity)
        self.issue_number = issue_number
        self.editor = editor

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")
        print(f"Editor: {self.editor}")


# Start with empty inventories
book_inventory = []
dvd_inventory = []
journal_inventory = []

# Function to add new items
def add_item():
    item_type = input("Enter item type (Book, DVD, Journal): ").lower()
    if item_type == "book":
        title = input("Enter title: ")
        item_id = input("Enter item ID: ")
        author = input("Enter author: ")
        genre = input("Enter genre: ")
        quantity = int(input("Enter quantity: "))
        book_inventory.append(Book(title, item_id, author, genre, quantity))
    elif item_type == "dvd":
        # ... (Similar for DVD and Journal)
    else:
        print("Invalid item type.")

# Function to display inventory
def display_inventory():
    print("\nCurrent Inventory:")
    for item in book_inventory + dvd_inventory + journal_inventory:
        item.display_info()

# Function for check-out and check-in operations
def checkout_checkin():
    while True:
        choice = input("\nEnter 'C' to check out, 'I' to check in, 'A' to add item, or 'Q' to quit: ").upper()
        if choice == 'Q':
            break
        elif choice == 'C':
            display_inventory()
            item_id = input("\nEnter the Item ID to check out: ")
            for item in book_inventory + dvd_inventory
