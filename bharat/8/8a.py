def atom():
    at={
        "he":"helium",
        "ne":"neon",
        "li":"lithium"
    }
    a = input("enter the symbol")
    b = input("enter the element")
    at.update({a:b})
    c = input("enter the symbol")
    d = input("enter the element")
    at.update({c:d})
    print("elements in dictonary are",at)
    print("number of elements in dictonary are",len(at.keys()))
    f = input("enter the element you want to search")
    if f in at.values():
        print("element found ")
    else:
        print("element not found")
atom()

