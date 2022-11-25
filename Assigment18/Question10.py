'''. Write a python program to get the key of lowest value from the dictionary.
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}'''

sample_dict = {'c':92,'java':66,'python':85}
temp = min(sample_dict.values())

for key in sample_dict:
    if sample_dict[key] == temp:
        print(key)
print( )
        