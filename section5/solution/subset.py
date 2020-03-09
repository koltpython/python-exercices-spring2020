"""
Input:
the lenght of the first set => integer
the elements in the first set one by one => integer
the lenght of the second set => integer
the elements in the second set one by one => integer 
Output:
print YES if one of them is a subset of the other
print NO otherwise
"""


def take_input_set():
    set_length = int(input("Length of the set: "))
    input_set = set()
    while len(input_set) < set_length:
        element = input(f"Enter element {len(input_set) + 1}: ")
        input_set.add(element)

    return input_set

# Given two sets check whether one of them is a subset of the other


def check_is_subset(set1, set2):
    set3 = set1.union(set2)
    return len(set3) == len(set1) or len(set3) == len(set2)


print("This program checks whether one of the given two sets is one of the subsets of the other.")
set1 = take_input_set()
set2 = take_input_set()
result = check_is_subset(set1, set2)
print(f"Set1 = {set1} Set2 {set2} => {'YES' if result else 'NO'}")
