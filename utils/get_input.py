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