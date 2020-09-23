#convert 10-character telephone number format XXX-XXXX-XXX to numberic format
#i.e 555-GET-GOOD will be converted to 555-438-4663

#creating char to number dictionary
def generate_dict():
    #declaring empty dict and key
    dict = {}
    keys = range(2,10)
    #declaring empty list character
    char_list = []

    #generating list char from A to Z
    for i in range (65,91):
        char_list += chr(i)

    #creating dict base on keys and char_list
    current_char = 0
    for i in keys:
        for j in range (0,3):
            #P,Q,R,S replace by 7
            if (i == 7 and j == 2):
                dict[char_list[current_char]] = i
                current_char+=1
                dict[char_list[current_char]] = i
                current_char+=1
            dict[char_list[current_char]] = i
            current_char += 1

    return dict

#convert tele_number 10-character format to numeric (assuming user input the right format)
def convert(tele_number):
    #generate blank result
    result = ""

    #convert tele_number format to numeric
    for letters in tele_number:
        if letters.isalpha() :
            result += str(generate_dict()[letters.upper()])
        else:
            result += letters

    return result

def main():
    tele_number = input("Enter the telephone number format in 10-character: ")
    print(convert(tele_number))

main()