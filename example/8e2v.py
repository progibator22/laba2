def book_list(books, func):
    for book in books:
        print(func(book))
books = ['Мартин Иден','Стоицизм','Охотники на жирафов']
def book_print(book):
    return book.upper() + ' - остался в восторге'
book_list(books, book_print)
