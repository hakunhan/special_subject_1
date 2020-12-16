# print menu to console for user to choose
import codelive.perform_task
class PrintMenu:
    def __init__(self, list_books, list_users, dictionary_data):
        self.list_books = list_books
        self.list_user = list_users
        self.dictionary_data = dictionary_data

    # print intro menu to console
    def print_intro(self):
        print("Welcome to the CSC110 Book Recommender. Type the word in the \n"
              "left column to do the action on the right. \n"
              "recommend (r): recommend books for a particular user \n"
              "averages  (a): output the average ratings of all books in the system \n"
              "quit      (q): exit the program")

    # get choosing task from user and return task function
    def get_task(self):
        while (True):
            task = input("next task? ")
            perfromTask = codelive.perform_task.PerformTask(self.list_books, self.list_user, self.dictionary_data)
            if (task.lower() == 'r' or task.lower() == "recommend"):
                perfromTask.get_recommendations()
            elif (task.lower() == 'a' or task.lower() == "averages"):
                perfromTask.get_averages()
            elif (task.lower() == 'q' or task.lower() == 'quit'):
                quit()
            else:
                print("Wrong format input! Type the word in the \n"
                      "left column to do the action on the right. \n"
                      "recommend (r): recommend books for a particular user \n"
                      "averages  (a): output the average ratings of all books in the system \n"
                      "quit      (q): exit the program")
