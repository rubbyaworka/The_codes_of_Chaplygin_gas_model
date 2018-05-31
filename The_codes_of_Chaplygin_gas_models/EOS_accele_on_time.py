import numpy as np
import matplotlib.pyplot as plt

###### the $\rho_0$ of dust, radiation and cosmological constant
rh_dark = 1.2
rh_radia = 2
rh_lam = 1

######### time
t = np.linspace(0,5,100)

##### the acceleration in terms of time
a1= ( -rh_dark/6.)*(((3/4.)*rh_dark)**(-1.))
accele1 = a1*(t**(-4/3.))

a2 = (-rh_radia/3.)*(((rh_radia*4)/3.)**(-3/2))
accele2 = a2*(t**(-3/2.))

accele3 = rh_lam/3.*(np.exp(np.sqrt(rh_lam/3.)*t))

plt.plot(t,accele1, label=r'$\ddot{a}(t)_m$')
plt.plot(t,accele2, label=r'$\ddot{a}(t)_{\gamma}$')
plt.plot(t,accele3, label=r'$\ddot{a}(t)_{\Lambda}$')
plt.legend(loc="upper left")    
plt.xlabel(r'time ($t$)')
plt.ylabel(r'acceleration ($\ddot{a}$)')
#plt.grid()
#plt.title('acceleration as function of time')
axes = plt.gca()
axes.set_ylim([-6,7])
plt.show() 


