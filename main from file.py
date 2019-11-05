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


def compute_y(x, x1, y1, x2, y2):
    return (x - x1) / (x2 - x1) * (y2 - y1) + y1


def is_on_the_line(p_x, p_y, a_x, a_y, b_x, b_y):
    if not ((a_y <= p_y <= b_y or b_y <= p_y <= a_y) and (a_x <= p_x <= b_x or b_x <= p_x <= a_x)):  # if point y is between the two y values of the line
        return False
    elif a_x == b_x and p_x == a_x:
        return True
    elif a_x != b_x and compute_y(p_x, a_x, a_y, b_x, b_y) == p_y:
        return True
    else:
        return False


if __name__ == "__main__":

    # Empty lists for coordinates of points and polygons to go into
    point_x = []
    point_y = []
    shape_x = []
    shape_y = []
    boundbox_output = []


    # Class containing methods to read files
    class File_reader:

        # Method to read the points from a csv file and create lists from the second and third column
        def read_points(filename):
            with open(filename, 'r') as f:
                lines = f.readlines()[1:]
                for line in lines:
                    line = line.strip().split(',')
                    point_x.append(float(line[1]))  # values added to the empty shape list.
                    point_y.append(float(line[2]))

        # Method to read the points from a csv file and create lists from the
        def read_polygon(filename):
            with open(filename, 'r') as f:
                lines = f.readlines()[1:]
                for line in lines:
                    line = line.strip().split(',')
                    shape_x.append(float(line[1]))  # values added to the empty point list.
                    shape_y.append(float(line[2]))


    # Read the files from the class File_reader
    File_reader.read_points("input.csv")
    File_reader.read_polygon("polygon.csv")

    ########################################################################################################################
    # Minimum bounding Algorithm

    # values to define a minimum and maximum to draw the boundry box in plotter for this polygon.
    boundboxx = [0, 0, 4, 4, 0]
    boundboxy = [0, 7, 7, 0, 0]


    # work out a way to input the values of max and min to a method - To give a bounding of ay box
    # def point_location_generator:

    def minimumbound(x_min, x_max, y_min, y_max):
        for i in range(len(point_x)):
            if x_min < point_x[i] < x_max and y_min < point_y[i] < y_max:  # is the point within the bounds of the box
                boundbox_output.append("inside")
            elif x_min == point_x[i] and y_min <= point_y[
                i] <= y_max:  # is the point.x on the min x axis and within the y segment
                boundbox_output.append("boundary")
            elif x_max == point_x[i] and y_min <= point_y[
                i] <= y_max:  # is the point.x on the max x axis and within the y segment
                boundbox_output.append("boundary")
            elif y_min == point_y[i] and x_min <= point_x[
                i] <= x_max:  # is the point.y on the min y axis within the x segment
                boundbox_output.append("boundary")
            elif y_max == point_y[i] and x_min <= point_x[
                i] <= x_max:  # is the point.y on the max y axis within the x segment
                boundbox_output.append("boundary")
            else:
                boundbox_output.append("outside")  # else the point cant be inside or on boundry, therefore its outside


    minimumbound(0, 4, 0, 7)
    # Make an input function for this - with error handling function for if the box isn't square

    # The plotter function is used to plot the points.
    plotter = Plotter()
    for i in range(len(point_x)):
        plotter.add_point(point_x[i], point_y[i], boundbox_output[i])
        plotter.add_boarder(boundboxx, boundboxy)
        plotter.add_polygon(shape_x, shape_y)

    # plotter.add_boarder(boundboxx, boundboxy)
    # plotter.add_polygon(shape_x, shape_y)
    # plotter.show()

    # Create a list from 1 - 100, that can be used for creating an id list for the boundbox outpuy.
    count = 1
    id = []
    idstring = []
    while (count < 101):
        id.append(count)
        count = count + 1

    # Write the output to a csv file called mbr_output
    output_file = open("mbr_output.csv", "w")
    for i in boundbox_output:
        output_file.write(i + "\n")

    ########################################################################################################################

    # Point on a line algorithm

    boundary_locator = []

    boundary_locator = []


    def polyboardercheck2(b):
        for i in range(len(shape_x)-1):
            if not shape_y[i] <= point_y[b] <= shape_y[i + 1]:  # if point y is between the two y values of the line
                boundary_locator.append("unclassified")
            elif shape_x[i] == shape_x[i + 1] and point_x == shape_x[i]:
                boundary_locator.append("boundary")
            elif shape_x[i] != shape_x[i + 1] and compute_y(point_x[b], shape_x[i], shape_y[i], shape_x[i + 1], shape_y[i + 1]) == point_y[b]:
                boundary_locator.append("boundary")
            else:
                boundary_locator.append("unclassified")

    polyboardercheck2(0)

        # Queries -
        # Why doesnt the control statement work/ Why is the elif staement skipping?
        # what do you do with the loop closure.
        # how do you make a statement that says something is between - not taking into account direction


    # print(boundary_locator)

    # Plots visualised through the matplotlib module

    plotter = Plotter()
    for i in range(len(point_x)):
        plotter.add_point(point_x[i], point_y[i], boundary_locator[i])

    plotter.add_boarder(boundboxx, boundboxy)
    plotter.add_polygon(shape_x, shape_y)
    plotter.show()

    ######################################################################################################################

    intersection_list = []
    counter = 0


    def do_the_lines_intersect(a):
        for i in range(19):
            if shape_y[i] == shape_y[
                i + 1]:  # the polygon line is parallel to the x axis - therefore parallel to the ray
                intersection_list.append("no")  # Unless on boundry
                break
            elif point_y == shape_y[i]:
                if shape_x[i + 1] >= point_x[a] >= shape_x[i] or shape_x[i + 1] <= point_x[a] <= shape_x[i]:
                    intersection_list.append("The lines are crossing on an infinite number of points")
                    break
                else:
                    intersection_list.append("no")
                    break
            elif shape_y[i] <= point_y[a] <= shape_y[i] or shape_y[i] >= point_y[a] >= shape_y[i]:
                if point_x[a] >= shape_x[i]:
                    intersection_list.append("once")
                    break
                else:
                    intersection_list.append("no")
                    break


    for i in range(100):
        do_the_lines_intersect(i)
    print(intersection_list)

    # Queries
    # How can we create an infinite value
    # How can you count the number of times that the line will cross
