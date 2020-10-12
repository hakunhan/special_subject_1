#create a text file base on list
def create_text_file(name,list):
    file = open(name,"w+")

    for i in range (len(list)):
        file.write(f'{list[i]}\r\n')

    file.close()