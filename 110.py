#count the numbers of dogs and chickens from the total heand and legs 

heads = int(input("enter the heads:"))
legs = int(input("enter the legs:"))

dogs = (legs - 2*heads)/2
chickens = heads - dogs

print("dogs:",dogs)
print("chickens:",chickens)
