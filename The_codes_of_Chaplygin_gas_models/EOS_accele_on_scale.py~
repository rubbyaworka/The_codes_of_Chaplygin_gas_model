import numpy as np
import matplotlib.pyplot as plt

###### defining the $\rho_0$ of dust, radiation and cosmological constant
rh_dark = 0.9
rh_radia = 1.
rh_lam = 0.5

###### scale factor
a = np.linspace(0.04,1.9,100)

####### the acceleration in terms of scale factor
acc1 = -(1./6)*(rh_dark*(a**(-2.)))
acc2 = -(1./3)*(rh_radia*(a**(-3.)))
acc3 = ((rh_lam)/3.)*a 

plt.plot(a,acc1, label=r'$\ddot{a}(a)_{m}$')
plt.plot(a,acc2, label=r'$\ddot{a}(a)_{\gamma}$')
plt.plot(a,acc3, label=r'$\ddot{a}(a)_{\Lambda}$')
plt.legend(loc="upper left")    
plt.xlabel(r'scale factor ($a$)')
plt.ylabel(r'acceleration ($\ddot{a}$)')
#plt.grid()
#plt.title('acceleration as function of scale factor')
axes = plt.gca()
axes.set_ylim([-3,2])
plt.show() 
