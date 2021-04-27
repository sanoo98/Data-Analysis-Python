#Question2 
def strRev(word):
    #print(word[::-1])
     string = word.split(" ")
     words = [word[::-1] for word in string]
         
     string1 = " ".join(words)
     print(string1)

if __name__ == "__main__":  
    strRev("This is Assignment")