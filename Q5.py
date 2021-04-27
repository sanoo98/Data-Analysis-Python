#Question5
#def remDup(list1):
#	list1 = list(dict.fromkeys(list1))
#	print("Resultant List:",list1)
    
#l1=[30,40,22,33,22,11]
#remDup(l1)


#--------------------
def remDup(a):
   i = 0
   while i < len(a):
      j = i + 1
      while j < len(a):
         if a[i] == a[j]:
            del a[j]
         else:
            j += 1
      i += 1

l1 = [30,40,22,33,22,11]
remDup(l1)
print("Resultant List:",l1)