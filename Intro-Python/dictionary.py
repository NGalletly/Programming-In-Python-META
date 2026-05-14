'''
#Dictionaries have key:value pairs; 

'''

sample_dict = {1: 'Coffee', 2: "tea", 3: "juice"}

sample_dict[2] = "Mint tea"
print(sample_dict)


sample_dict2 = {"one": 'Coffee', "two": "tea", "three": "juice"}

print(sample_dict2)

# del function to delete from dictionary
del sample_dict2["three"]

print(sample_dict2)

my_d = {1:"test"}

print(type(my_d))

# you Can add to a dictionary
my_d["new_key"] = "new_value"

print(my_d)

#iterate 

for x in my_d:
    print(x)

#You can iterate over keys & values with .items 
for key, value in my_d.items():
    print(str(key) + " : " + str(value))
