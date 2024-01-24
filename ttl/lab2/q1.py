# greates among three
print("Enter three numbers:")
a = int(input())
b = int(input())
c = int(input())
if a>b and a>c:
    print("The greatest is: ",a)
elif b>c and b>a:
    print("The greatest is: ",b)
else:
    print("The greatest is: ",c)