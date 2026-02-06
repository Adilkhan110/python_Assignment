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
    print("Without Space String: ", user.replace(" ",""))