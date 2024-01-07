#  wap to enter any number and check whether it is odd or even
# num=int(input("Enter the number:"))
# if (num%2==0):
#  print("Given number is even")
# else:
#  print("Given number is odd")

# wap to enter any number and whether it is divisible by 3 and 5
# num=int(input("Enter your number:"))
# if(num%3==0 and num%5==0):
#     print("given number is divisible by 3 and 5")
    
# else:
#     print("Given number is not divisible by 3 and 5")

# wap to enter five subjects marks and find total and percentage grade
# 35-45 D
# 45-60 C 
# 60-80 B 
# 80-90 A 
#  and marks not greater than 100 
# sub1=int(input("Enter your marks in English:"))
# sub2=int(input("Enter your marks in Nepali:"))
# sub3=int(input("Enter your marks in Social:"))
# sub4=int(input("Enter your marks in Math:"))
# sub5=int(input("Enter your marks in GK:"))

# marks=sub1+sub2+sub3+sub4+sub5
# print("your total marks in five subjects is :")
# percentage=marks/5
# print(f"your percentage is{percentage}%.")

# if percentage>35 and percentage<45:
#  print("D")
# elif percentage>45 and percentage<60:
#     print("C")
# elif percentage>60 and percentage<80:
#     print("B")
# elif percentage>80 and percentage<100:
#     print("A")
# else:
#     print ("fail")

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
    print("Invalid entry.Please enter 1,2,3 forrespective products.")
# quantity
Quantity=int(input("please enter no.of products you want to buy: "))
Totalprice=totalprice*Quantity
print(f"Number of products selected is: {Quantity}")
print(f"updated price=Rs.{Totalprice}")


