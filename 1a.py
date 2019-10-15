#1. a)  Write Python programs to do the following: a) Read a list of elements. Create a new list having all the elements 
#minus the duplicates (Use functions). Use one-line comprehensions of create a new list of 28 even numbers. 
#Create another list reversing the elements. 


list1=[]
size=int(input("Enter the size : "))
for i in range(size):
    list1.append(input("Element : "))
mydict=dict.fromkeys(list1);
list2=list(mydict)
print(list2)
list3=[x for x in range(56) if x%2==0]
print(list3)
list4=list3[::-1]
print(list4)
