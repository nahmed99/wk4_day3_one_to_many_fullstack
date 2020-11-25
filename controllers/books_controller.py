from flask import Flask, render_template, Blueprint, redirect, request
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository


books_blueprint = Blueprint("books", __name__)


# Also an INDEX - just in case user doesn't type in /books...
@books_blueprint.route('/')
def index():
    # This will redirect the user to the books index page
    return redirect("/books")

# INDEX
# GET '/books'
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    authors = author_repository.select_all
    return render_template("books/index.html", all_books=books, all_authors=authors)


# NEW
# GET '/books/new'
@books_blueprint.route("/books/new", methods=["GET"])
def new_book():
    authors = author_repository.select_all()
    # pass the authors, so that user can select the author name...or do we want free-form text (for a new author)???
    return render_template("books/new.html", authors_list=authors)


# CREATE
# POST '/books'
@books_blueprint.route("/books", methods=["POST"])
def create_book():
    # grab the form data for the the book variables: title, genre, publisher, author
    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']
    author_id = request.form['author_id']

    # select (existing author)
    author = author_repository.select(author_id)

    # create new book object
    book = Book(title, genre, publisher, author)

    # Save new book object in database
    book_repository.save(book)

    return redirect('/books')



# SHOW
# GET '/books/<id>'
@books_blueprint.route('/books/<id>')
def show_book(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book=book)


# EDIT
# GET '/books/<id>/edit'


# UPDATE
# PUT '/books/<id>'



# DELETE
# DELETE '/books/<id>'

@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')

