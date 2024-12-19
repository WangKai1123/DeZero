from unicodedata import numeric
import numpy as np
from GetFunction import Exp, Function, Square

from GetVariable import Variable
from Getnumerical_diff import numerical_diff

# data = np.array(1.0)
# x = Variable(data)
# print(x.data)  # 1.0

# x = Variable(np.array(10))
# f = Square()
# y = f(x)

# print(type(y))  # <class 'numpy.ndarray'>
# print(y.data)  # [10.0]


# A = Square()
# B = Exp()
# C = Square()

# x = Variable(np.array(10))
# a = A(x)
# b = B(a)
# c = C(b)

# print(c.data)  # 100.0
# f = Square()
# x = Variable(np.array(2.0))
# dy = numerical_diff(f,x)
# print(dy)

A = Square()
B = Exp()
C = Square()

x = Variable(np.array(0.5))
a = A(x)
b = B(a)
y = C(b)

assert y.creator == C
assert y.creator.input == b

assert y.creator.input.creator == B
assert y.creator.input.creator.input == a

assert y.creator.input.creator.input.creator == A
assert y.creator.input.creator.input.creator.input == x

