# This class has the two responsibility one is the get properities
# Other is to store the functionality
class User:
    
    def __init__(self, name:str):
        self.name = name 
    
    def get_name(self)->str:
        pass 
    
    def save(self, user: User):
        pass 
    
    
class User:
        
    def __init__(self, name:str):
        self.name = name 
    
    def get_name(self)->str:
        pass 
    

class UserDB:
     
    def get_user(self, id)->User:
        pass 
    
    def save(self, user:User):
        pass 