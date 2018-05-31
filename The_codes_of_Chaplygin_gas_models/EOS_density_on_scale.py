import numpy as np
import matplotlib.pyplot as plt

##### the scale factor
a= np.linspace(0.4,1.6,101)

######## the $\rho_0$ of dust, radiation and cosmological constant
rh_dark = 0.9
rh_radia = 1
rh_lam = 0.3

######### the density in terms of the scale factor
rho1 = rh_dark *(a**(-3-3*0.))
rho2 = rh_radia *(a**(-3-3*(1/3.)))
rho3 = rh_lam *(a**(-3-3*(-1.)))
    
    
    
#plt.legend(loc="upper left") 
plt.plot(a,rho1, label=r'$\rho(a)_{m}$')
plt.plot(a,rho2, label=r'$\rho(a)_{\gamma}$ ') 
plt.plot(a,rho3, label=r'$\rho(a)_{\Lambda}$') 
plt.xlabel(r'scale factor ($a$)')
plt.ylabel(r' Density ($\rho$)')
#plt.grid()
#plt.title(r'Density as function of Scale factor, $\rho = \rho_0 a^{-3(1+w)}$')
axes = plt.gca()
axes.set_ylim([0,2])
axes.set_xlim([0.8,1.6])
plt.legend()
plt.show()       
