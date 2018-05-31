import numpy as np
import matplotlib.pyplot as plt

######## parameters
A = 1/3.
B = 3.
n = 0.05

###### scale factor
a = np.linspace(0.3,20,101) 

###### definition of density of GCG
rho2g = (A+ (B/(a**(3. + 3.*n))))**(1./(1+n))



 
 
#plt.legend(loc="upper left")
plt.plot(a,rho2g)    
plt.xlabel(r'scale factor ($a$)')
plt.ylabel(r' density ($\rho$)')
#plt.grid()
axes = plt.gca()
axes.set_ylim([0.,10.])
plt.legend()
plt.show()   
