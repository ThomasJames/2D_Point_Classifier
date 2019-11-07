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



def minimum_bound(p_x, p_y, a_x, a_y):
    if min(a_x) < p_x < max(a_x) and min(a_y) < p_y < max(a_y):  # is the point within the bounds of the box
        out.append("inside")
    elif min(a_x) == p_x and min(a_y) <= p_y <= max(a_y):  # is the point.x on the min x axis and within the y
        out.append("boundary")
    elif max(a_x) == p_x and min(a_y) <= p_y <= max(a_y):  # is the point.x on the max x axis and within the y
        out.append("boundary")
    elif min(a_y) == p_y and min(a_x) <= p_x <= max(a_x):  # is the point.y on the min y axis within the x
        out.append("boundary")
    elif max(a_y) == p_y and min(a_x) <= p_x <= max(a_x):  # is the point.y on the max y axis within the x
        out.append("boundary")
    else:
        out.append("outside")  # else the point cant be inside or on boundry, therefore its outside





def minimum_bound(p_x, p_y, a_x, a_y):
    if min(a_x) < p_x < max(a_x) and min(a_y) < p_y < max(a_y):  # is the point within the bounds of the box
        return True
    elif min(a_x) == p_x and min(a_y) <= p_y <= max(a_y):
        return True
    elif max(a_x) == p_x and min(a_y) <= p_y <= max(a_y):
        return True
    elif min(a_y) == p_y and min(a_x) <= p_x <= max(a_x):
        return True
    elif max(a_y) == p_y and min(a_x) <= p_x <= max(a_x):
        return True
    else:
        return False  # else the point cant be inside or on boundry, therefore its outside




# def merge_lists(point_x, point_y, shape_x, shape_y):
#     s = []
#     p = []
#     for i in range(len(point_x)):
#         p.append(point_x, point_y)
#     for i in range(len(shape_x)):
#         s.append(shape_x, shape_y)


def ray_casting(p, s):
    n = len(s)-1
    counter = 0
    for i in range(n):
        if (s[i][1] <= p[1] and s[i+1][1] > p[1]) or (s[i][1] > p[1] and s[i+1][1] <= p[1]):
            vt = (p[1] - s[i][1]) / (s[i+1][1] - s[i][1])
            if p[0] < (s[i][0] + vt * (s[i+1][0] - s[i][0])):
                counter += 1
        i += 1
    return counter


def calculate_y(x, x1, y1, x2, y2):
    return (x - x1) / (x2 - x1) * (y2 - y1) + y1


def is_on_line(p_x, p_y, a_x, a_y, b_x, b_y):
    if not ((a_y <= p_y <= b_y or b_y <= p_y <= a_y) and (a_x <= p_x <= b_x or b_x <= p_x <= a_x)):
        return False
    elif a_x == b_x and p_x == a_x:
        return True
    elif a_x != b_x and calculate_y(p_x, a_x, a_y, b_x, b_y) == p_y:
        return True
    else:
        return False


def read_points(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()[1:]
        for line in lines:
            line = line.strip().split(',')
            point_x.append(float(line[1]))
            point_y.append(float(line[2]))


def read_polygon(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()[1:]
        for line in lines:
            line = line.strip().split(',')
            shape_x.append(float(line[1]))
            shape_y.append(float(line[2]))


def generate_coordinates(p_x, p_y):
    return list(map(lambda x, y:(x,y), p_x, p_y))


if __name__ == "__main__":

    point_x = []
    point_y = []
    shape_x = []
    shape_y = []
    s = []
    p = []


    read_polygon("polygon.csv")
    read_points("input.csv")

    p = generate_coordinates(point_x, point_y)
    s = generate_coordinates(shape_x, shape_y)

    location = [None] * len(point_x)    # Create an list with 100 empty values


    for i in range(len(location)):
        if (ray_casting(p[i], s)) % 2 != 0:
            location[i] = ("inside")
        else:
            location[i] = ("outside")
        for j in range(len(shape_x)-1):
            if is_on_line(point_x[i], point_y[i], shape_x[j], shape_y[j], shape_x[j+1], shape_y[j+1]) == True:
                location[i]=("boundary")




    plotter = Plotter()
    for i in range(len(point_x)):
        plotter.add_point(point_x[i], point_y[i], location[i])
    plotter.add_polygon(shape_x, shape_y)
    plotter.show()









    









    
   











    



















