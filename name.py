# Declaring an empty List

from itertools import count


list1 =[]

# A list of Numbers

list1 =[99,90,95,96,92]

print(list1)

print(type(list1))

# Length of the list

print(len(list1))

#  A list Of Strings

list2 =[]

list2 =["WhiteHatjr","coding","classes"]

print(list2)

print(len(list2))

#positive Index  starts from 0 at the beginning of  the list

# negative index starts from -1 at the end of the list


# Index of an element
print(list1.index(99))

print(list1.index(96))

# Accessing list elements using positve index

print(list1[0])

print(list2[2])

# Accessing list elements using negative index

print(list1[-1])

print(list2[-1])

# Accessing list element using Slice Operator

print(list1[0:2])

print(list2[0:2])

print(list1[0:5])

# Slice Operator With Negative Index

print(list1[-5:-3])

# Accessing list element using For Loop

for elem in list1:
    print(elem)

for elem in list2:
    print(elem)


# Range of numbers

range(0,5)
print(range(0,5))

for i in range(0,5):
    print(i)

for i in range(0,5,2):
    print(i)

for i in range(5,0,-1):
    print(i)   


# COUNT the occurance of a given element in the list

# [75, 98, 89, 86, 79, 62, 78, 61, 90, 97, 92, 61, 64, 97, 82, 69, 87, 96, 65, 75, 85, 76, 95, 83, 62, 80, 80, 77, 94, 71, 86, 94, 85, 99, 77, 68, 92, 91, 99, 90]
list3 =[]
list3 = [75, 98, 89, 86, 79, 62, 78, 61, 90, 97, 92, 61, 64, 97, 82, 69, 87, 96, 65, 75, 85, 76, 95, 83, 62, 80, 80, 77, 94, 71, 86, 94, 85, 99, 77, 68, 92, 91, 99, 90]

count = 0

check_num = 62

for elem in list3:
  if (check_num == elem):
    count = count + 1

print(count)