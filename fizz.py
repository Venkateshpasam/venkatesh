def fizzbuzz(num):
    if x % 3 == 0 and x % 5 == 0:
        return "Fizz Buzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x    

MAXNUM = 20
for x in range (MAXNUM):
    print (fizzbuzz(x))
