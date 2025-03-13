import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,3,1],float)
y = np.array([1,2,2,1,1],float)
plt.plot(x,y,'g',linewidth=1,marker='.',markersize=5)
plt.axis([0,4,0,4])
plt.title('Graf')
plt.grid(True)
plt.show()
