# Class, Modules, Functions should be open for extensions 
# But closed for the modifications. 


# Here you are modifying the class basedo on the number of or categories of the 
# Customers which should not be happens. 
class Discount:
    
    def __init__(self,customer, price):
        self.customer = customer
        self.price = price 
        
    def give_discounts(self):
        if self.customer == "new":
            self.price * 0.2 
        if self.customer == "vip":
            return self.price * 0.4  


# Open-Closed Principle 

class Discount:
    
    def __init__(self, customer, price):
        self.customer = customer 
        self.price = price
        
    def give_discounts(self):
        return self.price * 0.2 
    
class VIPDiscount(Discount):
    
    def give_discounts(self):
        return super().get_discounts()*2


class PrimieumDiscount(VIPDiscount):
    
    def give_discounts(self):
        return super().get_discounts()*2 