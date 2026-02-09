user = input("Enter the String: ")
length = len(user)
if length > 6 < 12:
    if user[0] == user[-1]:
        print("The first and last characters are the same:", " The 01:", user[0], " The 02:", user[-1])
    elif " " in user:
        print("First Word is: ", user.split()[0])
    else:
        print("alternate characters: ", user[::2])
else:
    print(user[::-1])

# 1       Input
# Enter the String: Hello World

#         Output
# First Word is:  Hello

# 2       Input
# Enter the String: Python

#         Output
# alternate characters:  Pton

# 3       Input
# Enter the String: abcdefghijkl

#         Output
# The first and last characters are the same:  The 01: a  The 02: l

# 4       Input
# Enter the String: abcdef

#         Output
# fedcba