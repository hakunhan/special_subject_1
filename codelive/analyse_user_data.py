# analyse user rating data to get the list of book title and rating of each person
class AnalyseUserData:
    # parameter: list of data
    def __init__(self, lst):
        self.lst = lst

    # read the list of user data and return books list
    def get_books_list(self):
        set_books = set()
        for i in range (1, len(self.lst), 3):
            set_books.add(self.lst[i].strip())

        return list(set_books)

    # read the list of user data and return user name
    def get_names_list(self):
        set_name = set()
        for i in range (0, len(self.lst), 3):
            set_name.add(self.lst[i].strip())

        return list(set_name)

    # read the list of user data and return a dictionary of their rating of each book
    def get_rating(self):
        list_book = self.get_books_list()
        list_name = self.get_names_list()
        rating_dictionary = {}

        for i in range (0, len(list_name)):
            rating_dictionary[list_name[i]] = [0]*len(list_book)

        for i in range (0, len(self.lst), 3):
            rating_dictionary[self.lst[i].strip()][list_book.index(self.lst[i+1].strip())] = int(self.lst[i+2])

        return rating_dictionary