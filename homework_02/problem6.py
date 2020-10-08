#return the most frequent char in a string
def most_frequent_char(str):
    frequent_char = ''

    #generate char list
    list_char = [char for char in str]

    #sort char list
    list_char.sort()

    #generating counter for the time most frequent char appear
    most_appearance = 0
    #generating counter for each time current frequent char appear
    current_appearance = 0

    #comparing the current frequent character with the most frequent character each time
    #to get the most frequent character of the string
    for i in range (len(list_char) - 1):
        if(list_char[i] == list_char[i+1]):
            current_appearance+=1
        else:
            current_appearance = 0

        if(current_appearance >= most_appearance):
            most_appearance = current_appearance
            frequent_char = list_char[i]

    return frequent_char

def main():
    str = input("Enter string: ")
    print(most_frequent_char(str))

main()