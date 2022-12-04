a=input("Enter the character=")
if a.isalpha():
    print("it is a alphabet")
    if a.isupper():
        print("All are uppercase")
    else:
        print("It is a lower case")
elif a.isnumeric():
    print("It is a number")
    def printValue(digit):
        if digit == '0':
            print("Zero ", end=" ")
        elif digit == '1':
            print("One ", end=" ")
        elif digit == '2':
            print("Two ", end=" ")
        elif digit == '3':
            print("Three", end=" ")
        elif digit == '4':
            print("Four ", end=" ")
        elif digit == '5':
            print("Five ", end=" ")
        elif digit == '6':
            print("Six ", end=" ")
        elif digit == '7':
            print("Seven", end=" ")
        elif digit == '8':
            print("Eight", end=" ")
        elif digit == '9':
            print("Nine ", end=" ")
    def printWord(a):
        i = 0
        length = len(a)
        while i < length:
            printValue(a[i])
            i += 1
    printWord(a)
elif a.isalnum():
    print("It has both alphabets and numbers")
else:
    print("it is a special character")
