a=input("Enter the string=")

#to find frequency
print("frequency =",len(a),)
print(a)

#to replace elements
fake=list(a)
c=input("enter the character you want to replace=")
b=input("enter the character you want to replace with the present character=")
for i in range(len(fake)):
    if a[i]==c:
        fake[i]=b
print(" ".join(fake))

#To remove 1st occurence
fool=list(a)
d=input("enter the character you want to remove=")
fool.remove(d)
print(" ".join(fool))


#To remove all occurence
chandu=list(a)
y=input("enter the character you want to remove=")
for i in range(len(chandu)):
    if str(chandu[i])==y:
        chandu.remove(i)
print(chandu)