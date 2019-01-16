def fib2(x):
    nterms = x
    temp1 = 0
    temp2 = 1
    count = 0

    if nterms <=0:
        print("plfibease enter positive number")
    elif nterms == 1:
        print("Fibonacci for 1 is 0")
    else:
        print("Fibonacci till",nterms," are")
        while count < nterms:
            print(temp1, end=' , ')
            n = temp1+temp2
            temp1 = temp2
            temp2 = n
            count += 1
