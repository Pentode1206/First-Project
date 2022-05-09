# 09MAY22
# The following example is from the Python Tutorial
# Found at https://docs.python.org/3.7/tutorial/introduction.html
# 
# It demostrates if / elif (else if) / else statement
# The variable x is defined as an integer using int() class
# The input() function is used with prompt string "Please enter an integer: "

x = int() #Declare x

while x != int(5): #While x does not equal int(5), loop
    x = int(input("Please enter an integer: "))
    if x < 0:
        x = 0
        print('Negative value changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')
