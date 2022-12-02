import numpy as np

x = [float(i) for i in input("x")]
x = np.array(x)


y = [float(i) for i in input("y")]
y = np.array(y)

a = len(x)
b = sum(x)
c = sum(y)
d = sum(x**2)
e = sum(x*y)

