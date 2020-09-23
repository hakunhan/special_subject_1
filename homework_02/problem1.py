#get initials base on user input name
#i.e

def print_initials(name):
    #split the name into list
    name_list = list(name.split(" "))

    #print the first letter of the name as initials
    for letter in name_list:
        print(letter[0].upper(),end = ". ")

def main():
    #get user name
    name = input("Enter your name: ")
    print_initials(name)

main()