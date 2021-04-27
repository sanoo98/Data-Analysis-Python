#Question4
def even(list):
    a=[]
    for i in list:
        if (i % 2) == 0:
            a.append(i)
    return a
    
def odd(list):
    b=[]
    for i in list:
        if (i % 2) != 0:
            b.append(i)
    return b
    
#Main

#l1=[30,40,22,33,22,11]
#l2=[40,30,10,99,53]

l1=[]
n = int(input("Enter number of elements in list 1 : "))
print("Enter", n ,"Elements of list 1:")
for i in range(0, n):
    element = int(input())
    l1.append(element) 
            
print("List 1:",l1)

l2=[]
n = int(input("Enter number of elements in list 2 : "))
print("Enter", n ,"Elements of list 2:")
for i in range(0, n):
    element = int(input())
    l2.append(element) 
            
print("List 2:",l2)
    
a=even(l1)
b=odd(l2)
    
l3=a+b
l3 = list(dict.fromkeys(l3))
print("\nResultant list:")
print(l3)