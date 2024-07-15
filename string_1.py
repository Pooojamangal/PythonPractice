#1. Write a Python program that counts the number of characters in a given string.
'''s = 'Python is growing programming language'
print(s)
print(len(s), 'total chracters')
'''
#2. Create a program that takes a string input from the user and prints the last character of the string.
'''s = input("enter string")
print(s)
print("last chracter", s[-1])'''
#3. Write a program that iterates over a string and prints each character on a new line.
#4. Develop a program that takes a string from the user and prints only the characters present at even indices.
'''s = input("enter string")
print(s)
for i in range(len(s)):
    if i%2==0:
        print(i, s[i])'''
#5. Create a program that searches for a specific word in a given string and prints whether it's found or not.
'''s = 'poooja is my name'
print(s)
if 'pooja' in s:
    print("found")
else:
    print("not found")'''
#6. Write a program to slice a string from index 0 to 7 with a step size of 2.
'''s = 'python is a programming language'
print(s)
print(s[0:7:2])'''
#7. Develop a program that takes a string from the user and prints the first 5 characters.
'''s = input("enter string")
print(s)
print(s[0:5])'''
#8. Write a program to print the characters of a string from index 9 onwards.
'''s = input("enter string")
print(s)
print(s[9:])'''
#9. Create a program to reverse a given string.
'''s = input("enter string")
print(s)
print(s[::-1])'''
#10. Develop a program that checks if a given string is a palindrome or not
'''s = input("enter string")
print(s)
rev = s[: : -1]
if rev==s:
    print("palindrome")
else:
    print('Not palindrome')
'''
'''11. Write a program that counts the number of vowels and consonants in a given string.




15. Create a program that checks if two strings are anagrams of each other'''
#12. Create a program that replaces all occurrences of a specific character in a string with another character.
'''s = 'poojapoojapoojamangalaamangal'
for i in s:
    if i == 'a':
        replace = s.replace('a','x')
print(replace)'''
#13. Write a program to check if a given string contains only alphabets or not.
'''s = 'pooja mangal 123'

if all(i.isalpha() for i in s):
    print("All characters are alphabets")
else:
    print("non alphabetic string")'''
#14. Develop a program that capitalizes the first letter of each word in a given string.

'''s ='pooja mangal python codenera'
x=' '
s1 = s.split()
for i in s1:
    x += i.title()
print(x)'''

#Functions in String
'''s = 'Python'
print(s.upper())
print(s)
a = 'PYTHON'
print(a.lower())
print(a)
a1 = '   python    '
print(len(a1))
a2 =a1.strip()
print(len(a2))
a = "python is a programming language,python is widely used, python , a python"
print(a)
b = a.replace('python','java')
print(b)
s = 'Python'
print(s.endswith("on"))
s = 'Python'
print(s.startswith("Py"))'''
#isupper()
'''s = "PYTHON"
print(s.isupper())'''
#islower()
'''s1 = "python"
print(s1.isupper())'''
#isdigit()
'''s = '123540'
print(s.isdigit())'''
#isalpha()
'''s='ajshdjk'
print(s.isalpha())'''
#isalnum()
'''s ="123abc"
print(s)
print(s.isalnum())'''
#isspace()
'''s = '     '
print(s)
print(s.isspace())'''
#Q1.Wap take a string from user and find the count of upper , lower, digit, white space.
'''s = input("enter the string")
print(s)
u =0
l=0
d=0
w =0
for i in s:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    elif i.isdigit():
        d+=1
    elif i.isspace():
        w+=1
    else:
        pass
print('total uppercase:', u)
print('total lowercase:', l)
print('total digit:', d)
print('total space:', w)
'''
'''
    if i.isalpha() or i.issmpace():
        print("great the string is alphabets")
    else:
        print('please enter a string containing only alphabets')'''
