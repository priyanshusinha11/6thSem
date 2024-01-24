#palindrome
print("Enter the number:")
num = int(input())
temp = num
rev = 0
while temp != 0:
    dig = temp % 10
    rev = (rev * 10) + dig
    temp = temp // 10 
print("Reverse of the number:", rev)
if rev == num:
    print(num,"is a plaindrome")
else:
    print(num,"is not a palindrome")
