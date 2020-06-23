from library import Library

def test_library():
    list_of_books = [{"book_id":1, "title" :"a1"}, {"book_id":2, "title" :"a2"}]
    my_library = Library(list_of_books)
    my_library.issue_book(1, "Satya")
    my_library.issue_book(234, "Satya2")
    my_library.return_book(1)
    
    
    

if __name__ == "__main__":
    test_library()