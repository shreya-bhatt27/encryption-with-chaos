import numpy as np
import matplotlib.pyplot as plt

def langford_key(xinit, yinit, zinit, num_steps):
    dt = 0.01

    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    xs[0], ys[0], zs[0] = (xinit, yinit, zinit)

    a = 0.95
    b = 0.7
    c = 0.6
    d = 3.5
    e = 0.25
    f = 0.1

    for i in range(num_steps):
        xs[i + 1] = xs[i] + ((zs[i] - b) * xs[i] - d * ys[i]) * dt
        ys[i + 1] = ys[i] + (d * xs[i] + (zs[i] - b) * ys[i]) * dt
        zs[i + 1] = zs[i] + (c + a * zs[i] - zs[i]**3 / 3 - xs[i]**2 + f * zs[i] * xs[i]**3) * dt

    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # ax.plot(xs, ys, zs)
    # plt.show()

    return xs, ys, zs

# # Example usage:
# xinit, yinit, zinit = 0.1, 0.1, 0.1
# num_steps = 10000
# xs, ys, zs = langford_system(xinit, yinit, zinit, num_steps)

# # Plotting
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot(xs, ys, zs)
# plt.show()
