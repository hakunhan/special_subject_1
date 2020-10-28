# compressing text using static huffman algorithm
# static huffman algorithm:
# step 1: calculate frequency of each character
# step 2: build an huffman tree base on frequency of each character
# step 3: assign bit value to each branches

class StaticHuffman:
    def __init__(self, string=None, path=None):
        self.__string = string
        self.__path = path  # for input file (will implement later)
        self.__codes = {}  # storing binary encode of each characters

    class HuffmanNode:
        def __init__(self, char, freq, left=None, right=None):
            self.char = char
            self.freq = freq
            self.left = left
            self.right = right

    # generate frequency dictionary for building huffman tree
    def gen_frequency_dict(self):
        frequency = {}
        string = self.__string
        for char in string:
            if not char in frequency:
                frequency[char] = 0
            frequency[char] += 1

        return frequency

    # generate huffman tree's root with child
    def __gen_huffman_tree(self):

        # support method for generating huffman tree
        def get_two_min_node(node_list):
            lst = sorted(node_list, key = lambda x: x.freq, reverse=False)

            first_min_node = lst[0]
            second_min_node = lst[1]

            return [first_min_node, second_min_node]

        huffman_list = []
        frequency_dict = self.gen_frequency_dict()

        for char in frequency_dict:
            node = self.HuffmanNode(char, frequency_dict[char])
            huffman_list.append(node)

        # keep removing two smallest frequency node and
        # adding the sum of frequency as an new node
        # to the node list until getting the root of the tree
        while (len(huffman_list) > 1):
            first_node, second_node = get_two_min_node(huffman_list)
            huffman_list.remove(first_node)
            huffman_list.remove(second_node)

            node = self.HuffmanNode(None, first_node.freq + second_node.freq, first_node, second_node)
            huffman_list.append(node)

        return huffman_list[0]

    # support method to assign binary number to branch
    def __gen_code_helper(self, root, current_code):
        if (root == None):
            return

        if root.char != None:
            self.__codes[root.char] = current_code
            return

        self.__gen_code_helper(root.left, current_code + "0")
        self.__gen_code_helper(root.right, current_code + "1")

    def gen_code(self):
        root = self.__gen_huffman_tree()
        current_code = ""
        self.__gen_code_helper(root, current_code)
        return self.__codes


# =================== END OF STATIC HUFFMAN CLASS ============================

if __name__ == '__main__':
    string = "abbc"
    static_huffman = StaticHuffman(string)
    print(static_huffman.gen_frequency_dict())
    print(static_huffman.gen_code())
