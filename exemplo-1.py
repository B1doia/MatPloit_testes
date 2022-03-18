
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111)
x  = np.arange(0,10,0.1)
y = np.array([ a for a in x ])
l = plt.plot(x,y)
t = ax.set_title("Gráfico da Função " r"$f(x) = x$")

plt.show()
