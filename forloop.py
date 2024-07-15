



n = int(input("enter the number you want to reverse"))
n1=n
rev=0
l = str(n)
s =0
c=0

for i in range(len(l)):
    rem = n1%10
    if rem%2!=0:
        s = s+rem
        c+=1
        print(rem)
    n1//=10
print(s,c)    

