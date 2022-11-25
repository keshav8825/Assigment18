#. Write a python program to get a list of the values from a dictionary.

data = {'keshav': [{'sub1': "java", 'marks': 98}, 
                   {'sub2': "PHP", 'marks': 89}],
        'ravi': [{'sub1': "java", 'marks': 78}, 
                  {'sub2': "PHP", 'marks': 79}]}
  
# get the list of data
# using items() method
for key, values in data.items():
    for i in values:
        print(key, " : ", i)