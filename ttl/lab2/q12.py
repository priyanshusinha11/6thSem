def isPalindrome(num):
    temp = num
    rev = 0
    while temp != 0:
        dig = temp % 10
        rev = (rev * 10) + dig
        temp = temp // 10 
    if rev == num:
        print(num,"is a plaindrome")

for i in range(10,100):
    isPalindrome(i)