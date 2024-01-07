print("---computer bazzar")
print("1.Dell(Rs:20000) 2.Toshiba(Rs:30000) 3.Mac(Rs:50000)")
print("==================")
product_name=''
quantity=0
dell_price=0
toshiba_price=0
mac_price=0
option=int(input("Enter your option:"))
if option == 1:
    quantity =int(input("Enter quantity"))
    product_name="Dell"
    dell_price=quantity*20000
