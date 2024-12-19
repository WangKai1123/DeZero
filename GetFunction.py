from GetVariable import Variable
import numpy as np

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        output.set_Creator(self)  #让变量输出
        self.input = input
        self.output = output
        return output
    
    def forward(self,x):
        raise NotImplementedError()
    def backward(self, grad):
        raise NotImplementedError()
    
class Square(Function):
    def forward(self, x):
        return x**2
    def backward(self, gy):
        x = self.input.data
        gx = 2*x*gy
        return gx

class Exp(Function):
    def forward(self, x):
        return np.exp(x)
    def backward(self,gy):
        x = self.input.data
        gx = np.exp(x)*gy
        return gx