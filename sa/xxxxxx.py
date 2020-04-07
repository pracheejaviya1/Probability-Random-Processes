import matplotlib.pyplot as plt
import numpy as np
from random import seed
from random import random, randint

seed(3)
y = []
x = []
for i in np.arange(2, 4, 0.1, dtype='float'):
    finx = round(i, 1)
    x.append(finx)

print(x)

for i in range(20):
    val = random()
    value = randint(0, 35)
    sum = 100+val+value
    finy = round(sum, 2)
    y.append(finy)
print(y)

# chkx = []

# for i in np.arange(4, 8, 0.1, dtype='float'):
#     finx1 = round(i, 1)
#     chkx.append(finx1)

# chky = []

# np.logspace(4.0, 8.0, num=40)
# for i in range(40)

#     chky.append(np.logspace(0.1, 0.001,100 , endpoint=True))


plt.scatter(x, y)
plt.grid()
plt.xlim(2, 10)
plt.ylim(0.001, 10000)
plt.yscale("log")
plt.show()

# plt.scatter(x, y)
# plt.grid()
# plt.xlim(2, 10)
# plt.ylim(0.001, 10000)
# plt.yscale("log")
# plt.show()
