#searching index of key using linear search

#loop though the list_key
#if key found, return index of key
#else return "Can't found key"
def linear_search(key, list_key):
    for i in range (len(list_key)):
        if (key == list_key[i]):
            return i
    return f"Can't found {key}"

def main():
    list_key = list(map(str,input("Enter your list: ")))
    key = input("Enter the key need to search: ")
    print(linear_search(key,list_key))

main()