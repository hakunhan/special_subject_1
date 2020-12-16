from tkinter.filedialog import askopenfilename
import codelive.analyse_user_data
import codelive.menu

filename = askopenfilename()
lst = []
try:
    with open(filename, 'r') as reader:
        for line in reader:
            lst.append(line.split('\n')[0])
except Exception as e:
    print(e)

analyseUserData = codelive.analyse_user_data.AnalyseUserData(lst)
list_books = analyseUserData.get_books_list()
list_names = analyseUserData.get_names_list()
ratings = analyseUserData.get_rating()

menu = codelive.menu.PrintMenu(list_books,list_names, ratings)
menu.print_intro()
menu.get_task()

