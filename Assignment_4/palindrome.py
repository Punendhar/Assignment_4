def ispalindrome():
    x = input("please input a string : ")
    if x[::-1] == x:
        print("give string ",x, "is palindrome")
    else:
        print("give string ",x, "is not palindrome")    
