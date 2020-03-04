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
#It takes the length of the set as input and then takes this number of elements one by one. Returns the set.
def take_input_set():
    num_elements = int(input("Enter number of elements:"))
    elements = set()
    for i in range(0,num_elements):
        element = int(input("Enter the element "+str(i)+" :"))
        elements.add(element)
    return elements

#Given two sets check whether one of them is a subset of the other
def check_is_subset(set1,set2):
   # print(set1.difference(set2))
    if len(set1.difference(set2)) == 0 or len(set2.difference(set1)) == 0:
        return True
    else:
        return False
    


print("This program checks whether one of the given two sets is one of the subsets of the other.")
set1 = take_input_set()
set2 = take_input_set()
if check_is_subset(set1,set2):
    print("YES")
else:
    print("NO")