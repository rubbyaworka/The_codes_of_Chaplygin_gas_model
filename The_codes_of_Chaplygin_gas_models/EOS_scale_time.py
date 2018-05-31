import numpy as np
import matplotlib.pyplot as plt

####### the initial density of dark matter, radiation and cosmological constant
rh_dark = 1.
rh_radia = 1.
rh_lam = 0.5

#### time
t = np.linspace(0,10,100)


###### scale factor of dark matter
s1 = np.sqrt(3/4.*rh_dark)
scalefac1 = s1*(t**(2/3.))


####### scale factor of radiation
s2 = np.sqrt(4/3.*rh_radia)
scalefac2 = s2*(t**(1/2.))

######### scale factor of cosmological constant
scalefac3 = np.exp(np.sqrt(rh_lam/3.)*t)

plt.plot(t,scalefac1, label=r'$a(t)_{m}$')
plt.plot(t,scalefac2, label=r'$a(t)_{\gamma}$')
plt.plot(t,scalefac3, label=r'$a(t)_{\Lambda}$')
plt.legend(loc="upper right")    
plt.xlabel(r'time ($t$)')
plt.ylabel(r'scale factor ($a$)')
#plt.grid()
#plt.title('Scale factor as function of time')
axes = plt.gca()
axes.set_ylim([0,20])
plt.show()    
