"""
Input:
Number of tuples: n => integer
2 elements for each tuple => both will be integers

Output:
Print the multiplication of elements in each tuple
"""
# It should take the number of tuples as input from the user and then for each tuple
# it should input two integers and create a tuple with them. It returns a list of
# tuples.


def input_tuple():
    n = int(input("Enter the number of tuples."))
    tuples = list()
    for i in range(0, n):
        first_element = int(
            input("First element " + "tuple number " + str(i) + " :"))
        second_element = int(
            input("Second element " + "tuple number " + str(i) + " :"))
        tuples.append((first_element, second_element))
    return tuples

# takes a tuple-list as parameter and prints the multiplication of the elements in each tuple in the list


def print_multiplication(tuples):
    for i in tuples:
        print(i[0] * i[1])


print("This program takes a list of tuples with two elements from user and prints the multiplication of the elements in each tuple.")
tup = input_tuple()
print_multiplication(tup)
