l1 = []
print("enter number of element you want to enter")
for i in range(int(input())):
    print("enter",i," the element")
    l1.append(int(input()))

print("minimum element is: ",min(l1),"maximum element is: ",max(l1))

print("enter a new elemnt")
l1.append(int(input()))
print(l1)

print("enter the element you want to remove")
l1.remove(int(input()))
print(l1)

print("enter the element you want to search")
if int(input()) in l1:
    print("element found")

else:
    print("element not found")