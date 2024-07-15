'''


Q1.

Create a Car class with encapsulated attributes to represent information about a car. The class should have the following attributes: make (string), model (string), year (integer), and mileage (float). Implement appropriate methods to retrieve and update each attribute while incorporating validation checks. Additionally, demonstrate how encapsulation principles are applied to restrict direct access to these attributes.

1. Implement the __init__ method to initialize the Car object with the specified attributes. Ensure that the year is a positive integer and the mileage is a non-negative float.
2. Write methods (get_make, get_model, get_year, get_mileage) to retrieve the values of the attributes.
3. Write methods (set_make, set_model, set_year, set_mileage) to update the values of the attributes. Include validation checks to ensure the correctness of the assigned values (e.g., valid make and model strings, positive integer year, non-negative float mileage).
4. Create an instance of the Car class and demonstrate how to use the implemented methods to interact with the object, emphasizing encapsulation.


Q2.

Create a BankAccount class to represent a simple bank account. The class should have encapsulated attributes: account_number (string), account_holder (string), balance (float). Implement appropriate methods to retrieve and update each attribute while incorporating validation checks. Additionally, demonstrate how encapsulation principles are applied to restrict direct access to these attributes.

1. Implement the __init__ method to initialize the BankAccount object with the specified attributes. Ensure that the account_number is a unique string, account_holder is a non-empty string, and balance is a non-negative float.
2. Write methods (get_account_number, get_account_holder, get_balance) to retrieve the values of the attributes.
3. Write methods (set_account_holder, set_balance, deposit, withdraw) to update the values of the attributes. Include validation checks to ensure the correctness of the assigned values (e.g., valid account holder name, non-negative float balance).
4. Create an instance of the BankAccount class and demonstrate how to use the implemented methods to interact with the object, emphasizing encapsulation.

Q3.

 Create a Student class to represent information about a student. The class should have encapsulated attributes: student_id (string), name (string), age (integer), and grade (float). Implement appropriate methods to retrieve and update each attribute while incorporating validation checks. Additionally, demonstrate how encapsulation principles are applied to restrict direct access to these attributes.

1. Implement the __init__ method to initialize the Student object with the specified attributes. Ensure that the student_id is a unique string, name is a non-empty string, age is a positive integer, and grade is a float between 0 and 100.
2. Write methods (get_student_id, get_name, get_age, get_grade) to retrieve the values of the attributes.
3. Write methods (set_name, set_age, set_grade) to update the values of the attributes. Include validation checks to ensure the correctness of the assigned values (e.g., valid name, positive integer age, float grade within range).
4. Create an instance of the Student class and demonstrate how to use the implemented methods to interact with the object, emphasizing encapsulation.

'''
#1. Write a Python script to sort (ascending and descending) a dictionary by value. 
'''dict = {'three':3,'four': 4, 'one': 1, 'two':2, 'three':3}

dict1 = {}
dict1 = sorted(dict.values())
print(dict1)
for key, value in dict1.items():
    print(key,value)
dict2 = {}
dict2 = sorted(dict.values(), reverse=True)
print(dict2)
for key, value in dict2.items():
    print(key,value)'''
'''x ={'three':3,'four': 4, 'one': 1, 'two':2, 'three':3}

print(sorted(x.values()))

print(sorted(x.values(), reverse=True))'''
#2. Write a Python script to add a key to a dictionary. Sample Dictionary : {0: 10, 1: 20} Expected Result : {0: 10, 1: 20, 2: 30}
'''x = {0: 10, 1: 20}
x.update({2:30})
print(x)'''
#3. Write a Python script to concatenate the following dictionaries to create a new one. 

#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}

dict4 = {**dict1 , **dict2 , **dict3}
print(dict4)'''

#1. Write a Python program to create a set.

'''s = set({2,3,4,5,6,7,7,8})
print(s)
'''
#2. Write a Python program to iterate over sets.

'''s = set({12,34,45,6,6,89,45})
for i in s:
    print(i)
'''
#3. Write a Python program to add member(s) to a set.
'''s = set({12,34,45,6,6,89,45})
s.add(780)
print(s)
'''
#4. Write a Python program to remove item(s) from a given set.

'''s = set({12,34,45,6,6,89,45})
s.remove(12)
print(s)
'''
#5. Write a Python program to remove an item from a set if it is present in the set
'''s = set({1,2,3,4,5,3,2,12,5,7,7,9,0,7,7,5,3})
s1 = 5  
s.remove(s1)
print(s) 
 
'''
#6. Write a Python program to create an intersection of sets.
'''s = {1,2,3,5,6,8,9}
s1 = {2,5,6,7,8,9,4,2,13}
s2 =s.intersection(s1)
print(s2)'''
#7. Write a Python program to create a union of sets.
'''s = {1,2,3,5,6,8,9}
s1 = {2,5,6,7,8,9,4,2,13}
s2 = s.union(s1)
print(s2)'''
'''
1## print the pattern##
*
**
***
****
*****

2## Printing the pattern ##
*****
**** 
***  
**   
*   

3## Printing the pattern ##
    *
   **
  ***
 ****
*****'''

'''i = 1
while i<=5:
    j = 1
    while j<=i:
        print('*', end=' ') # line break
        j+=1
    print(" ")
    i+=1'''
'''i = 1
while i<=5:
    j = 5
    while j<=i:
        print('*', end=' ') # line break
        j+=1
    print(" ")
    
    while j>=i:
        print('*', end=' ') # line break
        j-=1
    print(" ")
    i+=1'''
'''i = 1
while i<=5:
    j = 5
    while j>=i:
        print(' ', end=' ') # line break
        j-=1
    j = 1
    while j<=i:
        print('*', end=' ') # line break
        j+=1  
    print(" ")
    i+=1'''