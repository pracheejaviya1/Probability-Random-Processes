import numpy as np
import matplotlib.pyplot as plt

k = 2
n = 1000
c = 1
term1 = np.power(n/n+1, k)
term2 = np.power(n/n+2, k)
termc1 = np.power(n/n+1, 1)
termc2 = np.power(n/n+2, 1)
for i in range(4, 9):
    CLa = term1*((term1-term2)/(term2-np.power(term1, 2)))*i*0.2
    CLc = term1*((term1-term2)/(term2-np.power(term1, 2)))*i*0.2
    total = CLa*CLa*CLc
    print(round(CLa, 2), round(CLc, 2), round(total))
    plt.scatter((i*0.1), total)

plt.xlim(0, 1)
plt.ylim(0, 100)
plt.xlabel('Confidence level of Component')
plt.ylabel('System reliability')
plt.show()
