def power(x, y, ans):
    if y == 0:
        return ans
    ans = ans * x
    return power(x, y - 1, ans)

x = int(input("Enter the first number: "))
y = int(input("Enter the second exponent: "))
ans = 1
ans = power(x, y, ans)  
print("Power =", ans)
