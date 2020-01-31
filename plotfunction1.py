from matplotlib import pyplot as plt
import numpy as np
x=np.linspace(-np.pi,np.pi,256,endpoint=True)
C, S = np.sin(x), np.cos(x)
plt.plot(x,C,'o')
plt.plot(x,S)
plt.axis([-8,8,-1,1])
plt.show()
