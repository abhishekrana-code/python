# #while 
# t=1;
# while t<=5:
#     print(t*"*")
#     t+=1

# #for
# for i in range(1,6):
#     print(i*"*")    

for letter in "Abhishek":
    print(letter)


def raise_power(base, exp):
    result=1
    for i in range(exp):
        result *= base
    return result
print(raise_power(2,3))

