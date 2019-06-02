import numpy as np
import os 
from matplotlib import pyplot as plt
import seaborn

alpha = 0.037
beta = 16.5

def _zero_order(x, t):
    y = np.zeros(x.shape)
    y[np.nonzero(x >= t)[0]] = 450
    return y

fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111)

ax.set_xlabel('Time [s]')
ax.set_ylabel('Rotor angular velocity [rad / s]')
ax.set_title(r'Yoerger\'s first-order dynamic model, $\alpha={}$, $\beta={}$'.format(alpha, beta))

ax.set_xlim([0, 4])
ax.set_ylim([0, 500])
ax.grid(True, which='major', color='gray', alpha=0.5, linestyle='--')

tau = 0.2

x = np.linspace(0, 4, 200)
input = _zero_order(x, 2)
y = np.zeros(x.shape)
dt = np.diff(x)[0]

for i in range(1, x.size):
    y[i] = y[i - 1] + dt * (beta * input[i] - alpha * y[i - 1] * np.abs(y[i - 1])) 

seaborn.lineplot(
    x=x, 
    y=input,
    ax=ax,
    label='Input')

seaborn.lineplot(
    x=x, 
    y=y,
    ax=ax, 
    label='Output')

ROOT_FOLDER = '../../../docs/packages/uuv_simulator/docs/images/actuators/'
plt.savefig(os.path.join(ROOT_FOLDER, 'dyn_yoerger.png'), bbox_inches='tight')
plt.show()