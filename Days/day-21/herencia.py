class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("inhale, exhale")
        

class Fish(Animal):
    def __init__(Self):
        super().__init__() 
    def breathe(self):
        super().breathe()
        print("DOing this underwater")
    
    
nemo = Fish()
nemo.breathe()