#Q2.Wap take string from user and find the count of vowel and consonent.
'''s = input("enter the string")
print(s)
s = s.lower()

vowel = 0
consonent = 0
for i in s:
    if i in 'aeiou':
        vowel +=1
    elif i.isalpha():
        consonent +=1
print("total vowels:", vowel)
print("total consonent:", consonent)
'''
#Q3.wap take a string from user and find the count of 1st and last character.
'''s = input("enter the string")
print(s)
first = 0
last = 0

for i in s:
    if i == s[0]:
        first +=1
    elif i==s[-1]:
        last+=1
print(first)
print(last)'''
#Q4.Wap take a string from user and find  percentage of the  upper , lower, digit, white space.
'''s = input("enter string")
print(s)
l = len(s)
u=0
lo =0
d =0
w=0

for i in s:
    if i.isupper():
        u +=1
    elif i.islower():
        lo +=1
    elif i.isdigit():
        d+=1
    elif i.isspace():
        w += 1
print("upper percent:" ,round(u/l*100))
print("lower percent:", round(lo/l*100))
print("digit percent:", round(d/l*100))
print("space percent:" ,round(w/l*100))
'''
'''s = 'APplE'
print(s)
a = s.swapcase()
print(a)'''
s = 'python is a programming language'
#1.Wap take a string from user and find the count of 1st and last word,
'''s = input("enter string")
print(s)
c=0
c1=0
s1 = s.split(" ")
for i in s1:
    if i == s1[0]:
        c += 1
    elif i == s1[-1]:
        c1+=1
print("count of first word", c)
print("count of last word",c1)'''
#2.Wap take a string from user and print only those words which is start from vowel.
'''

s = input("enter string")
print(s)
s1 = s.split(" ")
for i in s1:
    if i.startswith('a'):
        print(i)
    elif i.startswith('e'):
        print(i)
    elif i.startswith('i'):
        print(i)
    elif i.startswith('o'):
        print(i)
    elif i.startswith('u'):
        print(i)
'''
#3.Wap take a string from user and convert all uppercase into lower and vise versa, without using any inbuilt function.
'''s = input('Enter string: ')
t = ''
for i in s:
    asc = ord(i)
    if asc in range(65,91):
        char = asc+32
        t+=chr(char)
    elif asc in range(97,123):
        char = asc-32
        t+=chr(char)
    else:
        t+=i
print(s)
print(t)

def convert_case(string):
    converted_string = ""
    for char in string:
        if 'a' <= char <= 'z':
            converted_string += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            converted_string += chr(ord(char) + 32)
        else:
            converted_string += char
    return converted_string

user_input = input("Enter a string: ")
converted_string = convert_case(user_input)
print("Converted string:", converted_string)'''

##4.Wap take a string from user and find the the count of any particular character , without usingn any loop.
'''s1 = input('enter string')
s2 = input("enter character:")
print('COUNT of', s2, 'occurence', s1.count(s2))
'''
#format
'''name = 'pooja'
age = 25
city = 'pune'
phone = 1234531313

txt = 'my name is {}, i am {} years old, i live in {}, my contact number is {}'
print(txt.format(name, age, city, phone))
#f-string
print(f'my name is {name}, i am {age } years old, i live in {city }, my contact number is {phone }')'''
#Q1. Wap take a string from user and find the frequency of each character.
'''s = 'python programing'
fre ={ }
for i in s:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
print("Character Frequnecy:")
for c,f in fre.items():
    print(f"'{c}':'{f}'")'''
# reverse string without printing vomels 
'''s = 'My Name Pooja'
s1 = s[: : -1]
print(s1)
vowels = 'aieouAIOUE'
for i in vowels:
    if i in s1:
       s1 = s1.replace(i,'')
print(s1)
'''
# Q2. Wap take  a string from user and find the frequency of each word.
'''s = 'python programming is good programming language, python is used for multi purpose and is user understandable'
print(s)
s1 = s.split(" ")
fre ={ }
for i in s1:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
print("Character Frequnecy:")
for c,f in fre.items():
    print(f"'{c}':'{f}'")'''
#1. Write a Python program to enter a string and print it in reverse order word by word.
'''s = input("enter string")
print(s)
s1 = s.split(' ')
s2=str(s1[: :-1])
print('reverse',s2)
'''
#Q2. Write a Python program to enter a string and find the count of words and characters (excluding space).
'''s = input("enter string")
print(s) 
fre ={ }
for i in s:
    if i.isalnum():
        if i in fre:
            fre[i]+=1
        else:
            fre[i]=1
print("frequnecy of Characters excluding Space")
for c,f in fre.items():
    print(f"'{c}':'{f}'")
s1 = s.split(' ')
fre1 ={ }
for ch in s1:
        if ch in fre1:
            fre1[ch]+=1
        else:
            fre1[ch]=1
print("frequnecy of words excluding Space")
for c1,f1 in fre1.items():
    print(f"'{c1}':'{f1}'")
'''
#Q3. Write a Python program to input a string and print only those words which start with a vowel.
'''s = input("enter string")
print(s) 
s1 = s.split(" ")
for i in s1:
    if i.startswith("a"):
        print(i)
    elif i.startswith("e"):
        print(i)
    elif i.startswith("i"):
        print(i)
    elif i.startswith("o"):
        print(i)
    elif i.startswith("u"):
        print(i)'''
