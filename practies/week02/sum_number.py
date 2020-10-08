#getting the sum of series of single digit number
#require: no separation between each digit
#e.g. input: 2514 -> output: 12

import utils.get_input

def get_sum(num):
    result = [] #creating a list to add each number
    for i in range (len(num)):
        result.append(int(num[i]))

    return sum(result)

def main():
    num = utils.get_input.number("Enter number without separation: ")

    print(f"The sum of the series of single digit numbers is: {get_sum(num)}")

main()