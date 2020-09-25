#convert sentence that has no space between each words and has a uppercase letter
#for first character in every word to a sentence that has space between each words
#and only have uppercase for the first word of the sentence
#i.e. "StopAndSmellTheRose" => "Stop and smell the rose"

#convert sentence
def convert(str):
    result = ''

    #counting the current letter in the string
    current_letter = 0
    #counting the current letter before the uppercase word
    before_uppercase = 0

    #if letter is in uppercase and not the first letter
    #   result add all the character before the uppercase word and current_letter++
    #   set before_uppercase = current_letter
    #   skip the next iteration
    #current_letter++
    for letter in str:
        if (letter.isupper() and current_letter != 0):
            result += str[before_uppercase: current_letter] + " " + str[current_letter].lower()
            current_letter+=1
            before_uppercase = current_letter
            continue

        current_letter += 1

    #adding the last part of the word as the loop skip
    result += str[before_uppercase:len(str)]
    return result

def main():
    str = input("Enter the sentence has no space and uppercase the first letter in each words: ")
    print(convert(str))

main()