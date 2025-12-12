n1 = int(input("First: "))
n2 = int(input("Second: "))

# define an anonymous function
mean = lambda x,y: (x+y)/2


# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f"The arithmetic mean of {result}")