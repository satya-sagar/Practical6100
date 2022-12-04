a=input("Emter the 1st string=")
b=input("Enter the 2nd string=")
chandu=list(a)
chandi=list(b)
c=int(input("Enter the n numbers of characters="))
chandu[0:c],chandi[0:c]=chandi[0:c],chandu[0:c]
print(" ".join(chandu))
print(" ".join(chandi))