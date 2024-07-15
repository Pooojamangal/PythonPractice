#REVERSE A NUMBER:
'''
n = 12314345
rev=0
i = n
while i!=0:
    rem = i%10
    rev = (rev *10)+rem
    i//=10
print(rev)'''

#REVERSE NUMBER USING FOR
'''
n= 234214241
rev=0
n1=n
temp =str(n)

for i in range(len(temp)):
    rem=n1%10
    rev = (rev*10)+rem
    n1//=10
print(rev)
'''
# REVERSE SERIES FOR 1 to 100
'''
j= 1
while j<=100:
    n=j
    rev=0
    n1=n
    temp =str(n)

    for i in range(len(temp)):
        rem=n1%10
        rev = (rev*10)+rem
        n1//=10
    print(rev, end='  ' )
    j+=1
  '''
#Palindrome Using While

'''n = 121
rev = 0
i = n
c=0
while i!=0:
    rem = i%10
    rev = (rev*10)+rem
    i//=10
if rev==n:
    print('palindrome')
else:
    print('not palindrome')'''

#Palindrome Using For

'''n = 12123
rev = 0
n1 = n
temp = str(n)
for i in range(len(temp)):
    rem = n1%10
    rev = (rev*10)+rem
    n1//=10
if rev==n:
    print('palindrome')
else:
    print('not palindrome')'''
# palindrome in series
j = 10
while j<=1000:
    rev = 0
    n=j
    i=n
    while i!=0:
        rem = i%10
        rev = (rev *10)+rem
        i//=10
    if rev==n:
        print(j, end='  ')
    j+=1   
    







    
