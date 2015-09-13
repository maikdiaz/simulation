 
import matplotlib.pyplot as plt
import numpy as np

def xy(r,phi):
  return r*np.cos(phi), r*np.sin(phi)

fig = plt.figure()
ax = fig.add_subplot(111,aspect='equal')  

phis=np.arange(0,6.28,0.01)
r =1000.
ax.plot( *xy(r,phis), c='r',ls='-' )
plt.show()

try:
        input('press something to finish')
except:
    print 'finished program'