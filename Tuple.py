
#1. Write a Python program to create a tuple.
'''s = tuple((1,2,3,4,3))
print(type(s))
print(s)
or 
x = 1,2,3,4,5,6,7,8,9
print(x)
print(type(x))'''

#2. Write a Python program to create a tuple with different data types.
'''
x = 1,2,3.4,'23',4.7
print(x)'''
#3. Write a Python program to create a tuple of numbers and print one item.
'''x = 1,2,3,4,5,6,7,8
print(x[4])'''
#4. Write a Python program to unpack a tuple into several variables.
'''x = (12,3,4,5,6,7)
a,b,c,d,e,f = x
print(a,b,c,d,e,f)
'''
#5. Write a Python program to add an item to a tuple.
'''a = 1,2,3,4,5,6
b = 7,8
c = a+b
print(c)'''

#6. Write a Python program to convert a tuple to a string.
'''a = 1,2,3,4,5,6
b = str(a)
print(a)
print(type(b))'''

#7. Write a Python program to get the 4th element from the last element of a tuple.
'''a = 1,2,3,4,5,(3,5,6,7,7)
print(a)
print(a[5][4])
'''
#8. Write a Python program to create the colon of a tuple.

#9. Write a Python program to find repeated items in a tuple.
'''a = 1,2,3,4,5,1,23,4,2
b = set()
for i in a:
    if a.count(i)>1:
        b.add(i)
print(a)
print(b)'''

#10. Write a Python program to check whether an element exists within a tuple. 
'''a = 1,2,3,4,5,6
element = 41
c=0
for i in a:
    if element == i:
        c+=1
if c>0:
    print("exist")
else:
    print("doesn't exist")'''

#11. Write a Python program to convert a list to a tuple.
'''l = [1,2,3,4,5,56,6,3]
s = tuple(l)
print(type(s))
print(s)'''

#12. Write a Python program to remove an item from a tuple.
'''t = 1,2,3,4,5
print(t)
li = list(t)
print(li)
li.remove(3)
print(li)
t= tuple(li)
print(t)
print(type(t))'''
'''
'''
#13. Write a Python program to slice a tuple.
'''t = 1,2,3,4,56,7,87
print(t[0:4:2])'''

#14. Write a Python program to find the index of an item in a tuple.
'''t = 12,23,3,4,5,6,7,8
print(t)
s = 5
print(t.index(s))'''


#15. Write a Python program to find the length of a tuple.
'''t = 1,2,3,5,6,7,8
s = len(t)
print(s)
'''
#16. Write a Python program to convert a tuple to a dictionary.
'''a = (1,2,3,4,5,6,7,8,9)
b = {i:i**3 for i in a}
print('tuple:',a)
print('dictionary:',b)'''


#17. Write a Python program to unzip a list of tuples into individual lists.
'''a = (1,2,3,4,5),(9,8,7,6,5,4),(12.3,3,4,5,5)
x,y,z = a
print(x)
print(y)
print(z)'''

#18. Write a Python program to reverse a tuple.
'''t = 1,2,3,4,5,6,7,8
print(t)
print('reverse', t[::-1])'''

#19. Write a Python program to convert a list of tuples into a dictionary.
'''a = 1,2,3,4,5
b = 'one','two','three','four'
c = {i:j for i in a for j in b}
print('tuple: ',a)
print('tuple: ',b)
print('dictionary: ',c)'''
#20. Write a Python program to print a tuple with string formatting.
'''Sample tuple : (100, 200, 300)
Output : This is a tuple (100, 200, 300)

a = 100, 200, 300
print(f'This is a tuple {a}')'''


#21. Write a Python program to replace the last value of tuples in a list.
'''Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
a = (10, 20, 40), (40, 50, 60), (70, 80, 90)
b = []
for i in a:
    c = list(i)
    c[2]=100
    b.append(tuple(c))
print(b)
'''

#22. Write a Python program to remove an empty tuple(s) from a list of tuples.
'''l = [( ), (''), (1,2,4), ('a','b','c'),( ), ('one')]
print(l)
for i in l:
    if len(i)<1:
        l.remove(i)
print(l)'''

