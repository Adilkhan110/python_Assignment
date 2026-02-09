user = input("Enter the String: ")
vowels = "aeiou"
length = len(user)
if user[0].isalpha() and user[0] not in vowels:
    if user[-1].isdigit():
        mid = len(user) //2
        f_h = user[:mid]
        s_h = user[mid:]
        print("First Half: ", f_h[::-1] + s_h)
    else:
        mid = len(user) // 2
        f_h = user[:mid]
        s_h = user[mid:]
        print("Second Half: ", f_h + s_h[::-1])
else:
    jls_extract_var = ""
    print("Without Space String:", user.replace(" ", jls_extract_var))

# 1       Input
# Enter the String: Hello World

#         Output
# First Half:  olleH World

# 2       Input
# Enter the String: Python3

#         Output
# Second Half:  Pytho3n

# 3       Input
# Enter the String: 12345

#         Output
# Without Space String: 12345

