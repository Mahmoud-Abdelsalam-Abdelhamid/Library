class User:
  all_users = []

  def __init__(self, name):
    self.name = name
    self.borrowed_books = []
    self.num_borrowed_books = len(self.borrowed_books)
    User.all_users.append(self)


class Book:
  all_books = []

  def __init__(self, title, author, date_of_publish, statues="Not borrowed"):
    self.title = title
    self.author = author
    self.date_of_publish = date_of_publish
    self.statues = statues
    Book.all_books.append(self)

  def __str__(self):
    return f"Book title: {self.title},Statues: {self.statues}"

  def __repr__(self):
    return f"title = {self.title} , author = {self.author} , date of publish = {self.date_of_publish} "


def main():
  print("-" * 15, "Welcome to Medo library", '-' * 15)
  print("Log in as:")
  main_menu_message = """1. Admin
2. User
3. Exit"""
  print(main_menu_message)
  choice = input("Enter your choice: ")
  if choice == "1":
    admin()
  elif choice == "2":
    user()
  elif choice == "3":
    return
  else:
    print("Invalid choice,Please Enter number between 1 and 3")
    main()


def admin():
  print("-" * 15, "Log in as Admin", '-' * 15)
  print()
  print()
  print(' ' * 15, "Select option")
  print()
  print()
  print("-" * 47)
  admin_menu_message = """1. Add new book
2. Show all books
3. Search for a book
4. Back to the main menu"""
  print(admin_menu_message)
  choice = input("Enter your choice: ")
  if choice == "1":
    add_book()
  elif choice == "2":
    show_books()
    admin()
  elif choice == "3":
    search_for_abook()
  elif choice == "4":
    main()
  else:
    print("Invalid choice,Please Enter number between 1 and 3")
    admin()


def user():
  print("-" * 15, "Log in as User", '-' * 15)
  print()
  print()
  name = input("Enter your name: ").strip().title()
  index_of_user = None
  for i in range(len(User.all_users)):
    if name == User.all_users[i]:
      index_of_user = i
  if index_of_user != None:
    user_menu(User.all_users[index_of_user])
  else:
    new_user = User(name)
    user_menu(new_user)


def add_book():
  print()
  title = input("Enter book title: ").strip().title()
  author_name = input("Enter author name: ")
  date_of_publish = input("Enter date of publish: ")
  book = Book(title, author_name, date_of_publish)
  print()
  print("Book added successfully to the library")
  print()

  admin()


def show_books():
  print("Available books: ")
  print("-" * 30)
  for i, book in enumerate(Book.all_books, 1):
    print(f"{i}. {book}")


def search_for_abook():
  book_title = input("Enter the title of the book: ").title()
  is_found = False
  for book in Book.all_books:
    if book_title == book.title:
      print(book)
      is_found = True
      break
  if not is_found:
    print("There is no such this book in the library")
  admin()


def user_menu(user_object):
  print("-" * 15, "Log in as User", '-' * 15)
  print()
  print()
  print(' ' * 15, "Select option")
  print()
  print()
  print("-" * 47)
  print("1. Show available books and borrow")
  print("2. Re-book")
  print("3. Check book")
  print("4. Back to main menu")
  choice = input("Enter your choice: ")
  if choice == "1":
    borrow_book(user_object)
    main()
  elif choice == "2":
    re_book(user_object)
    main()
  elif choice == "3":
    search_for_abook()
    main()
  elif choice == "4":
    main()
  else:
    print("Invalid option,Please choose number between 1 and 2")


def borrow_book(user_object):
  print("You hava at maximum 3 books to borrow")

  if user_object.num_borrowed_books > 3:
    print("exceeded the allowed number of books")
  else:
    show_books()
    print()
    try:
      book_number = int(input("Enter book number: "))
      if book_number <= 0:
        return
      borrowed_book = Book.all_books[book_number - 1]
      user_object.borrowed_books.append(borrowed_book)
      Book.all_books[book_number - 1].statues = "Borrowed"
      book_name = Book.all_books[book_number - 1].title
      print(f"{book_name} borrowed successfully")
    except ValueError:
      print("Invalid input,Please Enter number")
    except IndexError:
      print("Choose book from the available books")


def re_book(user_ob):
  book_title = input("Enter book title: ").title()
  book_index_in_user = None
  for i in range(len(user_ob.borrowed_books)):
    if book_title == user_ob.borrowed_books[i].title:
      book_index_in_user = i
  if book_index_in_user != None:
    del user_ob.borrowed_books[book_index_in_user]
  book_index_in_book = None
  for i in range(len(Book.all_books)):
    if book_title == Book.all_books[i].title:
      book_index_in_book = i
  if book_index_in_book != None:
    Book.all_books[book_index_in_book].statues = "Not borrowed"
    print("Re-book successfully")


if __name__ == "__main__":
  main()
