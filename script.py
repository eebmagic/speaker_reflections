import math
from matplotlib import pyplot as plt
from IPython.display import HTML
import matplotlib.animation as animation

def wave(x, t=0):
    y = math.sin((x/5) - (t/10))
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
    total_frames = 150
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
    frames = []
    for t in range(0, total_frames):
        Z = []
        for y in Y:
            row = []
            for x in X:
                curr = (x, y)
                z = get_z(curr, source, t=t)
                row.append(z)
            Z.append(row)
        frames.append(Z)

    # Animation settings
    fig, ax = plt.subplots()
    im = ax.imshow(frames[0])

    def init():
        im.set_data(frames[0])
        return (im,)

    def animate(i):
        data_slice = frames[i]
        im.set_data(data_slice)
        return (im,)

    # Generate and export animation to file
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(frames), interval=50, blit=True)
    anim.save("OUTPUT.mp4")
