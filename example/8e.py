def book_list(books, func):
  for book in books:
    print(func(book))
books = ['Мартин Иден','Стоицизм','Охотники на жирафов']
book_list(books, lambda book: book.upper() + ' - остался в восторге')