#Q4. Write a Python program to enter a string and sort each word of the string in ascending and descending order by the length of each word.
'''s = input('Enter a string: ')
print(s)
s1 = s.split()
print("Ascending ")
print(sorted(s1, key=len))
print("Descending")
print(sorted(s1, key=len, reverse=True))'''
#Q5. Write a Python program to enter a string in lowercase. Now, you have to convert every first character of the word to uppercase.
'''s=input("enter string")
s = s.lower()
print(s)
s1 = s.split(" ")
for i in s1:
    print(i.capitalize(), end=" ")
'''
#Q6. Write a Python program to enter a string and print the first non-repeating character 
'''s = input("enter a string")
print(s)
fre ={ }
for i in s:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
print("the non repeating characters of the string")
for c,f in fre.items():
    if f == 1:  
        print(f"'{c}':'{f}'")
        break'''
#Q7. Write a Python program to enter a string and check if it is an anagram 
#compare two words and their character frequency
'''word1 =input("enter first word  ")
word2 = input("enter second word  ")
fre1 ={ }
for i in word1:
    if i in fre1:
        fre1[i]+=1
    else:
        fre1[i]=1
fre2 ={ }
for i in word2:
    if i in fre2:
        fre2[i]+=1
    else:
        fre2[i]=1
if fre1 == fre2:
    print("anagrams")
else:
    print("not anagrams")'''
#Q8. Write a Python program to enter a string and print the most repeated character in the string.
'''s = input("enter string")
print(s)
fre = { }
for i in s:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1

for c,f in fre.items():
    max = fre[c]
    if max>fre[i]:
        print(f"'{c}':'{f}'")
    else:
        max = fre[c]'''

#9. Write a Python program to create a new string from a given string by swapping the 
# last two characters of the given string. The length of the given string must be two or more.
'''Sample Output:
   The given string is: string
   The string after swapping last two characters is: strign
s = 'string'
print(s)
print(s[:-2] + s[-1]+s[-2])
'''
#Q10. Write a Python program to read a given string. If the first or last characters are the same, return the 
# string without those characters; otherwise, return the string unchanged.
'''
s = 'poo coo oop'

if  s[0]==s[-1]:
    print(s[1:-1])
else:
    print(s)'''
#   Q2.Create a Python program to determine if a given number is a Neon number or not. 
#(A Neon number is a number where the sum of the digits of the square of the number is equal to the number itself.)

'''n = 9
s = n*n
s1= sum(int(i)for i in str(s))
if n == s1:
    print("number is neon")
else:
    print('number is not neon')
'''
#Q3.Write a Python function to check whether a given number is a magic number or not. 
#(A Magic number is a number in which the successive sums of its digits finally converge to 1.)
'''n = 101
print(n)

while n > 9: 
    sum = 0
    while n > 0:
        digit = n % 10  
        sum += digit 
        n //= 10  
    n = sum

if n == 1:
    print(" magic number.")
else:
    print("not a magic number.")'''

#Q1.Write a Python program to check if a given number is a Krishnamurthy number or not. 
    #(A Krishnamurthy number is a number whose sum of the factorial of its digits    is equal to the number itself
'''a = 145
print(a)
n = a
sum = 0
while n!=0:
    rem = n%10
    fact = 1
    for i in range(1,rem+1):
        fact*=i
    sum+=fact
    n//=10
if a==sum:
    print('Krishnamurthy\'s number')
else:
    print('not Krishnamurthy\'s number')'''


'''
7. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.'''

#1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

'''try:

    a = int(input('enter the number'))
    b = int(input('enter another number'))
    c = a/b

except ZeroDivisionError:
    print("Number cannot be divided by zero")'''
#2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

'''try:

    a = int(input('enter the number'))
    b = int(input('enter another number'))
    c = a/b

except ValueError:
    print("Incorrect Value")'''
#3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
#4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
'''try:

    a = int(input('enter the number'))
    b = int(input('enter another number'))
    c = a/b
except TypeError:
    print("Data inputed is not numerical")
except Exception as e:
    print("Data inputed is not numerical",e)'''
