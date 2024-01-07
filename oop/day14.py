# class introduction:
#     x=10  #propert or attibute
    
#     def demo(self): #method or behaviour
#         print("hello world")
# # instance of class 
# obj=introduction()#creating an object
# print(obj.x)
# obj.demo()

class calculator:
    
    
    def add(self,a,b):
        return(a+b)
    def sub(self,a,b):
        return(a-b)
    def mul(self,a,b):
        return(a*b)
a=int(input("Enter the first number:"))
b=int(input("Enter the secondnumber:"))
obj=calculator()
print(obj.add(a,b))
print(obj.sub(a,b))
print(obj.mul(a,b))


 