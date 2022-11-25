''' Write a python program to convert two lists into a dictionary in a way that item from
list1 is the key and item from list2 is the value'''

l1={1,2,3,4,5}
l2={'CPU','mouse','moniter','keyboard','headphone'}

final_dict = {l1[i]:l2[i] for i in range(len(l1))}
print(final_dict)
