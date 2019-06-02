import numpy as np
import os 
from matplotlib import pyplot as plt
import seaborn


def _zero_order(x, t):
    y = np.zeros(x.shape)
    y[np.nonzero(x >= t)[0]] = 450
    return y

fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111)

ax.set_xlabel('Time [s]')
ax.set_ylabel('Rotor angular velocity [rad / s]')
ax.set_title('Zero-order dynamic model')

ax.set_xlim([0, 4])
ax.set_ylim([0, 500])
ax.grid(True, which='major', color='gray', alpha=0.5, linestyle='--')

x = np.linspace(0, 4, 200)
y = _zero_order(x, 2)

seaborn.lineplot(
    x=x, 
    y=y,
    ax=ax)

ROOT_FOLDER = '../../../docs/packages/uuv_simulator/docs/images/actuators/'
plt.savefig(os.path.join(ROOT_FOLDER, 'dyn_zero_order.png'), bbox_inches='tight')
plt.show()