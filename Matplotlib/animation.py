import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import seaborn as sns

# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = plt.plot([], [], 'ro')
#
#
# def init():
#     ax.set_xlim(0, 2*np.pi)
#     ax.set_ylim(-1, 1)
#     return ln,
#
#
# def update(frame):
#     xdata.append(frame)
#     ydata.append(np.sin(frame))
#     ln.set_data(xdata, ydata)
#     return ln,
#
#
# ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
#                     init_func=init, blit=True)
#
# plt.show()
#
#
# ########################################
#
# fig = plt.figure()
# # creating a subplot
# ax1 = fig.add_subplot(1, 1, 1)
#
#
# def animate(i):
#     data = open('stock.txt', 'r').read()
#     lines = data.split('\n')
#     xs = []
#     ys = []
#
#     for line in lines:
#         x, y = line.split(',')  # Delimiter is comma
#         xs.append(float(x))
#         ys.append(float(y))
#
#     ax1.clear()
#     ax1.plot(xs, ys)
#
#     plt.xlabel('Date')
#     plt.ylabel('Price')
#     plt.title('Live graph with matplotlib')
#
#
# ani = animation.FuncAnimation(fig, animate, interval=1000)
# plt.show()

##################################

# Get the data (csv file is hosted on the web)
url = 'https://python-graph-gallery.com/wp-content/uploads/volcano.csv'
data = pd.read_csv(url)

# Transform it to a long format
df = data.unstack().reset_index()
df.columns = ["X", "Y", "Z"]

# And transform the old column name in something numeric
df['X'] = pd.Categorical(df['X'])
df['X'] = df['X'].cat.codes

# We are going to do 20 plots, for 20 different angles
for angle in range(70, 210, 2):
    # Make the plot
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)

    ax.view_init(30, angle)

    filename = 'Volcano_step' + str(angle) + '.png'
    plt.savefig(filename, dpi=96)
    plt.gca()
