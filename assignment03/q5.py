#wap to print even length words in a string
n=input("enter any sentence : ").split()
print("even length words are :")
for i in n:
    if len(i)%2==0:
        print(i)
  
    
    