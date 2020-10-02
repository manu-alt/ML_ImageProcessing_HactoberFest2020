import numpy as np
import math as m
import matplotlib.pyplot as plt
x1=[0,0,1,1]
x2=[0,1,0,1]
t=[0,1,1,0]
u1 = [0, 0]
u2 = [1, 1]
ph1 = []
ph2 = []
G =[]
dmax = m.sqrt( ((u1[0] - u2[0])**2) + ((u1[1] - u2[1])**2))
for i in range(0,len(x1)):
    ph1.append(m.exp((-1*2/(dmax**2))*(((x1[i] - u1[0])**2) + ((x2[i] - u1[1])**2))))
    ph2.append(m.exp((-1*2/(dmax**2))*(((x1[i] - u2[0])**2) + ((x2[i] - u2[1])**2))))

for i in range (0, len(ph1)):
    G.append([ph1[i],ph2[i],1])
#print(G)
Garr = np.array(G)
Garrt = Garr.transpose()

Gp = np.linalg.inv(Garrt.dot(Garr)).dot(Garrt)
print(Gp)
w = Gp.dot(np.array(t).transpose())
print(w)
plt.plot([0,0.9],[0.9,0],'--g')
plt.plot(ph1,ph2,'.b')
plt.show()