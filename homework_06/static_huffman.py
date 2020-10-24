# compressing text file using static huffman algorithm
import utils.data_structure.example_binary_tree

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

class binary_tree():
    def __init__(self, key):
        self.key = key
        self

def static_huffman(my_dict):
    b_tree = binary_tree()
    b_tree.insert("1")

    static_huffman_dict = my_dict

    for i in range (len(my_dict)):
        __value, __key = None, None
        b_tree.insert(list(static_huffman_dict.keys())[0])

        if(len(static_huffman_dict) > 1):
            b_tree.insert(list(static_huffman_dict.keys())[1])

        if(len(static_huffman_dict) > 1):
            __value = list(static_huffman_dict.values())[0] + list(static_huffman_dict.values())[1]
            __key = list(static_huffman_dict.keys())[0] + list(static_huffman_dict.keys())[1]
        else:
            __value = list(static_huffman_dict.values())[0]
            __key = list(static_huffman_dict.keys())[0]


        static_huffman_dict.pop(list(static_huffman_dict.keys())[0])

        if(len(static_huffman_dict) > 1):
            static_huffman_dict.pop(list(static_huffman_dict.keys())[0])

        static_huffman_dict[__key] = __value
        dict(sorted(static_huffman_dict.items(), key = lambda x: x[1]), reverse = False)
        print(static_huffman_dict)

    return b_tree

my_dict = get_frequency_dict("asdgfasdfasfasdf")
print(my_dict)

arr = static_huffman(my_dict)
print(arr.inorder_traverse())
print(arr.display())
