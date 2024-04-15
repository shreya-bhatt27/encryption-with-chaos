import numpy as np
import matplotlib.pyplot as plt

def rossler_key(xinit, yinit, zinit, num_steps):

    dt = 0.01

    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    xs[0], ys[0], zs[0] = (xinit, yinit, zinit)

    a = 0.2
    b = 0.2
    c = 5.7

    for i in range(num_steps):
        k1x = - (zs[i] + ys[i])
        k1y = (xs[i] + a * ys[i])
        k1z = (b + zs[i]*(xs[i]-c))

        k2x = - (zs[i] + ys[i] + 0.5 * dt * k1x)
        k2y = (xs[i] + 0.5 * dt * k1y + a * (ys[i] + 0.5 * dt * k1y))
        k2z = (b + (zs[i] + 0.5 * dt * k1z) * ((xs[i] + 0.5 * dt * k1x) - c))

        k3x = - (zs[i] + ys[i] + 0.5 * dt * k2x)
        k3y = (xs[i] + 0.5 * dt * k2y + a * (ys[i] + 0.5 * dt * k2y))
        k3z = (b + (zs[i] + 0.5 * dt * k2z) * ((xs[i] + 0.5 * dt * k2x) - c))

        k4x = - (zs[i] + ys[i] + dt * k3x)
        k4y = (xs[i] + dt * k3y + a * (ys[i] + dt * k3y))
        k4z = (b + (zs[i] + dt * k3z) * ((xs[i] + dt * k3x) - c))

        xs[i + 1] = xs[i] + (dt / 6) * (k1x + 2 * k2x + 2 * k3x + k4x)
        ys[i + 1] = ys[i] + (dt / 6) * (k1y + 2 * k2y + 2 * k3y + k4y)
        zs[i + 1] = zs[i] + (dt / 6) * (k1z + 2 * k2z + 2 * k3z + k4z)

    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # ax.plot(xs, ys, zs)
    # plt.show()

    return xs, ys, zs