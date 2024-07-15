'''
A
BB
CCC
DDDD
EEEEE

k = 65
i=1
while i<=5:
    j=1
    while j<=i:
        print(chr(k),end=" ")
        j+=1
    print()
    i+=1
    k+=1

E
DD
CCC
BBBB
AAAAA
k = 69
i=1
while i<=5:
    j=1
    while j<=i:
        print(chr(k),end=" ")
        j+=1
    print()
    i+=1
    k-=1
A
A B
A B C
A B C D
A B C D E
i=1
while i<=5:
    j=1
    k = 65
    while j<=i:
        print(chr(k),end=" ")
        j+=1
        k+=1
    print()
    i+=1
A
B A
C B A
D C B A
E D C B A
k = 65
i=1
while i<=5:
    j=1
    m=k
    while j<=i:
        print(chr(m),end=" ")
        m-=1
        j+=1
    print()
    i+=1
    k+=1

A
B C
C D E
D E F G
E F G H I


k = 65
i=1
while i<=5:
    j=1
    m=k
    while j<=i:
        print(chr(m),end=" ")
        m+=1
        j+=1
    print()
    i+=1
    k+=1
'''
'''
6
A B C D E
B C D E
C D E
D E
E
k = 65
i = 1
while i <=5:
    j = i
    m = k
    while j<=5:
        print(chr(m), end= '  ')
        m+=1
        j+=1
    print()
    i+=1
    k+=1

7
E
E D
E D C
E D C B
E D C B A

i = 1
while i <=5:
    j = 1
    k =69
    while j<=i:
        print(chr(k), end = "  ")
        j+=1
        k-=1
    print()
    i+=1

8
A B
A B C
A B C D E
A B C D E F G
A B C D E F G H

9
A
B F
C G J
D H K M
E  I  L  N O

k=65
r = 5
i = 1
while i <=r:
    j = 1
    n= i
    m = k
    while j<=i:
        print( chr(m), end = '  ')
        m+=r-j
   
        j+=1
           
    print()
    i+=1
    k+=1

10
                A
            B A B
        C B A B C
    D C B A B C D
E D C B A B C D E

'''
'''
6
A 
A B C
A B C D E
A B C D E F G
A B C D E F G H I


k=65
i = 1
while i <=5:
    j = 1
    m = k
    while j<=i:
        print( chr(m), end = '  ')
        m+=1
        print
        j+=1
        
        
    print()
    i+=1
'''
#dfjsoifvdfoivl
'''
                
'''
'''
Q11
a
B c
D e F
g H i J
k L m N o

Q12
E E E E E
D D D D
C C C
B B
A
k=69
i = 1
while i<=5:
    j=i
    
    while j<=5:
        print(chr(k),end = " " )
        j+=1
    print()
    i+=1
    k-=1
Q13
A A A A A
B B B B
C C C
D D
E
k=65
i = 1
while i<=5:
    j=i
    
    while j<=5:
        print(chr(k),end = " " )
        j+=1
    print()
    i+=1
    k+=1
Q14
A B C D E
A B C D
A B C
A B
A
i = 1
while i<=5:
    j=i
    k=65
    while j<=5:
        print(chr(k),end = " " )
        k+=1
        j+=1
    print()
    i+=1
    
Q15
E D C B A
D C B A
C B A
B A
A
k=69
    
i = 1
while i<=5:
    j=i
    m=k
    while j<=5:
        print(chr(m),end = " " )
        m-=1
        j+=1
    print()
    i+=1
    k-=1

A B
A B C
A B C D E
A B C D E F G
A B C D E F G H
    
'''

'''
i=1
while i<=5:
    j = 1
    k=65
    while j <= i * 2 - 1:
        print(chr(k), end=" ")
        j += 1
        k+=1
    print()
    i+=1

i=1
while i<=9:
    j = 1
    while j <= i:
        if i%2!=0:
            print(j,end = '  ')
        j+=1
    print()
    i+=1

    Q11
a
B c
D e F
g H i J
k L m N o

k=97
r = 5
i = 1

while i <=r:
    j = 1
    n= i
    m = k
    while j<=i:
        print( chr(m), end = '  ')
        if k%2==0:
            m-=31
        else:
            m+=32
   
        j+=1
           
    print()
    i+=1
    k+=1

                A
            B A B
        C B A B C
    D C B A B C D
E D C B A B C D E
'''
'''
i = 1
while i <=5:
    
    j = i
    while j<=5:
        print("  " , end = '   ' )
        j+=1
     
    j=1
    k1=69
   
    while j<=i:
        print(chr(k),end="  ")
        j+=1
        k-=1

       
    j=2
    k=66
   
    while j<=i:
        print(chr(k),end="  ")
        j+=1
        k+=1
    print()
    i+=1
 '''
'''
i = 1
k=65
while i <=5:  
    j = i
    while j<=5:
        print("  " , end = '   ' )
        j+=1  
    j=1
    k1=k
    while j<=i:
        print(chr(k1),end="  ")
        j+=1
        k1-=1
    k+=1
    j=2
    k2=66  
    while j<=i:
        print(chr(k2),end="  ")
        j+=1
        k2+=1
    print()
    i+=1
'''
'''
k=65
i=1
while i<=5:
    j=i
    while j<=5:
        print(end='  ')
        j+=1
    l=k
    j=1
    while j<=i:
        print(chr(l),end='')
        l-=1
        j+=1
    k+=1
    l=66
    j=2
    while j<=i:
        print(chr(l),end='  ')
        l+=1
        j+=1
    print()
    i+=1
'''
k=97
l=0
i = 1

while i <=5:
    j = 1
    
    while j<=i:
        l+=1
        if  l%2==0:
            print(chr(k-32), end = '  ')
        else:
            print(chr(k), end ='   ')
        k+=1
        j+=1
           
    print()
    i+=1
   





    
