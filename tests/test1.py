from elemental import optimizer
import numpy as np
import matplotlib.pyplot as plt

def x(_x):
    r, theta, fai = _x
    return r * np.cos(theta) * np.cos(fai)


def y(_x):
    r, theta, fai = _x
    return r * np.cos(theta) * np.sin(fai)


def z(_x):
    r, theta, fai = _x
    return r * np.sin(theta)


if __name__ == "__main__":

    opt = optimizer.Ray()

    opt.add_parameter('r', .5, 0, 1)
    opt.add_parameter('theta', 0, -np.pi/2, np.pi/2)
    opt.add_parameter('fai', 0, 0, 2*np.pi)
    opt.add_objective('x', x)

    opt.main()

    print(opt.history.data)


