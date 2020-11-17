# Entropy
import math
from collections import Counter, defaultdict
from functools import partial

""" Data form: (inputs, label)"""
# example: ({'level':'Senior', 'lang':'Java', 'tweets':'no', 'phd':'no'}, False)
#   here 'level' is attribute,
#        'Senior' one of inputs can insert into 'level' input type
#        'False' is label

"""--- Entropy calculation part ---"""

# the entropy will be calculated by the label probabilities p in
# consideration of multiple not only two label as in binary classifying decision
def entropy(class_probabilities):
    return sum(-p * math.log(p,2) for p in class_probabilities if p) #ignore zero probability

"""calculate the probabilities with data in form (input, label)"""

# return the probabilities of labels
def class_probabilities(labels):
    total_count = len(labels)
    return [count/ total_count for count in Counter(labels).values()]

# return the entropy of a input
def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    probabilities = class_probabilities(labels);
    return entropy(probabilities)

# return the entropy of an attribute
def partition_entropy(subsets):
    total_count = sum(len(subset) for subset in subsets)
    return sum(data_entropy(subset) * len(subset) / total_count for subset in subsets)

def partition_by(inputs, attribute):
    groups = defaultdict(list)
    for input in inputs:
        key = input[0][attribute]
        groups[key].append(input)
    return groups

def partition_entropy_by(inputs, attribute):
    patitions = partition_by(inputs, attribute)
    return partition_entropy(patitions.values())

""" --- Sample Input --- """

# this input has 4 input types (level, lang, tweets, phd) and 2 labels (True and False)
inputs = [
 ({'level':'Senior', 'lang':'Java', 'tweets':'no', 'phd':'no'}, False),
 ({'level':'Senior', 'lang':'Java', 'tweets':'no', 'phd':'yes'}, False),
 ({'level':'Mid', 'lang':'Python', 'tweets':'no', 'phd':'no'}, True),
 ({'level':'Junior', 'lang':'Python', 'tweets':'no', 'phd':'no'}, True),
 ({'level':'Junior', 'lang':'R', 'tweets':'yes', 'phd':'no'}, True),
 ({'level':'Junior', 'lang':'R', 'tweets':'yes', 'phd':'yes'}, False),
 ({'level':'Mid', 'lang':'R', 'tweets':'yes', 'phd':'yes'}, True),
 ({'level':'Senior', 'lang':'Python', 'tweets':'no', 'phd':'no'}, False),
 ({'level':'Senior', 'lang':'R', 'tweets':'yes', 'phd':'no'}, True),
 ({'level':'Junior', 'lang':'Python', 'tweets':'yes', 'phd':'no'}, True),
 ({'level':'Senior', 'lang':'Python', 'tweets':'yes', 'phd':'yes'}, True),
 ({'level':'Mid', 'lang':'Python', 'tweets':'no', 'phd':'yes'}, True),
 ({'level':'Mid', 'lang':'Java', 'tweets':'yes', 'phd':'no'}, True),
 ({'level':'Junior', 'lang':'Python', 'tweets':'no', 'phd':'yes'}, False)
]

""" --- Decision tree --- """
def classify(tree, input):
    if tree in [True, False]:
        return tree

    attribute, subtree_dict = tree
    subtree_key = input.get(attribute)
    if subtree_key not in subtree_dict:
        subtree_key = None

    subtree = subtree_dict[subtree_key]
    return classify(subtree, input)

def build_tree_id3(inputs, split_candidates=None):
 # if this is our first pass,
 # all keys of the first input are split candidates
    if split_candidates is None:
     split_candidates = inputs[0][0].keys()
     # count Trues and Falses in the inputs
     num_inputs = len(inputs)
     num_trues = len([label for item, label in inputs if label])
     num_falses = num_inputs - num_trues

     if num_trues == 0: return False  # no Trues? return a "False" leaf
     if num_falses == 0: return True  # no Falses? return a "True" leaf

     if not split_candidates:  # if no split candidates left
         return num_trues >= num_falses  # return the majority leaf
     # otherwise, split on the best attribute
    best_attribute = min(split_candidates,
                          key=partial(partition_entropy_by, inputs))
    partitions = partition_by(inputs, best_attribute)
    new_candidates = [a for a in split_candidates
                       if a != best_attribute]
    # recursively build the subtrees
    subtrees = {attribute_value: build_tree_id3(subset, new_candidates)
                 for attribute_value, subset in partitions.iteritems()}
    subtrees[None] = num_trues > num_falses  # default case
    return (best_attribute, subtrees)


