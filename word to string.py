test_string1 = "WELCOME to python"
res = len(test_string1.split())
print ("The number of words in string1 are : ",res)
test_string2 = "suresh is an intelligent"
res =len(test_string2.split())
print ("the number of words in string2 are :",res)
list=[len(test_string1.split()),len(test_string2.split())]
print( max(list))
