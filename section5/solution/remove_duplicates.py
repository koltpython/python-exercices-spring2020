"""
Input a string and an integer k.
Divide string into k pieces.
Remove one duplicates until the piece consists of distinct letters.
Print the each piece after this process.
"""


def divide_string(string, num_pieces):
    len_str = len(string)
    short_len = len_str // num_pieces
    long_len = short_len + 1
    num_long_pieces = len_str % num_pieces
    pieces = []
    num_short_pieces = num_pieces - num_long_pieces
    for i in range(num_short_pieces):
        pieces.append(string[short_len * i:short_len * (i + 1)])

    for i in range(num_long_pieces):
        pieces.append(string[(num_short_pieces * short_len) + i *
                             long_len:(num_short_pieces * short_len) + (i + 1) * long_len])

    return pieces


# Removes repeated letters until the piece consists of only distinct characters
def remove_duplicates(pieces):
    new_pieces = []
    for piece in pieces:
        new_piece = ""
        for char in piece:
            if char not in new_piece:
                new_piece += char
        new_pieces.append(new_piece)
    return new_pieces


string = input("Enter a string:")
k = int(input("Number of pieces: "))
pieces = divide_string(string, k)
results = remove_duplicates(pieces)
for result in results:
    print(result)
