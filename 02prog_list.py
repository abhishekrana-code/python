#lists are mutable
#list is a collection of items in a particular order
#list can have items of different data types
# friends = ["Rohan", "Bob", "Jin"]
# print(friends[0])
# print(friends[-1])#negative indexing
# print(friends[0:2])#slicing
# print(friends[0:])#slicing from 0 to end
# print(friends[:2])#slicing from start to 2
friends = ["Rohan", "Bob", "Jin"]
nums = [1, 2, 3, 4, 5]
# print(nums.extend(friends))#extend adds the elements of friends to nums and returns None
# print(nums)
nums.append(friends)#append adds the entire friends list as a single element to nums
# print(nums)
friends.pop()#pop removes the last element from the list
friends.insert(len(friends), "Ravan")#insert adds an element at a specific index in the list

#print(friends)
new = [2, 3, 4]
new.reverse()#reverse reverses the list
#print(new)  
new2 = new.copy();



num_grid=[ 
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
#print(num_grid[0][1])

for row in num_grid:
    # print(row)
    for col in row:
        print(col* "*")
