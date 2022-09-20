# run below command in terminal
# pip install matplotlib

import matplotlib.pyplot as plt

x_axis = list(range(-100,101))
y_axis = list(map(lambda x: x**3, x_axis))
plt.plot(x_axis,y_axis)
plt.show()

