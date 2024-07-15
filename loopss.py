'''print('SORTING IN DICTIONARY')
x = {'A':1,'B':3,'C':4,'D':7}
print(x)
print("sort by keys")
print(sorted(x))
print('sort by values')
print(sorted(x.values()))
print('sort by items')
print(sorted(x.items()))
#update Dictionary
age ={'pooja':25,'gaurav':24,'sumit':18}
print(age)
#by using update method
age.update({'pooja':32,'gaurav':31})
print(age)
#check that particular item is present or not
age ={'pooja':25,'gaurav':24,'sumit':18}
print(age)
k='sumittt'
if k in age.keys():
    print("item found")
else:
    print("not found")
    '''
'''# Join Dictionary 
#1. update()
#2. **kwargs 
age ={'pooja':25,'gaurav':24,'sumit':18}
print(age)
x = {'A':1,'B':3,'C':4,'D':7}
print(x)
y = {'one':1,'two':2,'three':3,'four':4}
print(y)
#update
print('merged age and x by using update')
age.update(x)
print(age)
#**kwargs used to merge multiple dictionaries
print("merge by using ** kwargs")
p = {**age,**x,**y}
print(p)
print('check that particular item is present or not')
age ={'pooja':25,'gaurav':24,'sumit':18}
print(age)
k='sumittt'
print("searching item", k)
if k in age.keys():
    print("item found")
else:
    print("not found")'''
print('Join Dictionary') 
'''#1. update() use to merge to dictionary 
#2. **kwargs 
age ={'pooja':25,'gaurav':24,'sumit':18}
print(age)
x = {'A':1,'B':3,'C':4,'D':7}
print(x)
y = {'one':1,'two':2,'three':3,'four':4}
print(y)
print("merge by using ** kwargs")
p = {**age,**x,**y}
print(p)
#dictionary comprehension
el =[1,2,3,4,5,6,7,8,9]
sqr ={x:x**2 for x in el if x%2==0}
print(sqr)'''
'''#Nested Dictionary
address={'state':'bihar', 'city':'patna'}
person ={'name':'amit', 'company':'codenera', 'address': address}
print(person)
#get nested dictionary using key
print("person city", person['address']['city'])
#iterating nested dictionary
print('person details')
for key,value in person.items():
    if key=='address':
        print('printing nested dictionary')
        for n_key,n_value in value.items():
            print(n_key,n_value)
    else:
        print(key,value)'''





