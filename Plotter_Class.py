from collections import OrderedDict
import matplotlib.pyplot as plt

class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, 'lemonchiffon', label='Polygon')

    def add_point(self, x, y, kind=None):
        if kind == "outside":
            plt.plot(x, y, "cx", label='Outside')
        elif kind == "boundary":
            plt.plot(x, y, "ro", label='Boundary')
        elif kind == "inside":
            plt.plot(x, y, "g*", label='Inside')
        else:
            plt.plot(x, y, "ko", label='Unclassified')

    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        plt.show()

