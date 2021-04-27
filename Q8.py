#Question8
def wordcount(str):
    
    words = str.split()
    count = dict()
    

    for word in words:
        if word in count:
            count[word] += 1
            
            
        else:
            count[word] = 1

    return count

#print('Enter a string')
#b=input()
#a=wordcount(b)
a=wordcount('I love python but I am confused whether to select python 2 or python3.')
print(a)