# Interfaces Segratation Principle advices that the interfaces should be small 
# in terms of cohesion 
""" 
                Vehicle 
                
            Aircraft    Car 
             go, fly     go, fly 



                Moveable
                    go 
                    
            Flyable   Car 
                fly     go 
                
            Aircraft 
                go
                fly
                
- Unnecessary Methods, ko differentaite karna hai for finding ignore the class here.
- Methods should have the smallest entity in the interfaces segration principle
"""

class Phong(ABC):
    
    def voice():
        pass 
    
class Text(ABC):
    def text():
        pass 
    
class Camera(ABC):
    def photo():
        pass 
