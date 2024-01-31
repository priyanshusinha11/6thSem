def isPalindrome(num):
    temp = num
    rev = 0
    while temp != 0:
        dig = temp % 10
        rev = (rev * 10) + dig
        temp = temp // 10 
    if rev == num:
        print(num,"is a plaindrome")
    else:
        print(num,"is not a palindrome")

num = int(input("Enter a number: "))
isPalindrome(num)