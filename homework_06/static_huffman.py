# compressing text file using static huffman algorithm
import utils.data_structure.binary_tree

class Static_huffman():
    def __init__(self, string):
        self.input_string = string

    def get_frequency_dict(self):
        frequency_dict = {}

        # get the number of repeat of a chat in the string
        for char in self.input_string:
            if not (char in frequency_dict):
                frequency_dict[char] = 1
            else:
                frequency_dict[char] += 1

        for char in frequency_dict:
            frequency_dict[char] /= len(self.input_string)

        return dict(sorted(frequency_dict.items(), key=lambda x: x[1], reverse=False))

    def __generate_tree(self):
        binary_tree = utils.data_structure.binary_tree.AVLTree()

        static_huffman_dict = self.get_frequency_dict()

        for i in range(len(static_huffman_dict) - 1):
            __value, __key = None, None
            binary_tree.insert(list(static_huffman_dict.values())[0])

            if (len(static_huffman_dict) > 1):
                binary_tree.insert(list(static_huffman_dict.values())[1])

            if (len(static_huffman_dict) > 1):
                __value = list(static_huffman_dict.values())[0] + list(static_huffman_dict.values())[1]
                __key = list(static_huffman_dict.keys())[0] + list(static_huffman_dict.keys())[1]
                binary_tree.insert(__value)
            else:
                __value = list(static_huffman_dict.values())[0]
                __key = list(static_huffman_dict.keys())[0]

            static_huffman_dict.pop(list(static_huffman_dict.keys())[0])

            if (len(static_huffman_dict) > 1):
                static_huffman_dict.pop(list(static_huffman_dict.keys())[0])

            static_huffman_dict[__key] = __value
            static_huffman_dict = dict({k: v for k, v in sorted(static_huffman_dict.items(), key=lambda item: item[1])})

        return binary_tree

    def encode(self):

        encode_dict = {}
        arr = self.__generate_tree().inorder_traverse()

        encode_binary = ""
        for i in range(len(arr) - 2, -1, -1):
            if (i % 2 == 1):
                encode_dict[arr[i]] = encode_binary + "1"
            else:
                encode_dict[arr[i]] = encode_binary + "0"

                encode_binary += "1"

        return encode_dict


if __name__ == "__main__":
    string = input("Enter string need to compress: ")

    static_huffman = Static_huffman(string)
    frequency_dict = static_huffman.get_frequency_dict()
    encode_dict = static_huffman.encode()

    print(frequency_dict)
    print(encode_dict)
