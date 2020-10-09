#getting input from user

#getting string input from user
def string(message):
    str = input(message)
    return str

#getting number input from user
def number(message):
    num = 0
    while True:  # Keep getting input from the user
        try:
            num = input(message)
            if num.isnumeric():
                break
            else:
                print('Invalid input! Please try again')
        except ValueError:
            print('Conversion error, please re-input')
            continue
    return num

#getting list of element
def list(message):
    lst = []

    n = int(number(f"Enter number of element {message}: "))

    for i in range (n):
        element = input(f"Element number {i+1}: ")

        lst.append(element)

    return lst

#reading file and turn in to list base on the file path
def file_to_list(message):
    lst = []
    print(f"{message}")
    print(r"(Example of path: C:\Users\Administrator\Documents\GitHub\special_subject_1\utils\get_input)")
    file_path = input()

    try:
        with open(file_path,'r') as reader:
            for line in reader:
                lst.append(line.split('\n')[0])
    except Exception as e:
        print('Not succeed in read file! Please try again!')
        return file_to_list(message)

    return lst