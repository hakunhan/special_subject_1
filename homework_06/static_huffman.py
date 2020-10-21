# compressing text file using static huffman algorithm
import utils.data_structure.binary_tree

def get_frequency_dict(string):
    frequency_dict = {}

    # get the number of repeat of a chat in the string
    for char in string:
        if not (char in frequency_dict):
            frequency_dict[char] = 1
        else:
            frequency_dict[char] += 1

    for char in frequency_dict:
        frequency_dict[char] /= len(string)

    return dict(sorted(frequency_dict.items(), key = lambda x : x[1], reverse=False))

def static_huffman(my_dict):
    binary_tree = utils.data_structure.binary_tree.AVLTree()

    static_huffman_dict = my_dict

    for i in range (len(my_dict)):
        __value, __key = None, None

        


    return binary_tree

my_dict = get_frequency_dict("asdgfasdfasfasdf")
print(my_dict)
print(list(my_dict.keys())[0])

arr = static_huffman(my_dict).inorder_traverse()
print(arr)
