
Dict = {
    'name': 'Ram',
    'age': 30,
    'city': 'Delhi'
}

print("Name:", Dict['name'])
print("Age:", Dict['age'])
print("City:", Dict['city'])

Dict['gender'] = input("Enter the gender:")
print("Dictionary after adding gender:", Dict)

Dict['age'] = int(input("Enter updated age"))
print("Dictionary after updating age:", Dict)

print("Keys in the dictionary:", Dict.keys())

print("Values in the dictionary:", Dict.values())

if 'name' in Dict:
    print("'name' is present in the dictionary.")

ele = Dict.pop('city')
print("Removed value:", ele)
print("Dictionary after removing 'city':", Dict)
