
nums = (1, 2, 3, 4, 5)

print("Element at index 0:", nums[0])
print("Element at index 2:", nums[2])

nums2 = (6, 7, 8)
nums3 = nums + nums2
print("Concatenated tuple:", nums3)

nums4 = nums * 2
print("Repeated tuple:", nums4)

print("Length of the tuple:", len(nums))

print("Is 3 in the tuple?", 3 in nums)
print("Is 9 not in the tuple?", 9 not in nums)

print("Iterating through the tuple:")
for item in nums:
    print(item)

print("Sliced tuple from index 1 to 3:", nums[1:4])