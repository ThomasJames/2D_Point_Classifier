from collections import OrderedDict
import matplotlib.pyplot as plt


class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, 'lightgray', label='Polygon')

    def add_boarder(self, xs, ys):
        plt.plot(xs, ys, 'salmon', label='boarder')

    def add_point(self, x, y, kind=None):
        if kind == "outside":
            plt.plot(x, y, "ro", label='Outside')
        elif kind == "boundary":
            plt.plot(x, y, "bo", label='Boundary')
        elif kind == "inside":
            plt.plot(x, y, "go", label='Inside')
        else:
            plt.plot(x, y, "ko", label='Unclassified')

    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        plt.show()


def compute_y(x, x1, y1, x2, y2):  # The auguments for the equation for a point on a line.
    return (x - x1) / (x2 - x1) * (y2 - y1) + y1  # The auguments for a equation.


# Function to test parameters and return whether the point is on a line True / False
def is_on_the_line(p_x, p_y, a_x, a_y, b_x, b_y):
    if not ((a_y <= p_y <= b_y or b_y <= p_y <= a_y) and (
            a_x <= p_x <= b_x or b_x <= p_x <= a_x)):  # If point y is not between the x values and y values
        return False
    elif a_x == b_x and p_x == a_x:  # If
        return True
    elif a_x != b_x and compute_y(p_x, a_x, a_y, b_x, b_y) == p_y:
        return True
    else:
        return False


def is_point_outside_minimum_bound(p_x, p_y, a_x, a_y):
    if min(a_x) < p_x < max(a_x) and min(a_y) < p_y < max(a_y):  # is the point within the bounds of the box
        out.append("inside")
    elif min(a_x) == p_x and min(a_y) <= p_y <= max(a_y):  # is the point.x on the min x axis and within the y segment
        out.append("boundary")
    elif max(a_x) == p_x and min(a_y) <= p_y <= max(a_y):  # is the point.x on the max x axis and within the y segment
        out.append("boundary")
    elif min(a_y) == p_y and min(a_x) <= p_x <= max(a_x):  # is the point.y on the min y axis within the x segment
        out.append("boundary")
    elif max(a_y) == p_y and min(a_x) <= p_x <= max(a_x):  # is the point.y on the max y axis within the x segment
        out.append("boundary")
    else:
        out.append("outside")  # else the point cant be inside or on boundry, therefore its outside


# Class containing methods to read files
class File_reader:

    # Method to read the points from a csv file and create lists from the second and third col
    def read_points(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()[1:]
            for line in lines:
                line = line.strip().split(',')
                p_x.append(float(line[1]))  # values added to the empty shape list.
                p_y.append(float(line[2]))

                # Method to read the points from a csv file and create lists from the

    def read_polygon(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()[1:]
            for line in lines:
                line = line.strip().split(',')
                a_x.append(float(line[1]))  # values added to the empty point list.
                a_y.append(float(line[2]))


if __name__ == "__main__":

    p_x = []
    p_y = []
    a_x = []
    a_y = []
    out = []


    File_reader.read_polygon("polygon.csv")
    File_reader.read_points("input.csv")

    for i in range(len(p_y)):
        is_point_outside_minimum_bound(p_x[i], p_y[i], a_x, a_y)

    for i in range()
        
    print(out)

    plotter = Plotter()
    for i in range(len(p_y)):
        plotter.add_point(p_x[i], p_y[i], out[i])
    plotter.add_polygon(a_x, a_y)
    plotter.show()
    

    

    

    
   