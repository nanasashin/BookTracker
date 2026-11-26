from sqlmodel import SQLModel, Field, Relationship

# class Subgenre(SQLModel, table=True):
#     pass

class BookSubgenre(SQLModel, table=True):
    book_id: int | None = Field(default=None, foreign_key="book.id", primary_key=True)
    sub_genre_id: int | None = Field(default=None, foreign_key="")

# class BookSeries(SQLModel, table=True):
#     pass

class BookUser(SQLModel, table=True):
    user_id: int | None = Field(default=None, foreign_key="user.id", primary_key=True)
    book_id: int | None = Field(default=None, foreign_key="book.id", primary_key=True)

class Author(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

# class Series(SQLModel, table=True):
#     pass

class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    genre: str

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    books: list[Book] = Relationship(link_model=BookUser)