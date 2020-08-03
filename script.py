import math
from matplotlib import pyplot as plt
from IPython.display import HTML
import matplotlib.animation as animation
from tqdm import tqdm

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
    distance = dist(p, source)

    z = wave(distance, t=t)
    return z


def get_z_with_wall(p, source, wall_x=100, t=0):
    reflected_source = ((2 * wall_x) - source[0], source[1])

    reflect_z = get_z(p, reflected_source, t=t)
    original_z = get_z(p, source, t=t)

    if dist(p, reflected_source) < 160:
        real_z = original_z + reflect_z
    else:
        real_z = original_z

    return real_z


def get_z_with_counteraction(p, source, wall_x, t=0, delay=5):
    reflected_source = ((2 * wall_x) - source[0], source[1])

    reflect_z = get_z(p, reflected_source, t=t)
    original_z = get_z(p, source, t=t)

    delay_z = get_z(p, source, t=t-delay)

    if dist(p, reflected_source) < 160:
        real_z = original_z + reflect_z + (-delay_z)
    else:
        real_z = original_z

    return real_z


if __name__ == "__main__":
    # Area settings
    width, height = 100, 100
    total_frames = 150
    source = (10, height/2)

    # Make points
    X, Y = [], []
    for x in range(0, width):
        X.append(x)

    for y in range(0, height):
        Y.append(y)

    # Make data at those points
    frames = []
    for t in tqdm(range(0, total_frames)):
        Z = []
        for y in Y:
            row = []
            for x in X:
                curr = (x, y)
                # z = get_z(curr, source, t=t)
                z = get_z_with_wall(curr, source, wall_x=width, t=t)
                # z = get_z_with_counteraction(curr, source, wall_x=width, t=t, delay=90/2)
                ref_source = ((2*width)-source[0], source[1])
                z -= get_z(curr, ref_source, t=t)
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
    output_name = "OUTPUT.mp4"
    anim.save(output_name)
    print(f"Saved animation to file: {output_name}")
