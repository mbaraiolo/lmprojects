import math

# round up a float to nearest 0.05
def roundup_taxes (x):
    return math.ceil(x * 20) / 20

# 
# this class represents a shopping item in a shopping bag
#
class shopping_item: 

    def __init__(self):

        self._name = None
        self._price = 0
        self._quantity = 1      #default quantity is 1
        self._tax = 0          
        self._category = None
        self._imported = False  #default is not imported

    @property
    def name(self):
        return self._name

    @property
    def price(self): 
        return self._price
    
    @property
    def quantity(self): 
        return self._quantity

    @property
    def tax(self): 
        return self._tax

    @property
    def category(self): 
        return self._category

    @property
    def imported(self): 
        return self._imported

    @name.setter 
    def name(self, a):
        if not isinstance(a, str):
            raise TypeError("name must be set to an string")
        self._name = a 

    @quantity.setter 
    def quantity(self, a):
        if not isinstance(a, int):
            raise TypeError("quantity must be set to an int")
        self._quantity = a 

    @price.setter 
    def price(self, a): 
        if a < 0: 
            raise ValueError("price can't be below zero") 
        elif not isinstance(a, float):  
            raise ValueError("price must be set to an float") 
        self._price = a
    
    @tax.setter 
    def tax(self, a):
        if a < 0: 
            raise ValueError("tax can't be below zero") 
        elif not isinstance(a, float) : 
            raise ValueError("tax must be set to an float") 
        self._tax = a 

    @category.setter 
    def category(self, a): 
        self._category = a 

    @imported.setter 
    def imported(self, a):
        if not isinstance(a, bool):
            raise TypeError("imported must be set to an bool")
        self._imported = a 

# 
# this class represents a shopping basket
#
class shopping_basket ():

    def __init__(self): 
        self._items = []

    @property
    def items(self): 
        return self._items 

    @items.setter 
    def items(self, a): 
        self._items = a 

    def addItem (self, a):
        if (type(a) is shopping_item):
            self._items.append(a)
        else:
            raise ValueError("Wrong item type") 

    def print_items (self, verbose = False):

        print ("\n Shopping basket items")
        if (verbose) :
            for i in self._items: 
                print("{0}: {1} (cat: {2}, imported: {3})".format(i.name, i.price, i.category, i.imported))
        else:
            for i in self._items:
                if i.imported: 
                    print("{0} imported {1} \t at {2}\t(cat: {3})".format(i.quantity, i.name, i.price, i.category))
                else:
                    print("{0} {1} \tat {2}\t(cat: {3})".format(i.quantity, i.name, i.price, i.category))


#
# this class represents a shopping receipt
#
class shopping_receipt():

    __free_tax_categories = ['books','food','medicalproducts']

    def __init__(self, sb): 

        self._shopping_basket = sb   
        # calculate taxes after add shopping basket
        self.__calculate_taxes ()

    @property
    def shopping_basket(self): 
        return self._shopping_basket

    def __calculate_taxes(self):

        for i in self._shopping_basket.items:

            tax_rate = 0

            if i.category not in self.__free_tax_categories:
                tax_rate = 10

            if i.imported:
                tax_rate = tax_rate + 5

            i.tax = roundup_taxes((i.price * i.quantity * tax_rate)/100)

    def print_receipt_details (self,):

        print ("\n Receipt details")
        for i in self._shopping_basket.items:
            if i.imported:
                print("{0} imported {1}: \t{2} \t (cat: {3})".format(i.quantity, i.name, round(i.price + i.tax, 2), i.category))
            else:
                print("{0} {1}: \t{2} \t (cat: {3})".format(i.quantity, i.name, round(i.price + i.tax, 2), i.category))
        
        print ("Sales Taxes: {0}".format(self.get_taxes()))
        print ("Total: {0}".format(self.get_total()))

    # get total of the receipt
    def get_total (self):

        total = 0
        for i in self._shopping_basket.items:
            total = total + round((i.price*i.quantity + i.tax), 2)

        return round(total, 2)

    # get total of the taxes
    def get_taxes (self):
        
        total_taxes = 0
        for i in self._shopping_basket.items:
            total_taxes = roundup_taxes(total_taxes + i.tax)

        return total_taxes


