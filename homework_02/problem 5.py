#return the number of vowels and consonants of a string

#return the number of vowels in a string
def number_of_vowels(str):
    #list of vowels
    vowels = ['a','i','e','o','u']
    number_of_vowels = 0

    #getting number of vowels in str
    for letter in str:
        if letter in vowels:
            number_of_vowels+=1

    return number_of_vowels

#return the number of consonants in a string (assuming Y also an consonants in all case)
def number_of_consonants(str):
    #list of vowels
    vowels = ['a', 'i', 'e', 'o', 'u']
    number_of_consonants = 0

    #getting number of consonants in str
    for letter in str:
        if letter not in vowels:
            number_of_consonants+=1

    return number_of_consonants

def main():
    str = input("Enter your string: ")
    print(number_of_vowels(str))
    print(number_of_consonants(str))

main()