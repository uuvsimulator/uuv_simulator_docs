This package is the implementation of the algorithm presented in [`Tian and Zhang, 2010`](https://ieeexplore.ieee.org/abstract/document/5456812) for the generation of passive turbulent underwater plumes.

The plume is represented by a set of particles and to model the dynamics of the plume particles, the Lagrangian particle random walk approach from [`Mestres et al., 2003`](http://scimar.icm.csic.es/scimar/pdf/67/sm67n4379.pdf) is used.
The particles are generated from a pre-defined source position in space in batches at each iteration to ensure a steady flow.
Per default, 10 particles are generated at each iteration until the maximum number of particles is reached.

Each $i$-th particle has its position $(x_{i_k}, y_{i_k}, z_{i_k})$ described at the instant $t_k$ as:

$$
    x_k = x_{k - 1} + (u_a + u_t) \Delta t \\
    y_k = y_{k - 1} + (v_a + v_t) \Delta t \\
    z_k = z_{k - 1} + (w_a + w_b + w_t) \Delta t
$$

where $(u_a, v_a, w_a)$ are the particle's velocities due to the current velocity, $(u_t, v_t, w_t)$ are the particle's velocities due to turbulent diffusion, and $w_b$ is the vertical buoyant velocity that simulates the rise of the plume.

The plume is also limited to a box provided by the user. 
Once the particles reach the limits of the box, they are destroyed and it allows the same number of particles to be created in the source again.

# Turbulent diffusion velocity

The turbulent diffusion velocity $(u_t, v_t, w_t)$ is ruled by the turbulent diffusion coefficients $(d_u, d_v, d_w)$ given by the user and is computed as follows

$$
    u_t = 2 (0.5 - \text{rand}()) \sqrt{6 \frac{d_u}{\Delta t}} \\
    v_t = 2 (0.5 - \text{rand}()) \sqrt{6 \frac{d_v}{\Delta t}} \\
    w_t = 2 (0.5 - \text{rand}()) \sqrt{6 \frac{d_w}{\Delta t}} 
$$

$\text{rand()}$ being a random number from an uniform distribution generated in the interval $[0, 1]$ and $\Delta t$ being the simulation time step.

# Plume rise

The plume rise equation is used to compute the vertical buoyant velocity $w_b$. It is based on the experimental results presented in `Domenico, 1985` and can be written as

$$
    H(u, s, t) = 2.6 \left ( \frac{F t^2}{u} \right )^{1/3} (t^2 s + 4.3)^{-1/3}
$$

where $F$ is the buoyancy flux parameter and $s$ the stability parameters, and both can be tuned by the user, and $u$ is the magnitude of the current velocity on the horizontal plane. The resulting vertical buoyant velocity will be computed as follows

$$
    w_b = \frac{H(u, s, t + \Delta t) - H(u, s, t)}{\Delta t}
$$

# Bibliography

!!! note "`Tian and Zhang, 2010`"
    Yu Tian and Aiqun Zhang, "Simulation environment and guidance system
    for AUV tracing chemical plume in 3-dimensions," 2010 2nd International
    Asia Conference on Informatics in Control, Automation and Robotics
    (CAR 2010), Mar. 2010.

!!! note "`Mestres et al., 2003`"
    M. Mestres et al., "Modelling of the Ebro River plume. Validation with
    field observations," Scientia Marina, vol. 67, no. 4, pp. 379-391,
    Dec. 2003.

!!! note "`Domenico, 1985`"
    Anfossi, Domenico. "Analysis of plume rise data from five TVA steam
    plants." Journal of climate and applied meteorology 24.11 (1985):
    1225-1236.