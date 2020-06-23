from collections import defaultdict

class Book() :
    def __init__(self, book_id, title = None, author = None, dop = None):
        super(Book, self).__init__()
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__dop = dop
        self.__issuer = None
    
    def issued_to(self, issuer):
        self.__issuer = issuer
    
    def returned(self):
        self.__issuer = None
    
    def is_issued(self):
        if self.__issuer == None:
            return False
        else:
            return True

    def __eq__ (self, other):
        if not isinstance(other, Book):
            # don't attempt to compare against unrelated types
            return NotImplemented
    
        return self.__book_id == other.__book_id
    
    
class Library() :
    def __init__(self, init_book_list ):
        super(Library, self).__init__()
        self.books = defaultdict(Book)
        for book in init_book_list:
            self.books[book["book_id"]] = Book(**book) # Book is active in the library
    
    def issue_book(self, book_id, issuer ):
        '''
        Issue a book from library
        :param book_id: Book identifier
        :param issuer:  Book issuer name
        :return: Nothing
        '''
        if book_id not in self.books or self.books[book_id] == None :
            print("Book : {} not in library!".format(book_id))
        else :
            if self.books[book_id].is_issued():
                print("Book : {} is not available for issuance".format(book_id))
            else :
                self.books[book_id].issued_to(issuer)
                print("Book : {} is successfully issued to {}".format(book_id, issuer))
    
    def return_book(self, book_id):
        '''
        Return a book to the library
        :param book_id:  Book identifier
        :return: None
        '''
        if book_id not in self.books or self.books[book_id] == None:
            print("Book : {} not in library!".format(book_id))
        else:
            if self.books[book_id].is_issued():
                self.books[book_id].returned()
                print("Book : {} is successfully returned".format(book_id))
            else:
                print("Book : {} is not issued. ".format(book_id))
    
    def remove_book_from_library(self, book_id):
        '''
        Remove book from library
        :param book_id: Book identifier
        :return: None
        '''
        if book_id not in self.books or self.books[book_id] == None:
            print("Book : {} not in library!".format(book_id))
        else :
            self.books[book_id] = None
            print("Book : {} removed from library!".format(book_id))
        
    
    def add_book_to_library(self, book_details):
        '''
        Add a new book to the library
        :param book_details : dict
        :return: None
        '''
        if book_details["book_id"] in self.books :
            print("Book {} already in the library". format(book_details["book_id"]))
        else:
            self.books[book_details["book_id"]] = Book(**book_details)
            print("Book {} is successfully added to the library".format(book_details["book_id"]))
            
        
        
    
    