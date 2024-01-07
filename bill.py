print("Computer Bazzar")
Dell=20000
Toshiba=30000
Mac=50000
print("product we have:")
print("1.Dell-->Rs.20,000 \n 2.Toshiba-->Rs.30,000 \n 3.MAc-->50,000")
# choosing product
product=int(input("Enter a product number 1,2,3:\n"))
if product==1:
    print(f"you have choosen the product 1: Dell.")
    print(f"product price=Rs{Dell}.")
    totalprice=Dell
elif product==2:
    print(f"You have choosen the product 2:Toshiba.")
    print(f"product price=rs{Toshiba}")
    totalprice=Toshiba
elif product==3:
    print(f"You have choosen the product 3:Mac.")
    print(f"product price=rs{Mac}")
    totalprice=Mac
else:
    print("Invalid entry.Please enter 1,2,3 for respective products.")
# quantity
Quantity=int(input("please enter no.of products you want to buy: "))
Totalprice=totalprice*Quantity
print(f"Number of products selected is: {Quantity}")
print(f"updated price=Rs.{Totalprice}")
# choosing package type

package=int(input("Enter the packaging type:\n 1.plastic\n2.Bag\n3.giftbox\n4.None"))
if package == 1: