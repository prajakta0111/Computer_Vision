import numpy as np
from math import *
import matplotlib
import matplotlib.pyplot as plt
# import matplotlib.animation as animation
import matplotlib.pyplot as plt
plt.rcParams['animation.ffmpeg_path'] = '/usr/bin/ffmpeg'
import matplotlib.animation as animation
# this function gets called every time a new frame should be generated.


def takeoff(frame_number):
    global tx, ty, tz, compass, tilt, twist
    ty += 20
    if frame_number > 10 and frame_number < 40:
        ty += 10
        tz = tz + tz*0.2
    if frame_number > 40:
        ty += 10
        tx -= 30
        twist += 1.5
    # if frame_number > 10 and frame_number < 30: 
    #     tz -= 7
    # if frame_number > 30:
    #     tz -= 10

    f = 0.002
    transformation = np.array([[f, 0, 0], [0, f, 0], [0, 0, 1]])
    transformation = np.matmul(transformation, np.array([[1, 0, 0], [0, np.cos(tilt), -np.sin(tilt)], [0, np.sin(tilt), np.cos(tilt)]]))
    transformation = np.matmul(transformation, np.array([[np.cos(twist), 0, -np.sin(twist)], [0, 1, 0], [np.sin(twist), 0, np.cos(twist)]]))
    transformation = np.matmul(transformation, np.array([[np.cos(compass
                                                                 ), -np.sin(compass), 0], [np.sin(compass), np.cos(compass), 0], [0, 0, 1]]))
    transformation = np.matmul(transformation, np.array([[1, 0, 0, tx], [0, 1, 0, ty], [0, 0, 1, tz]]))

    pr = []
    pc = []
    for p in pts3:
        temp = np.array([p[0], p[1], p[2], 1])
        temp = np.matmul(transformation, temp)
        if temp[-1] < 0:

            pr += [temp[0] / temp[-1] + 1e-5]

            pc += [temp[1] / temp[-1] + 1e-5]

    plt.cla()
    plt.gca().set_xlim([-0.002, 0.002])
    plt.gca().set_ylim([-0.002, 0.002])
    line, = plt.plot(pr, pc, 'k', linestyle="", marker=".", markersize=2)
    return line,



# load in 3d point cloud
with open("airport.pts", "r") as f:
    pts3 = [[float(x) for x in l.split(" ")] for l in f.readlines()]


# initialize plane pose (translation and rotation)
(tx, ty, tz) = (0, -30, -10)
(compass, tilt, twist) = (0, pi/2, 0)

# takeoff(50)
# # create animation!
fig, ax = plt.subplots()
frame_count = 50

ani = animation.FuncAnimation(fig, takeoff, frames=range(0, frame_count))

# uncomment if you want to save your animation as a movie. :)
ani.save("movie.mp4")

# plt.show()
