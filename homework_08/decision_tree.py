import math


# create a decision tree to generate a tree that get the fastest derise answer
# from minimum question

# calculate class S's data entropy (where data have less disorder)
# formula: H(S) = sum(-p(n)*log2(p(n))) where n from 1 to infinity

def entropy(class_probabilities):
    sum_entropy = 0
    for p in class_probabilities:
        sum_entropy += (-p * math.log(p, 2))

    return sum_entropy

def class_probabilities(labels):
    count_positive = 0
    count_negative = 0
    total = len(labels)

    for i in range (len(labels)):
        if labels[i] == "YES":
            count_positive += 1
        else:
            count_negative += 1

    return [count_positive/total, count_negative/total]


def question_entropy(question):
    lst_labels = []
    




















class Pasta:
    def __init__(self, sauce_color, contains_meat, contains_seafood, like):
        self.sauce_color = sauce_color
        self.contains_meat = contains_meat
        self.contains_seafood = contains_seafood
        self.like = like

    def to_array(self):
        return [self.sauce_color, self.contains_meat, self.contains_seafood, self.like]
