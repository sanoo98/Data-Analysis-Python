#Question1 
def strLet(word, flag):
    print("Original string is",word)
    if(flag==1):
        print("Letters at even index:",word[::2])
        
    else:
        print("Letters at odd index:",word[1::2])


if __name__ == "__main__":  
    strLet('Assignment',1)

