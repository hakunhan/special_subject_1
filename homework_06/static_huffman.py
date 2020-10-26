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

        for char in frequency_dict:
            frequency_dict[char] /= len(self.input_string)

        return dict(sorted(frequency_dict.items(), key=lambda x: x[1], reverse=False))

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

            node = HuffmanNode("", first_node.frequency + second_node.frequency, None, first_node, second_node)
            huffman_list.append(node)

            tree = HuffmanTree(node)
            tree.gen_binary_code()

        return tree

if __name__ == "__main__":
    string = input("Enter string need to compress: ")

    static_huffman = Static_huffman(string)
    sys.getrecursionlimit
    #print(str(static_huffman.build_huffman_tree()))
