#return statement is used to exit a function and return a value. If there is no return statement, the function will return None.
# def cube(num):
#     num*num*num

# print(cube(3)) #this will print None because there is no return statement in the function

# def cube(n):
#     return n*n*n
# print(cube(3)) #this will print 27 because there is a return statement in the function

is_male = True
is_tall = False

if is_male and is_tall:
    print("ur a tall male")
elif is_male and not is_tall:
    print("ur a short male")
else:
    print("ur a female")    
    