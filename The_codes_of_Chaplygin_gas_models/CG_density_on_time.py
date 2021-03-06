############ Chaplygin gas


######## definition of Friedmann universe filled with CG
import numpy as np  
def CG(a, t, A, B):
    dadt = np.sqrt(np.sqrt(A*a**6 + B) )/np.sqrt(3.*a)
    return dadt 
     
###### parameters    
A = 1./3
B=0.3
a0 = 0.1

##### time
t = np.linspace(0, 16, 101)


from scipy.integrate import odeint
sol1 = odeint(CG, a0, t, args=(A, B))

import matplotlib.pyplot as plt

######### definition of density
def d1(a):
    den = np.sqrt(B/a**6. + A)
    return den
    
 
	   

plt.plot(t, d1(sol1[:]) )

plt.xlabel(r'time ($t$)')
plt.ylabel(r'density ($\rho$)')
plt.legend()
#plt.grid()
#plt.title('density as function of time')
axes = plt.gca()
axes.set_ylim([-2,20])
plt.show()




