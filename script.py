import math
from matplotlib import pyplot as plt

def wave(x, t=0):
    y = math.sin((x/5) + t)
    return y


def dist(a, b):
    ax, ay = a
    bx, by = b

    x = (bx - ax) ** 2
    y = (by - ay) ** 2
    d = math.sqrt(x + y)

    return d


def get_z(p, source, t=0):
    px, py = p
    distance = dist(p, source)

    z = wave(distance, t=t)
    return z


if __name__ == "__main__":
    # Area settings
    width, height = 100, 100
    source = (-40, 0)

    # Make points
    X, Y = [], []
    for i in range(0, width):
        x = i - (width/2)
        X.append(x)

    for j in range(0, height):
        y = j - (height/2)
        Y.append(y)

    # Make data at those points
    Z = []
    for y in Y:
        row = []
        for x in X:
            curr = (x, y)
            z = get_z(curr, source)
            row.append(z)
        Z.append(row)

    # Plot the data
    plt.imshow(Z, extent=[0, 50, 0, 50], origin='center', cmap='RdBu')
    plt.colorbar()
    plt.show()