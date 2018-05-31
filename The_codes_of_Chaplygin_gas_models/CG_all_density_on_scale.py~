import numpy as np
import matplotlib.pyplot as plt

########## parameters
A = 1/3.
B = 3.
C = 2
n = 0.05
a = np.linspace(0.3,20,101) 

######## density of CG
rho1 =np.sqrt((B/(a**6))+A)

######## density of GCG
rho2g = (A+ (B/(a**(3. + 3.*n))))**(1./(1+n))

######## density of MCG
rho3m = (B/(1.+A) + C/(a**((3.+3.*A)*(1.+n))))**(1./(1+n))


 
 
#plt.legend(loc="upper left")
plt.plot(a,rho1, label='CG') 
plt.plot(a,rho2g, label='GCG')
plt.plot(a,rho3m, label='MCG')
   
plt.xlabel(r'scale factor ($a$)')
plt.ylabel(r'energy density ($\rho$)')
#plt.grid()
#plt.title('enegy density as function of scale factor')
axes = plt.gca()
axes.set_ylim([0.,10.])
plt.legend()
plt.show()   
