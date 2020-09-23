#capitalize first character of each sentences
#assuming the paragraph write in correct form
def capitalize(sentences):
    result = ""
    #split the sentences into list of sentence
    list_sentence = sentences.split(" ")
    print(list_sentence)

    for i in range(len(list_sentence)):
        #substring the sentence into first char that will be capitalize and the others then add into result
        result += list_sentence[i][0].upper() + list_sentence[i][1:len(list_sentence[i])] + " "

    return result

def main():
    sentences = input("Enter your sentences: ")
    print(capitalize(sentences))

main()