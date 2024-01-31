def isNelson(num):
    dig = num%10
    temp=num
    flag = 0
    while(num):
        dig2 = num%10
        if dig != dig2:
            flag += 1
        num = num//10
    if flag == 0:
        print(temp,"is a Nelson number")
    else:
        print(temp,"is not a Nelson number")

num = int(input("Enter a number:"))
isNelson(num)
