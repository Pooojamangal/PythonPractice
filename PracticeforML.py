'''1.take input in constructor and display in method, print frequency of each character of String.

2.take input in constructor and display in method, remove most repeated char from string.

3. Write a Python script to sort (ascending and descending) a dictionary by value. 


4. Write a Python script to add a key to a dictionary. 

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}



5. Write a Python script to concatenate the following dictionaries to create a new one. 

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

Q1
         A
       B A B
     C B A B C
   D C B A B C D
 E D C B A B C D E

Q2
a
B c
D e F
g H i J
k L m N o'''
#1.take input in constructor and display in method, print frequency of each character of String.

'''class Frequency:
    def __init__(self):
        String1 = input("Enter String: ")
        String = String1.lower()
        freq ={ }
        self.String = String
        self.freq = freq

    def Frequency_Of_Character(self):
        for i in self.String:
            if i in self.freq:
                self.freq[i] +=1
            else:
                self.freq[i] = 1
        print(self.freq)
F = Frequency()
F.Frequency_Of_Character()'''

#2.take input in constructor and display in method, remove most repeated char from string.

'''class Frequency:
    def __init__(self):
        String1 = input("Enter String: ")
        String = String1.lower()
        freq ={ }
        self.String = String
        self.freq = freq

    def Frequency_Of_Character(self):
        for i in self.String:
            if i in self.freq:
                self.freq[i] +=1
            else:
                self.freq[i] = 1
        print(self.freq)
    def Remove_Most_Repeated(self):
        def get_value(item):
            return item[1]

        sorted_items = sorted(self.freq.items(), key=get_value)
        sorted_dict= dict(sorted_items)
        print(" Frequency of Characters: ", self.freq)
        sorted_dict.popitem()
        print("Removed most repeated character:", sorted_dict)
    
    
      
F = Frequency()
F.Frequency_Of_Character()
F.Remove_Most_Repeated()'''
'''
class Frequency:
    def __init__(self):
        String1 = input("Enter String: ")
        String = String1.lower()
        freq ={ }
        self.String = String
        self.freq = freq

    def Frequency_Of_Character(self):
        for i in self.String:
            if i in self.freq:
                self.freq[i] +=1
            else:
                self.freq[i] = 1
        print(self.freq)
    def Remove_Most_Repeated(self):
        
        most_repeated = max(self.freq.items(), key=self.freq.items())
    
   
        Removed = self.string.replace(most_repeated, '')
    
        print(Removed)
      
F = Frequency()
F.Remove_Most_Repeated()'''
#3. Write a Python script to sort (ascending and descending) a dictionary by value.

'''my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
def get_value(item):
    return item[1]

sorted_items_asc = sorted(my_dict.items(), key=get_value)
sorted_dict_asc = dict(sorted_items_asc)

sorted_items_desc = sorted(my_dict.items(), key=get_value, reverse=True)
sorted_dict_desc = dict(sorted_items_desc)

print("Original dictionary:", my_dict)
print("Dictionary sorted asc:", sorted_dict_asc)
print("Dictionary sorted desc:", sorted_dict_desc)

'''
#4. Write a Python script to add a key to a dictionary. 
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}
'''dict = {0: 10, 1: 20}
print(dict)
dict.update({2: 30})
print(dict)
'''
#5. Write a Python script to concatenate the following dictionaries to create a new one. 

#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dict4 ={**dic1,**dic2,**dic3}
print(dict4)'''

'''
         A
       B A B
     C B A B C
   D C B A B C D
 E D C B A B C D E
 Sure, here is a step-by-step approach to help you think through solving the problem:

1. **Analyze the Pattern**:
   - Identify how many rows there are.
   - Observe how many leading spaces each row starts with.
   - Notice the sequence of characters in each row, both in ascending and descending order.

2. **Break Down the Rows**:
   - Determine how the number of spaces decreases as the row number increases.
   - Determine how the characters are arranged, starting with the middle character and moving outwards.

3. **Set Up the Character Calculation**:
   - Use the ASCII value to get the character you need. The ASCII value for 'A' is 65. 
   - Understand how the characters change for each row.

4. **Loop Structures**:
   - Use a loop to iterate through each row.
   - Within each row, use a nested loop to handle the leading spaces.
   - Use another nested loop to handle the characters in the row, first in descending order then in ascending order.

5. **Increment and Print**:
   - Ensure you correctly increment the starting character for each row.
   - Print the characters without moving to the next line until the entire row is constructed.
   
6. **Combine Everything**:
   - Put all these loops together to form the final pattern.

7. **Test Your Logic**:
   - Before coding, write down how your loops would work on paper.
   - Manually check if the logic matches the expected output for a few rows.

Following these steps will guide you in constructing the pattern step-by-step.
         A
       B A B
     C B A B C
   D C B A B C D
 E D C B A B C D E
'''
'''i = 1
k=65
while i <=5:  
    j = i
    while j<=5:
        print(" " , end = ' ' )
        j+=1  
    j=1
    k1=k
    while j<=i:
        print(chr(k1),end=" ")
        j+=1
        k1-=1
    k+=1
    j=2
    k2=66  
    while j<=i:
        print(chr(k2),end=" ")
        j+=1
        k2+=1
    print()
    i+=1'''
'''
a
B c
D e F
g H i J
k L m N o
'''
k = 97  # ASCII value for 'a'
for i in range(1, 6):
    for j in range(1, i*2, 2):
        if i % 2 == 1:  # Odd rows (1, 3, 5)
            print(chr(k), end=' ')
            k += 1
        else:  # Even rows (2, 4)
            print(chr(k).upper(), end=' ')
            k += 1
    print()

    


