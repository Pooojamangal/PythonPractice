'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1

i = 5
while i>=1:
    j = i
    while j>=1:
        print(i,end=" " )
        j-=1
    print()
    i-=1
    
'''

'''
               1 
            2 2 
         3 3 3 
      4 4 4 4 
   5 5 5 5 5
 
i = 1
while i<=5:
    j = i
    while j<=5:
        print("  ",end=" " )
        j+=1
    j = 1
    while j<=i:
        print(i,end=" " )
        j+=1
    print()
    i+=1
    '''
'''
10 9 8 7 
6 5 4 
3 2 
1

k=10
i = 1
while i<=4:
    j = i
    while j<=4:
        print(k,end=" " )
        k-=1
        j+=1
    print()
    i+=1   
'''
'''
1  
2  6  
3  7  10  
4  8  11  13  
5  9  12  14  15  

r = 5
i=1
while i<=r:
    j=1
    n=i
    while j<=i:
        print(n, end="  ")
        n+=r-j
        j+=1
    print()
    i+=1
'''






























