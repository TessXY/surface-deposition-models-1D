from random import randrange
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')

l     = 128                 #numero delle colonne
h     = np.zeros(l)         #altezza delle colonne

j     = 0                   #indici del ciclo
i     = 0
k     = 0

n     = 1000               #particelle depositate ad ogni ciclo

y1 = np.zeros(l)            #array per salvare i valori delle altezze
x  = np.linspace(0,l,l)

N = 5                       #numero dei cicli da graficare

y  = np.empty((N,l))

for k in range(N):    

    for j in range(n):
        
        rand = randrange(l) #randrange non include lo stop va da 0 a 127

        if (rand==0):
            maxElement = max(h[rand],h[rand+1]) 
        elif (rand==l-1):
            maxElement = max(h[rand],h[rand-1]) 
        else:
            maxElement = max(h[rand],h[rand-1],h[rand+1])     
        

        if (h[rand] == maxElement):
            h[rand] = h[rand]+1
        elif (h[rand-1] == maxElement):
            h[rand] = h[rand-1]
        else:
            h[rand] = h[rand+1]


    for i in range(l):
        y1[i] = h[i]        
        
        if k == 0:
            y[k][i] = y1[i]

        else:
            y[k][i] = y[k-1][i]+y1[i]    

    plt.step(x,y[k])

plt.title("Balistic deposition")
plt.xlabel("surface lenght x")
plt.ylabel("surface height h(x)")
plt.show()

      