#23. Write a Python program to sort a tuple by its float element.
'''l = [(1, 3.0), (2, 1.5), (3, 2.5), (4, 1.0)]
print('unsorted list: ',l)
l.sort(reverse=True)
print('Sorted list: ',l)'''


#24. Write a Python program to count the elements in a list until an element is a tuple.
'''l = [1,2,3,(4,5,6),7,8,9]
c = 0
i = 0
while type(l[i]) != type(l[3]):
    c+=1
    i+=1
print(l)
print('count: ', c)'''
#25. Write a Python program to convert a given string list to a tuple.
'''a = 'pooja'
b = []
for i in a:
    c = tuple(i)
    b.append(c)
print(a)
print(b)'''
#26. Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
'''Original Tuple:
(4, 3, 2, 2, -1, 18)
Product - multiplying all the numbers of the said tuple: -864
Original Tuple:
(2, 4, 8, 8, 3, 2, 9)
Product - multiplying all the numbers of the said tuple: 27648'''
'''a = 2, 4, 8, 8, 3, 2, 9
m = 1
for i in a:
    m*=i
print(a)
print('multiplication: ',m)'''

#27. Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
'''Original Tuple:
((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
Average value of the numbers of the said tuple of tuples:
[30.5, 34.25, 27.0, 23.25]
Original Tuple:
((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
Average value of the numbers of the said tuple of tuples:
[25.5, -18.0, 3.75]'''

'''x = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
avg_li = []
for i in range(len(x)):
    li = []
    for j in range(len(x)):
        li.append(x[j][i])
    s = sum(li)
    avg = s/len(x[i])
    avg_li.append(avg)
print('list: ',x)
print('avg: ',avg_li)'''

#28. Write a Python program to convert a tuple of string values to a tuple of integer values.
'''a = (('333', '33'), ('1416', '55'))
b = []
for i in a:
    li = []
    for j in i:
        li.append(int(j))
    b.append(tuple(li))
print('string: ', a)
print('integer: ', tuple(b))
'''
#29. Write a Python program to convert a given tuple of positive integers into an integer.
'''Original tuple:
(1, 2, 3)
Convert the said tuple of positive integers into an integer:
123
Original tuple:
(10, 20, 40, 5, 70)
Convert the said tuple of positive integers into an integer:
102040570'''
'''s = 1,2,3
a,b,c = s
n = str(a)+str(b)+str(c)
print(s)
print(n)
'''
#30. Write a Python program to check if a specified element appears in a tuple of tuples.
'''a = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
b = 'White'
print(a)
for i in a:
    if b in i:
        print('True')
    else:
        print(' False')'''



#31. Write a Python program to compute the element-wise sum of given tuples.
'''Original lists:
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)
Element-wise sum of the said tuples:
(6, 9, 8, 6)'''


'''a = ((1, 2, 3, 4),(3, 5, 2, 1),(2, 2, 3, 1))
t = []
for i in range(len(a[0])):
    li = []
    for j in range(len(a)):
        li.append(a[j][i])
    s = sum(li)
    t.append(s)
print(a)
print('element wise sum: ', tuple(t))'''




#32. Write a Python program to compute the sum of all the elements of each tuple stored inside a

'''#list of tuples.
#Original list of tuples:
#[(1, 2), (2, 3), (3, 4)]
#Sum of all the elements of each tuple stored inside the said list of tuples:
#[3, 5, 7]
#Original list of tuples:
#[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
#Sum of all the elements of each tuple stored inside the said list of tuples:
#[9, -1, 7, 8]'''
'''a = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
t = []
for i in a:
    s = 0
    for j in i:
        s+=j
    t.append(s)
print(a)
print('sum of tuples: ', t)
'''
#33. Write a Python program to convert a given list of tuples to a list of lists.
#Original list of tuples: [(1, 2), (2, 3), (3, 4)]
#Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
#Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
#Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]
'''a = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
b = []
for i in a:
    b.append(list(i))
print('list of tuples: ',a)
print('list of lists: ', b)
'''

