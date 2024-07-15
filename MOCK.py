''' 


Q2.Wap to take a no from user and check it is prime no or not.
n = 17
i = 2
c = 0
while i<n:
    if n%i==0:
        c+=1 
    i+=1
if c>0:
    print('not prime')
else:
    print('prime')  
Q3.Create a Python program to print all prime numbers between 10 and n.

n = int(input("enter the number"))
for x in range(1,n):
    i = 2
    c = 0
    while i<x:
        if x%i==0:
            c+=1 
        i+=1
        
    if c>0:
        pass
    else:
        print(i)  
        


Q3.Wap to take a no from user and check it is Armstrong no or not.
n = 142
rev = 0
i = n
while i!=0:
    rem = i%10
    rev = rev + rem*rem*rem
    i//=10
if rev==n:
    print('armstrong')
else:
    print('not armstrong')
Q2.Develop a Python program to print all Armstrong numbers in the range from 10 to n.
n = int(input("enter a  number"))
for i in range(1,n+1):
    sum_of_cube = 0
    t = i
    while t!=0:
        rem  = t%10
        sum_of_cube = sum_of_cube + rem*rem*rem
        t//=10
    if sum_of_cube == i:
        print(i)


Q4.Wap to take a no from user and check it is neon no or not.
Q9.Create a Python program to determine if a given number is a Neon number or not. 
(A Neon number is a number where the sum of the digits of the square of the number is equal to the number itself.)

Q5.Wap to take a no from user and check it is Krishnamurthy's no or not.
Q8.Write a Python function to check if a given number is a Krishnamurthy number or not. 
A Krishnamurthy number is a number whose sum of the factorial of its digits    is equal to the number itself.)

Q10.Write a Python function to check whether a given number is a magic number or not. 
(A Magic number is a number in which the successive sums of its digits finally converge to 1.)

Q6.Wap to take a no from user and print the Fibonacci series.
Q6.Write a Python program that takes a number from the user and prints the Fibonacci series up to that number.

Q7.Wap to take a no from user and find the factorial.
Q7.Develop a Python program that takes a number from the user and finds its factorial. 

Q8.Wap to take a no from user , now search any particular digit from that no , if digit found then print their count also.
Q5.Implement a Python program that takes a 5-digit number from the user. Search for a specific number within it, and if found, print its count. 

'''

#reverse series( Q4.Write a Python program that takes a number as input from the user and prints its reverse. ) 
'''
i = 12345
rev = 0
t = i
while t!=0:
    rem = t%10
    rev = (rev*10)+rem
    t //= 10
print(rev)
'''
#Q1.Wap to take a no from user and check it is palindrome no or not./ Write a Python program that prints all palindrome numbers between 10 and n (inclusive).
#Palindrome Using While loop(Q1.Wap to take a no from user and check it is palindrome no or not.)

'''n = 12345
rev = 0
t = n
while t!=0:
    rem = t%10
    rev = (rev*10)+rem 
    t  //= 10
if rev == n:
    print('Number is Palindrome')
else:
    print("Number is Not palindrome")'''
#Palindrome series using while loop (Q1. Write a Python program that prints all palindrome numbers between 10 and n (inclusive).)
'''n = 200
i=10
while i<=n:
    rev = 0
    t=i
    while t!=0:
        rem = t%10         
        rev = (rev*10)+rem 
        t //= 10   
        if i==rev:
            print(i)
    i+=1'''

#Palindrome Using For loop (Q1. Write a Python program that prints all palindrome numbers between 10 and n (inclusive).)
'''
n = 200

for i in range(10,n+1):
    rev = 0
    t=i
    while t!=0:
        rem = t%10         
        rev = (rev*10)+rem 
        t //= 10   
        if i==rev:
            print(i)
'''
#Q9.Wap to take a no from user ,now find the sum of even and odd number with count separately.

n = int(input("enter a number"))
even_sum = 0
odd_sum = 0
even_count = 0
odd_count = 0
i = n
while i!=0:
    rem = i%10
    if rem%2==0:
        even_sum += rem
        even_count += 1
    else: 
        odd_count +=1
        odd_sum += rem
    i//=10
print("even number count: " , even_count)
print("even number sum", even_sum)
print("Odd Number count", odd_count)
print("Odd number sum ", odd_sum)