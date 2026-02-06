user = input("Enter the String: ")
length = len(user)
if length > 6 < 12:
    if user[0] == user[-1]:
        print("excluding the first and last character is Same: ", user[0::-1])
    elif " " in user:
        print("First Word is: ", user.split()[0])
    else:
        print("alternate characters: ", user[::2])
else:
    print(user[::-1])