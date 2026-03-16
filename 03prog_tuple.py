#tuple are immutable
#tuple can be created by using parentheses () or by using the tuple() function 
t1 = (1, 2, 3, 4, 5)
print(t1)
print(type(t1))
#tuple(1, 2, 3, 4, 5) #this will give an error because tuple() function takes only one argument which is an iterable
t2 = tuple([1, 2, 3, 4, 5])
print(t2)
print(type(t2))