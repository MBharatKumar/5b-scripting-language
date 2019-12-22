class rectangle:   
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def area(self):
        return self.length*self.breadth
    
print(rectangle(3,4).area())
print(rectangle(4,5).area())