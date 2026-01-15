import random 
import datetime
import time
import pandas as pd

time = datetime.datetime.now()
Bill_number = random.randint(11111,99999)

set_price = [{"salt":10,"sugar":20,"rice":60,"oil":30,"shampoo":10,"karam":20,"soap":10,"pasupu":10}]
final_item = []


print("     WELCOME TO TSN MART       ")
print(50*" ")
for k in set_price:
    print("Available items in our store")
    for item,price in k.items():
        print(f"{item} : {price} Rs")
print(50*"-")
count = 1
while True:
    items = input(f"enter {count} item in the list: " ).lower()
    
    if items == "done":
        break
    count += 1
    quanity = int(input("enter quanity: "))

    for i in set_price:
        if items in i:
            prince = quanity * i[items]
            data = {}
            data["Items Name"] = items
            data["MRP"] = i[items]
            data["Quanity"] = quanity
            data["Price"] = prince
            final_item.append(data)
        
pandas_data = pd.DataFrame(final_item)
pandas_data.to_csv("excel_data.csv")
print("TOTAL BILL GENERATE HERE")
print(50*"-")
print(10* " " + "TSN MART"+ 10 * " ")
print("Bill#:    ", Bill_number)
print("user :     Tsnmart")
print("Date // Time: ",time)
print(50 * "-")

print(pandas_data)
print("total price: ",float(pandas_data["Price"].sum()))

print("total items",count)
    




