# create a text file base on list
def create_text_file(name, lst):
    file = open(name, "w+")

    for i in range (len(lst)):
        file.write(f'{lst[i]}\r\n')

    file.close()
