set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Set1 and set2 are:",set1,set2)
set3 = set1.union(set2)
print("Union of set1 and set2:", set3)

set4 = set1.intersection(set2)
print("Intersection of set1 and set2:", set4)

set5 = set1.difference(set2)
print("Difference between set1 and set2:", set5)

set6 = set2.difference(set1)
print("Difference between set2 and set1:", set6)
