'''
j =1
while j<=5:
    i =1
    while i<=5:
        print(i,end=' ')
        i+=1

    print()
    j+=1
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5

1. Write a program to find the factorial of a number.
2. Write a program to check if a number is Palindrome or not
3. Write a program to find the sum of digits of a number.
4. Write a program to reverse a given number.
5. Write a program to find the sum and count of only even no from a number.
6. Write a program to find the sum and count of only odd no from a number.
7. Write a program takes a munber from the user and search any particular no from it also print their count.
8. Write a program to find the Fibonacci series up to n terms.


Q1
n = int(input("enter the number you want to find factorial for"))
j =1
while j<=n:
    i = 1
    fact = 1
    while i<=j:
        fact = fact * i
        i+=1
        
    print(fact, end=' ')
    j+=1

n = int(input("enter the number"))
j =10
while j<=n:
    i=j
    rev = 0
    while i!=0: 
        rem=i%10 
        rev = (rev*10)+rem 
        i//= 10
    if rev==j:
        print(j)
    j+=1


#3. Write a program to find the sum of digits of a number.

n = int(input("enter the number"))
s=0
i=n
rev = 0
while i!=0:
    rem = i%10
    rev = (rev *10) + rem
    i//=10
print(rev)

#5. Write a program to find the sum and count of only even no from a number.

n = int(input("enter a number"))
s= 0
c=0
i=n
while i!=0:
    rem = i%10
    if rem%2==0:
        s = s+rem
        c +=1
    i//=10
print('sum',s,'count',c)

#6. Write a program to find the sum and count of only odd no from a number  
n = int(input("enter a number"))
s= 0
c=0
i=n
while i!=0:
    rem = i%10
    if rem%2!=0:
        s = s+rem
        c +=1
    i//=10
print('sum',s,'count',c)

#7. Write a program takes a munber from the user and search
#any particular no from it also print their count.

n = int(input("enter a number"))
find =int(input("enter a digit you want to find"))
c=0
i = n
while i!=0:
    rem = i%10
    if rem==find:
        c+=1
    i//=10
if c>0:
    print("Number FOund")
else:
    print("Number is missing")

#Write a program to find the Fibonacci series up to n terms.
n  = int(input("enter number"))
a=0
b=1
i=2
while i <=n:
    temp = a+b
    a=b
    b=temp
    print(b)
    i+=1

    9. Write a program to find the largest among three numbers.
10. Write a program to check if a given year is a leap year.
11. Write a program to find the GCD (Greatest Common Divisor) of two numbers.

a = int(input("enter number 1"))
b = int(input("enter number 2"))
c = int(input("enter number 3"))

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
   

year = 2023

if year%4==0 and year%100!=0 or year%400==0:
    print("leap year")
else:
    print(year, "not a leap year")




n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number"))
min_n = min(n1, n2)
gcd = 1
i = 1
while i <= min_n:
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
    i += 1
print(n1, n2, gcd)


#PRIME NUMBER check
j = 10
while j <= 100 :
    
    n=j
    i=2
    c=0
    while i<n:
        if  n%i==0:
            c+=1
        i+=1
       
    if c==0:
        print('Prime number between 10 to 100')
        print(j)
        j+=1
corrected
j = 10
while j <= 100:
    n = j
    i = 2
    c = 0
    while i < n:
        if n % i == 0:
            c += 1
        i += 1
    if c == 0:
       
        print(j)
    j += 1

#ARMSTRONG IN LOOP

j = 10
while j<1000:
    n=j
    s=0
    i=n
    rem=0
    while i!=0:
        rem = i%10
        s = s + rem*rem*rem
        i//=10
    if s==j:
        print(j)
    j+=1

#GCD:
n= 26
n2= 84

gcd =1

for i in range(1,min(n,n2)D):
    if n%i==0 and n2%i==0:
        gcd = i
print("gcd = ", gcd)
'''














































