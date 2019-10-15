#c) Read a list of numbers. Use a recursive function to find the maximum of “n” numbers. 

def maxi(l2):
    if len(l2) == 1:
        return l2[0]
    else:
        return max(l2[0],maxi(l2[1:]))

l1 = []
print("the program will print the maximum of n numbers")
n = int(input("how many numbers you want to enter:  "))
for i in range(n):
    l1.append(int(input("enter the number")))

print("the highest number among the list is",maxi(l1))
