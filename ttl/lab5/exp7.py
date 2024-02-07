nums = [1, 2, 3, 4, 5]
print("Original nums:", nums)
nums.append(6)  
print("After adding element 6:", nums)

nums.remove(3) 
print("After removing element 3:", nums)

ind = 2
ele = nums[ind]
print(f"Element at ind {ind} is:", ele)

nums[0] = 10  
print("After modifying element at ind 0 to 10:", nums)

nums.insert(2, 7)  
print("After inserting element 7 at ind 2:", nums)

ind2 = 4
ele2 = nums.pop(ind2) 
print(f"Removed element at ind {ind2}:", ele2)
print("After removing element at ind 4:", nums)
