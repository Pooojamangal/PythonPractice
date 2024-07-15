'''Do it by using for loop

Q1. Write a program to print all natural numbers from 1 to n.
Q2. Write a program to print all natural numbers in reverse (from n to 1).
Q3.Wap take input first and last no and display all odd numbers between
them and find sum and count. 
Q4.Wap take input first and last no and display all even numbers between them
and find sum and find sum an count.

n = 80
for i in range(1,n):
    print(i ,end=' ')

n = 80
for i in range(n,0,-1):
    print(i ,end=' ')

first = int(input("enter first number"))
last = int(input("enter last number"))
s=0
c=0
for i in range(first,last,2):
    print(i, end=' ')
    s+=i
    c+=1
print( '\n sum',s, 'count',c)

first = int(input("enter first number"))
last = int(input("enter last number"))
s=0
c=0
for i in range(first-1,last,2):
    print(i, end=' ')
    s+=i
    c+=1
print( '\n sum',s, 'count',c)'''


