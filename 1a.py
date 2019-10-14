#1. a)  Write Python programs to do the following: a) Read a list of elements. Create a new list having all the elements 
#minus the duplicates (Use functions). Use one-line comprehensions of create a new list of 28 even numbers. 
#Create another list reversing the elements. 

l1 = []

#1a)
def create_list():
    for i in range(5):
        l1.append(input())

def remdup():
    return list(set(l1))

create_list()
print(remdup())

print([ i for i in range(28) if i%2 == 0])

l3 = ["This","is","XYZ","Here"]
print(l3[::-1])
