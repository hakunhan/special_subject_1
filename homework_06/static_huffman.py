# compressing text file using static huffman algorithm
import utils.data_structure.binary_tree

class Node():
    def __init__(self, data=None, frequency=0, left=None, right=None):
        self.data = data
        self.frequency = frequency
        self.left = left
        self.right = right

    def printTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

class Binary_tree():
    def __init__(self):
        self.node = None

    def insert(self, data = None, frequency = 0):
        tree = self.node

        if tree == None:
            self.node = Node(data,frequency)
            self.node.left = Binary_tree()
            self.node.right = Binary_tree()

        elif frequency < tree.frequency:
            self.node.left.insert(data,frequency)

        elif frequency > tree.frequency:
            self.node.right.insert(data,frequency)


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
        huffman_dict = self.get_frequency_dict()
        tree = Binary_tree()

        while(len(huffman_dict) > 1):
            tree.insert(list(huffman_dict.keys())[1], list(huffman_dict.values())[1])
            __value = list(huffman_dict.values())[1] + list(huffman_dict.values())[1]
            #tree.insert('\0',__value)
            tree.insert(list(huffman_dict.keys())[0],list(huffman_dict.values())[1])

            huffman_dict.pop(list(huffman_dict.keys())[0])
            huffman_dict.pop(list(huffman_dict.keys())[1])
            huffman_dict['\0'] = __value

        return tree

if __name__ == "__main__":
    string = input("Enter string need to compress: ")

    static_huffman = Static_huffman(string)
    frequency_dict = static_huffman.get_frequency_dict()
    tree = static_huffman.build_huffman_tree()
    print(tree.node)

