
'''5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
'''
'''i =1
while i<=5:
    j =1
    while j<=i:
        print("*", end=" ")
        j+=1
    print()
    i+=1'''
'''
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
    
for x in range(1,200):
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
        
    
n = 121
rev = 0
i = n 
while i != 0:
    rem = i%10
    rev = (rev*10)+rem
    i//=10
if rev == n:
    print("palindrome")
else:
    print("not palindrome")  '''