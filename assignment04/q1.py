#wap to print the second largest and second smallest element in a list of 10 integer without using sort function.
list=[1,2,5,7,8,10]
mx=list.remove(max(list))
mn=list.remove(min(list))
print(f"secound max term is {max(list)}")
print(f"secound min term is {min(list)}")