#Q1 :: Create empty list "my_list"
my_list = []
#Q2 :: Append 10,20,30,40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#Q3 :: Insert value 15 at second position in lis
my_list.insert(1,15)
#Q4 :: Extend my_list with another list [50,60,70]
add_list = [50, 60, 70]
my_list.extend(add_list)
# Q5 :: Remove last element from the list
del my_list[-1]
# Q6 :: sort my_listin ascending order
my_list.sort()
print(my_list)

print(my_list.index(30))