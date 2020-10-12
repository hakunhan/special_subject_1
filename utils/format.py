#printing format

#print a split line
def print_split_line(number_of_minus):
    a = '-'*number_of_minus
    print(a)

#format a list with index at first of each element
#e.g. ['a','b','c'] -> ['1. a', '2. b', '3. c]
def format_list(list):
    _temp = []

    for i in range (len(list)):
        _temp.append(f'{i+1}. {list[i]}')

    return _temp