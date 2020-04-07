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

ly = [0.009247139, 0.00812323423, 0.00673226, 0.0056335, 0.00864165, 0.0062324,
      0.008547088125592527,
      0.008928069775731717,
      0.009741736169915891,
      0.009741736169915891,
      0.009741736169915891,
      0.009741736169915891,
      0.01017596858529512,
      0.012115276586285901,
      0.012655308231907421,
      0.012655308231907421,
      0.015067121938231943,
      0.015738730431619045,
      0.016440275496186697,
      0.017173091537772325,
      0.017173091537772325,
      0.01793857244260369,
      0.01873817422860387,
      0.01873817422860387,
      0.019573417814876617,
      0.019573417814876617,
      0.022309243744089855,
      0.022309243744089855,
      0.023303665747243324,
      0.026560877829466895,
      0.027744814032758868,
      0.02898152352699646,
      0.03303234409819978,
      0.03303234409819978,
      0.04682249430010592,
      0.05108969774506935,
      0.05336699231206318,
      0.055745796004648976,
      0.09402,
      0.13929624006260613,
      0.13929624006260613,
      0.17323528848992867,
      0.2565020905680048,
      0.2565020905680048,
      0.26793552711303614,
      0.26793552711303614,
      0.26793552711303614,
      0.3189979402017377,
      0.33321709412448236,
      0.34807005884284165,
      0.34807005884284165,
      0.908517575651689,
      0.9490142360424744,
      0.9913160123129733,
      0.9913160123129733,
      1.0355033664891318,
      1.0355033664891318,
      1.0816603471464927,
      1.1298747492786143,
      1.1298747492786143,
      1.1802382812915648,
      3.0806074661379292,
      3.2179238127854055,
      3.3613609584193966,
      5.672674689055783,
      5.925530975545687,
      5.925530975545687,
      6.189658188912622,
      10.91135756621874,
      18.414143156536156,
      23.921470814626435,
      23.921470814626435,
      28.480358684358105,
      28.480358684358105,
      28.480358684358105,
      29.749854668099413,
      31.075937721919377,
      32.461130182667375,
      40.37017258596566,
      42.16965034285831,
      44.04933880954319,
      46.01281333333448,
      59.77438982065925,
      77.6518433]

lx = [8.9241410, 8.8311324, 8.5635245, 8.4424252,
      8.345421,
      8.123434143,
      8.0,
      7.983870967741936,
      7.903225806451613,
      7.887096774193548,
      7.870967741935484,
      7.854838709677419,
      7.854838709677419,
      7.741935483870968,
      7.725806451612903,
      7.709677419354839,
      7.596774193548387,
      7.596774193548387,
      7.580645161290323,
      7.564516129032258,
      7.548387096774194,
      7.516129032258065,
      7.516129032258065,
      7.5,
      7.483870967741936,
      7.467741935483871,
      7.403225806451613,
      7.387096774193548,
      7.370967741935484,
      7.306451612903226,
      7.290322580645161,
      7.274193548387097,
      7.225806451612903,
      7.209677419354839,
      7.048387096774194,
      7.016129032258065,
      7.0,
      6.983870967741936,
      6.72580,
      6.516129032258065,
      6.5,
      6.403225806451613,
      6.17741935483871,
      6.161290322580645,
      6.161290322580645,
      6.145161290322581,
      6.129032258064516,
      5.983870967741936,
      5.983870967741936,
      5.967741935483871,
      5.951612903225807,

      5.56451612903225,
      5.548387096774194,
      5.548387096774194,
      5.532258064516129,
      5.532258064516129,
      5.516129032258065,
      5.516129032258065,
      5.516129032258065,
      5.5,
      5.5,

      5.17741935483871,
      5.161290322580645,
      5.161290322580645,
      5.01612903225806,
      5.01612903225806,
      5.0,
      4.98387096774193,

      4.74193548387096,
      4.612903225806452,
      4.483870967741935,
      4.467741935483871,

      4.435483870967742,
      4.419354838709677,
      4.403225806451613,
      4.403225806451613,
      4.387096774193548,
      4.387096774193548,
      4.32258064516129,
      4.30645161290322,
      4.29032258064516,
      4.29032258064516,
      4.11290322580645,
      4.09677123]

nly = []
nlx = []
for i in range(len(ly[1:])):
    n = round(ly[i], 4)
    nly.append(n)

for i in range(len(lx[1:])):
    a = round(lx[i], 4)
    nlx.append(a)
point1 = [4, 80]
point2 = [7.7, 0.01]

x_values = [point1[0], point2[0]]
y_values = [point1[1], point2[1]]


plt.plot(x_values, y_values, color='red')

# def mouse_move(event):
#     x, y = event.xdata, event.ydata
#     print(x, y)
# plt.connect('motion_notify_event', mouse_move)

plt.scatter(x, y, color='blue')
plt.scatter(nlx, nly, color='blue')
plt.grid()
plt.xlim(2, 10)
plt.ylim(0.001, 10000)
plt.yscale("log")
plt.xlabel('Magnitude in Ritcher Scale')
plt.ylabel('Number of earthquakes with M>m')
plt.show()