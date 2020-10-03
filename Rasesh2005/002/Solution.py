sum=0
priceList=[]
i=1
while True:
    price=int(input(f"Enter The Price of item {i}: "))
    if not price: break 
    # if price is 0 then it is false , so if not false will trigggers break statement
    sum+=price
    priceList.append(price)
    i+=1
print("Item No.\tPrice")
for index,price in enumerate(priceList):
    print(f'{index+1}\t\t{price}')
print(f"Total\t{sum}")
