def isPrime(num):
    flag = 0
    for i in range(2,num):
        if(num%i == 0):
            flag+=1
    if(flag == 0):
        print(num,"is a prime number")

for i in range(3,100):
    isPrime(i)