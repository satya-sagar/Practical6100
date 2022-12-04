a=input("Enter the character=")
if a.isalpha():
    print("it is a alphabet")
elif a.isnumeric():
    print("It is a number")
elif a.isalnum():
    print("It has both alphabets and numbers")
else:
    print("it is a special character")
