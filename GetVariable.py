class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None
        self.creator = None
    
    def set_Creator(self,func):
        self.creator = func
        
