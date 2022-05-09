# 09MAY22
# The following example is from the Python Tutorial
# Found at https://docs.python.org/3.7/tutorial/introduction.html
# 
# It demostrates a multiple assignment of variables a and b as well as the while loop.
# The loop generates the first 23 Fibonacci numbers and printes them to console output.
#
a, b = 0, 1 # a is assigned the value 0, b is assigned the value 1
while a < 30000: 
    print(a, end=', ') # end=', ' supresses new line and inserts a comma and space  
    a, b = b, a + b # the value of b is stored in a, the value of a + b is stored in b