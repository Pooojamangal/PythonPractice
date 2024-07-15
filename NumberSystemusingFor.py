rev=0
n=12856
n1=n
l=str(n)# it is used to convert into string form

for i in range(len(l)):#4=>0,1,2,3
    rem=n1%10
    rev=(rev*10)+rem
    n1//=10

print("original no=",n)
print("reverse no=",rev)

 

