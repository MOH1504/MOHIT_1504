"""
Encapsulation : which is contain multiple data elements in a single location.

e.g. class

class contain different data member and member function in a single entity.


Private Access Modifier:

                        The members of a class that are declared private are accessible within the class only, 
                private access modifier is the most secure access modifier.
             Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class



-->> There are three access modifiers:

1) public - the property or method can be accessed from everywhere. This is default.
2) protected - the property or method can be accessed within the class and by classes derived from that class.
3) private - the property or method can ONLY be accessed within the class.


"""

class shop: 
    def __init__(self):
        self.mobile = 12000
        self.__laptop = 25000 



    def display(self):
        print("mobile = ",self.mobile)
        print("laptop = ",self.__laptop)

    def change_price(self,newprice): # change price of private access class to public.
        self.__laptop = newprice

obj = shop()
obj.display()

obj.mobile = 20000
obj.__laptop = 60000

obj.display()

obj.change_price(65000)
obj.display()