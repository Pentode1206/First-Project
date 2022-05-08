#The obligitory Hello program
#08MAY22
print('Hello')
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num -1)
    
print (factorial(9))
