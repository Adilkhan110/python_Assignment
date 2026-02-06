user = input("Enter the String: ")
length = len(user)
if length > 5:
    mid = length //2
    first = user[:mid]
    second = user[mid:]
    if first == second[::-1]:
        print("Palindrome Half")
    elif user.isupper():
        result = user
        result = result.replace("A", "")
        result = result.replace("E", "")
        result = result.replace("I", "")
        result = result.replace("O", "")
        result = result.replace("U", "")
        print(result)
    else:
        twice, = second + first
        print(twice,)
else:
    modified=user[1:]
    print(modified+modified)