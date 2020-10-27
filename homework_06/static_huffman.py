<<<<<<< HEAD
import sys

class StaticHuffman:
    def __init__(self, path = None, string = None):
        self.__string = string
        self.__path = path
        self.__codes = {}

    class HuffmanNode:
        def __init__(self, char, freq, left = None, right = None):
            self.char = char
            self.freq = freq
            self.left = left
            self.right = right

    def __gen_frequency_dict(self):
            frequency = {}
            string = self.__string
            for char in string:
                if not char in frequency:
                    frequency[char] = 0
                frequency[char] += 1

            return frequency

    def __gen_huffman_tree(self):
        def get_two_min_node(node_list):
            second_node = node_list[0]
            first_node = node_list[1]

            for node in node_list:
                if node.freq <= first_node.freq:
                    second_node = first_node
                    first_node = node

            return [first_node, second_node]

        huffman_list = []
        frequency_dict = self.__gen_frequency_dict()
        print(frequency_dict)
=======
# compressing text file using static huffman algorithm
import sys

import utils.data_structure.binary_tree


class HuffmanNode():
    def __init__(self, binary_code = '' ,frequency=0, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.binary_code = binary_code
        self.frequency = frequency

    def get_binary_code(self):
        return str(self.binary_code)
<<<<<<< Updated upstream

    def set_binary_code(self,binary_string):
        self.binary_code = binary_string

    def set_left_child_binary_code(self):
        self.left.set_binary_code(self.get_binary_code() + "0")

    def set_right_child_binary_code(self):
        self.right.set_binary_code(self.get_binary_code() + "1")

    def get_frequency(self, frequency):
        return self.frequency


class HuffmanTree():
    def __init__(self,root):
        self.root = root

    def gen_binary_code(self, node=None):
        if self.root is None or self.root.left is None or self.root.right is None:
            return

=======

    def set_binary_code(self,binary_string):
        self.binary_code = binary_string

    def set_left_child_binary_code(self):
        self.left.set_binary_code(self.get_binary_code() + "0")

    def set_right_child_binary_code(self):
        self.right.set_binary_code(self.get_binary_code() + "1")

    def get_frequency(self, frequency):
        return self.frequency


class HuffmanTree():
    def __init__(self,root):
        self.root = root

    def gen_binary_code(self, node=None):
        if self.root is None or self.root.left is None or self.root.right is None:
            return

>>>>>>> Stashed changes
        self.root.set_right_child_binary_code()
        self.root.set_left_child_binary_code()

        self.gen_binary_code(self.root.left)
        self.gen_binary_code(self.root.right)


class Static_huffman():
    def __init__(self, input_string):
        self.input_string = input_string

    def get_frequency_dict(self):
        frequency_dict = {}

        # get the number of repeat of a chat in the string
        for char in self.input_string:
            if not (char in frequency_dict):
                frequency_dict[char] = 1
            else:
                frequency_dict[char] += 1
>>>>>>> 9f287c2b1727a924a4b1713591f8197a19c437ca

        for char in frequency_dict:
            node = self.HuffmanNode(char, frequency_dict[char])
            huffman_list.append(node)

        while (len(huffman_list) > 1):
            first_node, second_node = get_two_min_node(huffman_list)
            huffman_list.remove(first_node)
            huffman_list.remove(second_node)

            node = self.HuffmanNode(None, first_node.freq + second_node.freq, first_node, second_node)
            huffman_list.append(node)

<<<<<<< HEAD
        return huffman_list[0]

    def __gen_code_helper(self, root, current_code):
        if(root == None):
            return

        if root.char != None:
            self.__codes[root.char] = current_code
            return
=======
    def build_huffman_tree(self):
        tree = None
        def get_two_min_node(node_list):
            second_node = node_list[0]
            first_node = node_list[1]

            for node in node_list:
                if node.frequency <= first_node.frequency:
                    second_node = first_node
                    first_node = node

            return [first_node, second_node]

        huffman_dict = self.get_frequency_dict()
        huffman_list = []

        for char in huffman_dict:
            node = HuffmanNode("",huffman_dict[char],char)
            huffman_list.append(node)

        while (len(huffman_list) > 1):
            first_node, second_node = get_two_min_node(huffman_list)
            huffman_list.remove(first_node)
            huffman_list.remove(second_node)
<<<<<<< Updated upstream

            node = HuffmanNode("", first_node.frequency + second_node.frequency, None, first_node, second_node)
            huffman_list.append(node)

            tree = HuffmanTree(node)
            tree.gen_binary_code()
=======
>>>>>>> Stashed changes

            node = HuffmanNode("", first_node.frequency + second_node.frequency, None, first_node, second_node)
            huffman_list.append(node)

            tree = HuffmanTree(node)
            tree.gen_binary_code()
>>>>>>> 9f287c2b1727a924a4b1713591f8197a19c437ca

<<<<<<< Updated upstream
    static_huffman = Static_huffman(string)
    sys.getrecursionlimit
    #print(str(static_huffman.build_huffman_tree()))
=======
        self.__gen_code_helper(root.left, current_code + "0")
        self.__gen_code_helper(root.right, current_code + "1")

    def gen_code(self):
        root = self.__gen_huffman_tree()
        current_code = ""
        self.__gen_code_helper(root, current_code)
        return self.__codes

<<<<<<< HEAD

if __name__ == '__main__':
    string = "abcabccbb"
    static_huffman = StaticHuffman(None,string)
    print(static_huffman.gen_code())
=======
    static_huffman = Static_huffman(string)
    sys.getrecursionlimit
    #print(str(static_huffman.build_huffman_tree()))
>>>>>>> 9f287c2b1727a924a4b1713591f8197a19c437ca
>>>>>>> Stashed changes
