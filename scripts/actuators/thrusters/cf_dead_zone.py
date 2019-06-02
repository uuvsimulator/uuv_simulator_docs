import numpy as np
import os 
from matplotlib import pyplot as plt
import seaborn


delta_l = -30*30
delta_r = 30*30

def _dead_zone(x, rotor_constant):
    thrust = np.zeros(x.size)
    filter = x * np.abs(x) <= delta_l
    thrust[np.nonzero(filter)[0]] = rotor_constant * (x[np.nonzero(filter)[0]] * np.abs(x[np.nonzero(filter)[0]]) - delta_l)
    filter = x * np.abs(x) >= delta_r
    thrust[np.nonzero(filter)[0]] = rotor_constant * (x[np.nonzero(filter)[0]] * np.abs(x[np.nonzero(filter)[0]]) - delta_r)
    return thrust


fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111)

ax.set_xlabel('Rotor angular velocity [rad / s]')
ax.set_ylabel('Thrust [N]')
ax.set_title('Thruster dead-zone conversion function')

ax.set_xlim([-100, 100])
ax.set_ylim([-500, 500])
ax.grid(True, which='major', color='gray', alpha=0.5, linestyle='--')

rotor_constant = np.array([0.001, 0.005, 0.01, 0.05, 0.1, 0.5])

for rc in rotor_constant:
    x = np.arange(-100, 100, 1)
    y = _dead_zone(x, rc)
    
    seaborn.lineplot(
        x=x, 
        y=y,
        ax=ax,
        label=r'$C_R = C_L = {}$'.format(rc))

ROOT_FOLDER = '../../../docs/packages/uuv_simulator/docs/images/actuators/'
plt.savefig(os.path.join(ROOT_FOLDER, 'cf_dead_zone.png'), bbox_inches='tight')
plt.show()