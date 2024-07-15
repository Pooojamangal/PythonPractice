'''1. Write a Python function to sort a dictionary by its keys.
2. Create a function to sort a dictionary by its values.
3. Implement a function to update a specific key-value pair in a dictionary.
4. Write a Python program to check if a particular key exists in a dictionary.
5. Develop a function to merge two dictionaries using the update method.
6. Create a Python program to merge multiple dictionaries using the **kwargs technique.
7. Write a function to generate a dictionary containing squares of even numbers from a given list.
8. Implement a Python script to access a nested dictionary value using a specified key.
9. Write a function to iterate through a nested dictionary and print its key-value pairs.
10. Develop a program that takes two dictionaries as input and returns a new dictionary containing the
common keys with their sum of values
11. Write a Python function to find the difference between two dictionaries.
d1 = {'one':1,'two':2,'three':3}
d2 = {'three':3,'ten':10,'one':1}
d3 = { }
print(d1,d2)
for i  in d1:
    if i not in d2:
        d3[i] = d1[i]
for i in d2:
    if i not in d1:
        d3[i] = d2[i]
print(d3)
12. Implement a program to remove a specific key from a dictionary.d1 = {'one':1,'two':2,'three':3,'three':3,'ten':10,'one':1}
print(d1)
d2 = d1.pop('one')
print(d1)

13. Develop a function to find the maximum value in a dictionary and return its corresponding key.
14. Write a Python script to count the frequency of each element in a dictionary.
15. Create a program to merge two dictionaries such that the values of common keys are concatenated into a list.'''

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 4, 'c': 5, 'd': 6}
d3 = {}
print(d1,d3)
for key, value in d1.items():
 d3[key] = [value]

for key, value in d2.items():
    if key in d3:
        d3[key].append(value)
    else:
        d3[key] = [value]
print(d3)


    
    
        

