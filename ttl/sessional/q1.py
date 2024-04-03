x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
greater = lambda x, y: x if x > y else y
ans = greater(x, y)
print("Greater among two numbers =", ans)
