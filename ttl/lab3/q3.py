def isPerfect(num):
    sum = 0
    for i in range(1,num-1):
        if num%i == 0:
            sum += i
    if sum == num:
        print(num,"is a perfect number")
    else:
        print(num,"is not a perfect number")

num = int(input("Enter a number:"))
isPerfect(num)