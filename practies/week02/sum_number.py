#getting the sum of series of single digit number
#require: no separation between each digit
#e.g. input: 2514 -> output: 12

def get_sum(num):
    result = [] #creating a list to add each number
    for i in range (len(num)):
        result.append(int(num[i]))

    return sum(result)

def main():
    num = 0

    while True:  # Keep getting input from the user
        try:
            num = input('Enter number without separation: ')
            if num.isnumeric():
                break
            else:
                print('Invalid input! Please try again')
        except ValueError:
            print('Conversion error, please re-input the the number!')
            continue

    print(num)
    print(f"The sum of the series of single digit numbers is: {get_sum(num)}")

main()