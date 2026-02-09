user = input("Enter a string: ")
length = len(user)
if length > 8:
    first_half = user[:length // 2]
    second_half = user[length // 2:]
    if first_half == second_half:
        print("Mirror String")