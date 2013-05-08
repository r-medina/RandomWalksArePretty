import pylab as pl
from sys import stdout
import os

steps = 100000

# generates a pseudo-random number between -1 and 1
random_step = lambda: pl.random()-pl.random()

# prints percent of task completed
def percent(x):
    if not (x % 100):
        stdout.write("\r{:.1%}".format(float(x+1)/float(steps)))
        stdout.flush()

# arrays of x and y positions
x = pl.zeros(steps)
y = pl.zeros(steps)

# evaluate all the positions before graphing
print "Steps percent complete:"
for i in range(steps):
    if (i > 0):
        x[i] = x[i-1]+random_step()
        y[i] = y[i-1]+random_step()
    percent(i)
print

# graphing steps
pl.figure(frameon=False)
pl.hold(True)
pl.axes().set_aspect('equal')
# next two lines get rid of x and y ticks
pl.gca().axes.get_xaxis().set_visible(False)
pl.gca().axes.get_yaxis().set_visible(False)
# array with equally spaced values between 0 and 255 for selecting color
colors = pl.linspace(0,255,steps)
# grabs the matplotlib winter color map
cm = pl.get_cmap('gist_rainbow')
# alpha
# linewidth
print "Graph percent complete:"
for i in range(steps-1):
    pl.plot(x[i:i+2],y[i:i+2], \
            linewidth=.4,c=cm(int(colors[i])),alpha=.2)
    percent(i)
print
# the picture's names are just consecutive integers finds the first
# integer that isn't the name of one of the pictures in the out/
# directory already
i = 0
while (os.path.exists("../out/{:02d}.png".format(i))): i+=1
print "Saving..."
pl.savefig("../out/{:02d}".format(i),dpi=800, bbox_inches='tight', \
           pad_inches=0)