#5. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
'''try:
    x = [1,2,3,4]
    print(x[7])
except IndexError:
    print("out of range from the list")'''

#6. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    x = 0

except IndexError:
    print("out of range from the list")

#Q13. Write a Python program to create a new string by repeating every character twice in a given string.
''' Sample Output:
The given string is: welcomeThe new string is: wweellccoommee'''
'''s = 'welcome'
s2 = ''
for i in s:
    s2 += i*2
print(s)
print(s2)
'''
#Q14. Write a Python program to enter a string and find the occurrence of the first word, first character, last word, and last character in the string '''
# Enter a string
'''s = input("Enter a string: ")
words = s.split()
fword = words[0]
lword = words[-1]
fchr = s[0]
lchr = s[-1]

print("First word:", fword)
print("First character:", fchr)
print("Last word:", lword)
print("Last character:", lchr)

'''

#Exception Handling
'''try:
    a = int(input("enter no"))
    b = int(input("enter number"))
    c = a/b
    print("result",c)
except Exception as e:
    print('you cannot divide any number by zero,', e)'''
'''try:
    a = int(input("enter no"))
    b = int(input("enter number"))
    c = a/b
    print("result",c)

except ValueError:
    print('You have entered incorrect value')
except ZeroDivisionError:
    print("Number Cannot be divided by zero")
except Exception as e:
    print(e)
else: 
    print("calculation done without hassel", a, '/',b,'=',c)'''
'''def SI (P,R,T):
    try:
        if R>100:
            raise (ValueError,R)
        I = (P*R*T)/100
        print("simple interest",I)
    except:
        print("EXCEPTION OCCURED AT RATE",R)
SI(1000,100,1)'''



#Q1.Factorial Calculation: Write a function to calculate the factorial of a given number. 
 #Handle the case where the input is negative by raising a custom exception.
'''def factt(n):
    try:
        if n<0:
            raise (ValueError,n)
        i=1
        fact = 1
        while i<=n:
            fact = fact *i
            i+=1
        print(f"factorial of {n}",fact)
    except:
        print("exception occured at", n)
factt(-5)
'''
#Q2.Temperature Conversion: Create a function that converts temperature from 
#Celsius to Fahrenheit. Ensure that the input temperature does not fall below absolute zero, raising an exception if it does.
'''def tem(celsius):
    try:
        if celsius<0:
            raise (ValueError,celsius)
        Fahrenheit = ( celsius * 9/5) + 32.
        print (f'{celsius} into Fahrenheit is' , Fahrenheit)
    except:
        print('exception occured at ', celsius)
tem(-3)'''
#Q3.Palindrome Check: Implement a function to check if a given string is
#a palindrome. Raise an exception if the input is not a string
'''def palindrome(s):
    try:
        if s != str(s):
            raise (ValueError,s)
        s1 = s[::-1]
        if s1==s:
            print('palindrome')
        else:
            print("not palindrome")
      
    except:
        print('exception occured at ', s)
palindrome('pooja')'''
#Q4.Matrix Multiplication: Write a function to multiply two matrices.
#Raise an exception if the dimensions of the matrices are incompatible for multiplication

'''def mul(m1,m2):
    try:
        if len(m1)!=len(m2):
            raise IndexError("dimenstions are wrong", m1,m2)
        for i in len(m1):
            for j in len(m2):
                Multiplication = m1[i]*m2[j]
                print(Multiplication)
                j+=1
            i+=1
    except:
        print("exception occured at ", m1, m2)



mul([1,2,3,4],[1,2,3,4])

def mul(m1, m2):
    
    try:
         if len(m1[0]) != len(m2):
            raise ValueError("Wrong dimensions",m1,m2)
         result = []
         for i in range(len(m1)):
             new = []
             for j in range(len(m2[0])):
                 element = 0
                 for k in range(len(m2)):
                     element += m1[i][k] * m2[k][j]
                     new.append(element)
                     result.append(row)
                     print("Result of matrix multiplication:")
                     for row in result:
                         print(row)
    except:
        print("eception occured at",m1,m2)

a = [[1, 2, 3, 4,]]
b = [[1], [2], [3], [4]]
mul(a,b)
'''


#2. Write a Python program that prompts the user to input an integer 
#and raises a ValueError exception if the input is not a valid integer.

'''try:
    
    n = int(input("enter the number: "))
    if n!= int(n):
        raise ValueError("Input is not an integer",n)
    n1 = n
    print(n1)
except:
    print("exception occurred")'''

#3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.





