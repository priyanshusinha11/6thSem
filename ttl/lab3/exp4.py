#implementing lambda,map,filter and sorted funtions

print("---Lambda Functions---")
print("Enter two numberss:")
n = float(input())
m = float(input())
div = lambda x, y: x / y if y != 0 else "Cannot divide by zero"
print(div(n,m))

print("---Map function---")
def addition(n):
    return n + n
print("Enter 4 numbers:")
nums = []
for i in range(4):  
    num = int(input()) 
    nums.append(num)  
nums = tuple(nums)
res = map(addition, nums)
print("Double of the numbers entered:")
print(list(res))

print("---Filter function---")
def fun(letter):
    letters = ['a','e','i','o','u']
    if (letter in letters):
        return True
    else:
        return False
str = input("Enter a string:")
seq = list(str)
vowles = filter(fun, seq)
print('The vowels are:')
for s in vowles:
    print(s)

print("---Sorted Function---")
words = input("Enter words separated by spaces: ").split()
sorted1 = sorted(words, key=lambda x: len(x))
print("Sorted words (ascending):", sorted1)
sorted2 = sorted(words, key=lambda x: len(x), reverse=True)
print("Sorted words (descending):", sorted2)
