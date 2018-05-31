import numpy as np 
import matplotlib.pyplot as plt  


####### definition of Friedmann universe filled with CG
def CG(a, t, A, B):
    dadt = np.sqrt(np.sqrt(A*a**6 + B) )/np.sqrt(3.*a)
    return dadt 

######## parameters    
A =1/3.     
B = 3    
a0 =0.1

######### time
t = np.linspace(0, 16, 101) 

from scipy.integrate import odeint
sol1 = odeint(CG, a0, t, args=(A, B))

####### definition of acceleration in terms of scale factor a
def accele1(a):
    den = np.sqrt(B/(a**6) + A)
    return - a/6 * (den - 3*A / den)

plt.figure()
plt.plot(t, accele1(sol1[:]) )
plt.xlabel(r'time ($t$)')
plt.ylabel(r' acceleration ($\ddot{a}$)')
#plt.grid()
#plt.title('acceleration as function of time')
axes = plt.gca()
axes.set_ylim([-7,17]) 
plt.show()  
