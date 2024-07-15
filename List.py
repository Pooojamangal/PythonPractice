'''
#Write a program take a input of 10 elements in list
#now modify each element with their square

x =[]
y=[]
for i in range(10):
    n = int(input("enter elements"))
    y.append( n)
    x.append(n*n)
print('input',y)
print('output' ,x)  ''' '''
print('REMOVE METHOD')
a =[1,2,3,4,5,5]
print(a)
a.remove(5)
print(a)
print()

print('POP METHOD')
b =[1,2,3,4,5,5]
print(b)
b.pop(2)
print(b)
print()

print('CLEAR METHOD')
x =[1,2,3,4,5,6,7,4]
print(x)
x.clear()
print(x)


print('INDEX METHOD')
x=[1,2,3,4,5,6,7,8,9]
print(x.index(5))
print()
#list Sorting ascending descending
print('SORT METHOD')
print()
print("ascending order")
x =[12,34,45,2,1,34,2,5,6]
print(x)
x.sort()
print(x)
print()
print("descending order")
y =[12,34,45,2,1,34,2,5,6]
print(y)
y.sort(reverse=True)
print(y)
print()
print("MAX AND MIN")
print()
z = [12,345,5665,3422,567]
print(z)
print("MAX", max(z))
print("MIN", min(z))
print("SUM",sum(z))
print("AVERAGE",sum(z)/len(x))



x=[1,2,3,4,5,6,7,2,3]
y=[]
z=[]
for i in x:
    if i%2==0:
      y.append(i)
    else:
      z.append(i)
print(y)
print(sum(y))
print(z)
print(sum(z))


i=1
while i <=5:
    j = 1
    
    while j<=i:
        print(('*'), end = '  ')
    

        j+=1
           
    print()
    i+=1

def addition(a,b):
    return a+b
print(addition(9,5))

def add(a, b):
    return a + b

def greet(name):
    if name:
        return "Hello, " + name
    else:
        return "Hello, World"
    print("This line will never be executed")
print(greet('pooja'))


x = [1,2,3,[11,12,13],4,5]

n=len(x)
for i in range(n):
    if type(x[i]) is list:
        if len(x[i] )> 1:
            l = len(x[i])
            for j in range (l):
                print(i,j,x[i][j])
    else:
        print(i,x[i])
        
'''
'''Q1. Wap takes the input of elements in the list and prints all odd no.
x =[]
for i in range(10):
    n = int(input("enter elements"))
    x.append(n)
print(x)

l = len(x)
for i in range(l):
    if x[i]%2==0:
        pass
    else:
        print(x[i])

Q2. Wap takes the input of elements in the list and prints all even no.
x =[]
for i in range(10):
    n = int(input("enter elements"))
    x.append(n)
print(x)

l = len(x)
for i in range(l):
    if x[i]%2==0:
         print(x[i])
    else:
        pass

Q3. Wap takes the input of elements in the list and prints all even no, counts, and their sum.
x =[]
s=0
c=0
for i in range(10):
    n = int(input("enter elements"))
    x.append(n)
print(x)

l = len(x)
for i in range(l):
    if x[i]%2==0:
        print(x[i])
        c+=1
        s = s+ x[i] 
    else:
        pass
print('sum' , s ,'count' , c)

Q 4. Wap takes the input of elements in the list and prints all odd no, counts, and their sum.
x =[]
s=0
c=0
for i in range(10):
    n = int(input("enter elements"))
    x.append(n)
print(x)

l = len(x)
for i in range(l):
    if x[i]%2==0:
        pass
    else:
        print(x[i])
        c+=1
        s = s+ x[i] 
print('sum' , s ,'count' , c)


Q5. Wap takes the input of elements in the list and prints it in reverse order using a while loop.

Q6. Wap takes the input of elements in the list and prints all palindrome no from it.

Q7. Wap takes the input of elements in the list and prints all Armstrong no from itz = [12,345,5665,3422,567]
print(z)
max = z[0]
for i in z:
    if (i>max):
        max = i
    
print(max)
.


list1=[]

for i in range(10):
    n = int(input("enter the list elements"))
    list1.append(n)
print(list1)

value = int(input("enter the value"))
print(value)

for i in list1:
    if i == value:
        list1.remove(i)

print("New List", list1)
  '''
'''
n = 25
sq =n**2

n1=str(n)
sq1=str(sq)
if sq1.endswith(n1):
    print("automorphic number")
else:
    print("not automorphic")


a = [ ]
n = int(input("enter how many items you need in the list"))
for i in range(1,n+1):
    x = int(input("enter the value"))
    a.append(x)
print(a)
rev = 0
for i in range(len(a)+1):
    while i!=0
     
a = [1,2,3,6,4,2]
b = [ ]
c = [ ]
i=0
for i in range(len(a)):
    if a[i]%2!=0:
        b.append(a[i])
    elif a[i]%2==0:
        c.append(a[i])
    else:
        pass
print(a)
print(b)
print(c)
print(sum(b))
print(sum(c))
  
a =[12,34,45,2,1,34,2,5,6]
b=[ ]
c= len(a)-1

while c >= 0:
    b.append(a[c])
    c -= 1
print(b)
print("3rd minimun number")
print(a)
a.sort()
print(a[2])
print(a)
print("descending order")
y =[12,34,45,2,1,34,2,5,6]
print(y)
y.sort(reverse=True)
print(y)
 
old = [1, 2, 4, 5, 6, 1, 8, 1, 9]
new = []
print("Original list:", old)

for item in old:
    if item not in new:  
        new.append(item)

new.sort(reverse=True)
print("New list:", new)
print("third minimum:", new[1])

x =[1,2,3,4,5,6]
#6,5,4,1,2,3 right
#3,4,5,6,1,2 left

n = 1
y=x[n:] +x[:n]
print(y)

x =[]
y=[]
for i in range(5):
    n = int(input("enter elements"))
    x.append(n)
print(x)

l = len(x)
rev =0
for i in range(l):
    while x[i]==0:
        rem = x[i]%10
        rev = (rev*10) +rem
        x[i]//=10
    if x[i]==rev:
        y.append(rev)
    else:
        pass
print(y)
        
'''  








































