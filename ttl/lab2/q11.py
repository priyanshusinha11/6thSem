def isArmStrong(num):
    temp = num
    cnt = 0
    while temp != 0:
        temp = temp // 10
        cnt += 1
    temp = num
    sum = 0
    while temp != 0:
        sum += (temp % 10) ** cnt
        temp = temp // 10
    if sum == num:
        print(num, "is an Armstrong number")

for i in range(100,1000):
    isArmStrong(i)