# In-memory storage for books and members
books = []
members = []

# Utility function to generate IDs
def generate_id(data_list):
    return len(data_list) + 1

# CRUD operations for Books
def add_book(title, author, publication_year):
    book_id = generate_id(books)
    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "publication_year": publication_year,
    }
    books.append(new_book)
    return new_book

def get_books():
    return books

def get_book_by_id(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None

def update_book(book_id, title, author, publication_year):
    book = get_book_by_id(book_id)
    if book:
        book["title"] = title
        book["author"] = author
        book["publication_year"] = publication_year
        return book
    return None

def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return True

# CRUD operations for Members
def add_member(name, email, membership_id):
    member_id = generate_id(members)
    new_member = {
        "id": member_id,
        "name": name,
        "email": email,
        "membership_id": membership_id,
    }
    members.append(new_member)
    return new_member

def get_members():
    return members

def get_member_by_id(member_id):
    for member in members:
        if member["id"] == member_id:
            return member
    return None

def update_member(member_id, name, email, membership_id):
    member = get_member_by_id(member_id)
    if member:
        member["name"] = name
        member["email"] = email
        member["membership_id"] = membership_id
        return member
    return None

def delete_member(member_id):
    global members
    members = [member for member in members if member["id"] != member_id]
    return True
