import numpy as np
import matplotlib.pyplot as plt



####### parameters
A = 1/3.
B = 3.

##### scale factor
a = np.linspace(0.3,20,101) 

### definition of density of CG
rho1 =np.sqrt((B/(a**6.))+A)



 
 

plt.plot(a,rho1 )    
plt.xlabel(r'scale factor ($a$)')
plt.ylabel(r'enegy density ($\rho$)')
axes = plt.gca()
#axes.set_ylim([0.,10.])
plt.legend()
plt.show()   
