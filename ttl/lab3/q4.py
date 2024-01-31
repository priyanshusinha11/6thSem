def isPrimeNum(num):
    if num <= 1:
        print(num, "is not a prime number")
        return
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            return

    print(num, "is a prime number")

num = int(input("Enter a number: "))
isPrimeNum(num)
