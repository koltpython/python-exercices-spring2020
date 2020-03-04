"""
Input a string and an integer k.
Divide string into k pieces.
Remove one duplicates until the piece consists of distinct letters.
Print the each piece after this process.

"""
#Divides a string into num_pieces piece
#Hint: Use slicing string such that each slice will have len(string)/num_pieces characters
def divide_string(string,num_pieces):
    pieces = list()
    for i in range(0,len(string)-num_pieces+1,len(string)//num_pieces):
        pieces.append(string[i:i+num_pieces])
    return pieces
#Removes repeated letters until the piece consists of only distinct characters
def remove_duplicates(pieces):
    new_pieces = list()
    for piece in pieces:
        new_piece = ""
        for char in piece:
            if not char in new_piece:
                new_piece+=char
        new_pieces.append(new_piece)
    return new_pieces

string = input("Enter a string:")
k = int(input("Number of pieces: "))
pieces = divide_string(string,k)
results = remove_duplicates(pieces)
for i in results:
    print(i)
    