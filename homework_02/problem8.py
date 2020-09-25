#convert sentences into "Pig Latin"
#i.e. English "I slept most of the night"
#     Pig Latin "Iay leptsay ostmay foay hetay ightnay"

def convert(str):
    result = ""

    #split sencentes into list sentence
    list_sentence = str.split(" ")

    #loop through list sentence
    #if len(sentence) > 1:
    #   result add substring the second to last letter of that sentence + substring the first letter + "ay"
    #else
    #   result add sentence + "ay"
    for i in range(len(list_sentence)):
        if (len(list_sentence[i]) > 1):
            result += list_sentence[i][1:len(list_sentence[i])] + list_sentence[i][0] + "ay" + " "
        else:
            result += list_sentence[i] + "ay" + " "

    return result

def main():
    str = input("Enter the sentences: ")
    print(convert(str))

main()