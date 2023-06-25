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



"""