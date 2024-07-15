
#1. Write a Python script to sort (ascending and descending) a dictionary by value. 

'''x = {'pooja':12,"s":13,'a':23,'we':231}

print(sorted(x.values()))

print(sorted(x.values(), reverse=True))'''

#2. Write a Python script to add a key to a dictionary. 

#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}

'''age ={'pooja':25,'gaurav':24,'sumit':18}
print(age)

age.update({'poojaa':32,'gaurava':31})
print(age)'''
#3. Write a Python script to concatenate the following dictionaries to create a new one. 

#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dict4 = {** dic1,**dic2,**dic3}
print(dict4)
'''
#4. Write a Python script to check whether a given key already exists in a dictionary. 
#check that particular item is present or not
'''age ={'pooja':25,'gaurav':24,'sumit':18}
print(age)
k='sumittt'
if k in age.keys():
    print("item found")
else:
    print("not found")'''
#5. Write a Python program to iterate over dictionaries using for loops. 
'''dict = {'a':1, 'b':7, 'c':9, 'd':2, 'e':5}
print(dict)
for i,j in dict.items():
    print(i,j ,end = " ")'''
#6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
#Sample Dictionary ( n = 5) :
#Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''dict = {x: x *x for x in range(1,6)}
print(dict)'''
#7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the 
#values are the square of the keys. 
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
'''dict = {x: x **2 for x in range(1,16)}
print(dict)'''
#8. Write a Python script to merge two Python dictionaries. 
'''d ={'a':1,"b":2,'c':12}
e = {'e':12,"h":123,'f':12}
h = {**d,**e}
print(h)'''
#9. Write a Python program to iterate over dictionaries using for loops. 
'''d ={'a':1,"b":2,'c':12}
for i, j in d.items():
    print(i,j)'''

#10. Write a Python program to sum all the items in a dictionary. 
'''d ={ 'a':1,"b":2,'c':12 }
d1 = (sum(d.values()))
print(d1)'''