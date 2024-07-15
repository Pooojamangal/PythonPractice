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
'''Q1. Wap takes the input of elements in the list and prints all odd no.

Q2. Wap takes the input of elements in the list and prints all even no.

Q3. Wap takes the input of elements in the list and prints all even no, counts, and their sum.

Q 4. Wap takes the input of elements in the list and prints all odd no, counts, and their sum.

Q5. Wap takes the input of elements in the list and prints it in reverse order using a while loop.

Q6. Wap takes the input of elements in the list and prints all palindrome no from it.

Q7. Wap takes the input of elements in the list and prints all Armstrong no from it.'''

n[ ] = int(input("enter the list elements"))
l = len(n)
for i in range(l):
    if n[i]%2==0:
        pass:
    else:
        print(n[i])

