# create an empty list
my_list = []

# append
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert 15 at index 1
my_list.insert(1, 15)

# extended list with 50, 60, 70
my_list.extend([50, 60, 70])

# remove the last element with 'pop'
my_list.pop()

# ascending order - sorting
my_list.sort()

# final output
print(my_list)

# print the index of 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

