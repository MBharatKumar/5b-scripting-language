from functools import reduce
l1 = [1, 2, 3, 4, 5]
newlist = [x*3 for x in l1]
sum1 = reduce(lambda a,b:a+b, l1)
sum2 = reduce(lambda a,b:a+b, newlist)
print(sum1)
print(sum2)