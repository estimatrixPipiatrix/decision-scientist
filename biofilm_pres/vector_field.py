import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

alpha = 0.1
beta  = 0.2
gamma = 0.3
delta = 0.1
mu    = 0.2

def dM_dt(M, C, V):
    return alpha*M + beta*C*M - gamma*V

def dC_dt(M, C, V):
    return delta*V - mu*M*C

M_range = np.linspace(0, 1, 20)
C_range = np.linspace(0, 1, 20)
M_grid, C_grid = np.meshgrid(M_range, C_range)

Vel = [0.01, 0.3, 1.0, 1.3]
plt.figure(figsize=(8, 8))
for i in range(4):
    V = Vel[i]
    dM = dM_dt(M_grid, C_grid, V)
    dC = dC_dt(M_grid, C_grid, V)

    magnitude = np.sqrt(dM**2 + dC**2)
    dM_normalized = dM / magnitude
    dC_normalized = dC / magnitude

    plt.subplot(2,2,i+1)
    plt.quiver(M_grid, C_grid, dM_normalized, dC_normalized, \
               scale=20, pivot='mid')
    if i>=2:
        plt.xlabel('Biofilm Mass (M)')
    if i==0 or i==2:
        plt.ylabel('Substrate Concentration (C)')
    plt.grid()
    plt.title(f'velocity ={V}')

plt.tight_layout()
plt.show()
