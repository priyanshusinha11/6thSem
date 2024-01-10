str1 = "Soumya Ranjan Nayak"
str2 = ''.join(word[0].upper() for word in str1.split())
str3 = str1.split()[-1]
print(str2)
print(f"{str2[0]}.{str2[1]}. {str3}")
print(f"{str3} {str2[:2]}")
str4 = "hello"
print(str4[0])
print(str4[1])
print(str4[2])
print(str4[3])
print(str4[4])