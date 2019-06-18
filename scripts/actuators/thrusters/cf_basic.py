import numpy as np
import os 
from matplotlib import pyplot as plt
import seaborn

seaborn.set()
seaborn.set_style('ticks')


def _cf(x, rotor_constant):
    return rotor_constant * np.multiply(x, np.abs(x))

fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111)

ax.set_xlabel('Rotor angular velocity [rad / s]')
ax.set_ylabel('Thrust [N]')
ax.set_title('Thruster basic conversion function')

ax.set_xlim([-100, 100])
ax.set_ylim([-500, 500])
ax.grid(True, which='major', color='gray', alpha=0.5, linestyle='--')

rotor_constant = np.array([0.001, 0.005, 0.01, 0.05, 0.1, 0.5])

for rc in rotor_constant:
    x = np.arange(-100, 100, 1)
    y = _cf(x, rc)

    seaborn.lineplot(
        x=x, 
        y=y,
        ax=ax,
        label=r'$C_b = {}$'.format(rc))
        
ROOT_FOLDER = '../../../docs/packages/uuv_simulator/docs/images/actuators/'
plt.savefig(os.path.join(ROOT_FOLDER, 'cf_basic.png'), bbox_inches='tight')
plt.show()