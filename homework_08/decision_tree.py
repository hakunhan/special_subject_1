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

def class_probabilities(label):
    count_positive = 0
    count_negative = 0
    total = len(label)

    for i in range (len(label)):
        if label[i] == "YES":
            count_positive += 1
        else:
            count_negative += 1

    return [count_positive/total, count_negative/total]


def question_information_gain(question):
    lst_labels = []

    for i in range(len(question)):
        if (question[i] in lst_labels):
            continue

        lst_labels.append(question[i])

    def question_entropy():
        count_positive = 0
        count_negative = 0

        for j in range(len(lst_labels)):
            label = lst_labels[j]
            for j in range(len(label)):
                if label[j] == "YES":
                    count_positive += 1
                else:
                    count_negative += 1

        total = count_positive + count_negative

        return entropy([count_positive/total, count_negative/total])

    def average_weight_subtree_entropy():
        total_entropy = 0

        for j in range(len(lst_labels)):
            probabilities = class_probabilities(lst_labels)
            label_entropy = entropy(probabilities)
            total_entropy += label_entropy

        return total_entropy

    return question_entropy() - average_weight_subtree_entropy()

















class Pasta:
    def __init__(self, sauce_color, contains_meat, contains_seafood, like):
        self.sauce_color = sauce_color
        self.contains_meat = contains_meat
        self.contains_seafood = contains_seafood
        self.like = like

    def to_array(self):
        return [self.sauce_color, self.contains_meat, self.contains_seafood, self.like]
