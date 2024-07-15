#Read the file
'''f =open('F:\\abc.txt','r')
print(f.read())
f.close()'''
#Write in file
'''f =open('F:\\abc.txt','w')
f.write("hello guys this is my second program")
f.close()
print("content updated")

'''
'''f =open('F:\\abc.txt','a')
f.write("no replacing done with a write function")
f.close()
print("content updated")'''


#Q1. Wap create a text file and input string into it, now read that file and find the frequency of each character.

'''
file= open("f:\\a.txt", 'w') 
    file.write("pooja")

freq = { }
file= open("f:\\a.txt", 'r') 
    text = file.read()
    print(text)
    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
print(freq)'''
#Q2. Wap create a text file and input string into it, now read that file and find the frequency of each word.
'''file= open("f:\\a.txt", 'w') 
file.write("pooja hello world pooja ")


freq = { }
file= open("f:\\a.txt", 'r') 
    text = file.read()
    f = text.split()
    print(text)
    for i in f:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
print(freq)'''
#Q3. Wap create a text file and input string into it, now read that file and print the words that start from vowels.
'''
file= open("f:\\a.txt", 'w') 
file.write('air earth fire water ice spring ocean')


file= open("f:\\a.txt", 'r') 
text = file.read()
x = text.split()
print(text)
for i in x:
    if i.startswith('a'):
        print(i)
    elif i.startswith('e'):
        print(i)
    elif i.startswith('i'):
        print(i)
    elif i.startswith('o'):
        print(i)
    elif i.startswith('u'):
        print(i)
    elif i.startswith('A'):
        print(i)
    elif i.startswith('E'):
        print(i)
    elif i.startswith('I'):
        print(i)
    elif i.startswith('O'):
        print(i)
    elif i.startswith('U'):
        print(i)'''
#Q4. Wap create a text file and input string into it, now read that file and print the most repeated and least repeated word.

'''
file= open("f:\\a.txt", 'w') 
file.write('air earth fire water ice spring ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean air earth earth earth earth earth earth earth earth earth earth fire water water water water water water water water water water water water ice  ice  ice  ice ice fire spring ice  fire ocean air earth fire water fire  ice spring oceanair earth fire water ice spring ocean')


freq = { }
file= open("f:\\a.txt", 'r') 
text = file.read()
x = text.split()
print(text)
for i in x:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]= 1
print(freq)
max1 = max(freq, key=freq.get)
min1 = min(freq, key=freq.get)
print('max',max1)
print('min',min1)'''
#Q5. Wap create a text file and input string into it, now read that file and first non repeated character.
'''file = open("f:\\a.txt", 'w')
file.write('z air earth fire water ice spring ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean ocean')


freq = { }
file= open("f:\\a.txt", 'r') 
text = file.read()
print(text)
for i in text:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]= 1
        if freq[i]==1:
            break
            
print(freq)   '''

