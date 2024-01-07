class user:
    def __data(self):
        return ['ram', 'sita','gita']
    def show(self):
        for name in self.__data():
            print(name)
    def get_by_name(self, name):
        if name in self.__data():
            return name
        else:
            return 'not found'
        
obj=user()
# obj.show() #to show the data
print(obj.get_by_name("ram"))