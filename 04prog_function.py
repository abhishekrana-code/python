#function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.


#def keyword is used to create a function and return a value. If there is no return statement, the function will return None.
# def cube(num):
#     num*num*num

# print(cube(3)) #this will print None because there is no return statement in the function

# def cube(n):
#     return n*n*n
# print(cube(3)) #this will print 27 because there is a return statement in the function
def greet(name):
    print("Hello, " + name + ". How are you?")

greet("abhishek")