from collections import OrderedDict
import matplotlib.pyplot as plt

class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, 'lightgray', label='Polygon')

    def add_boarder(self, xs, ys):
        plt.plot(xs, ys, 'salmon', label = 'boarder')

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

# Create a function that takes a CSV file and creates a list of points.
# This may be reused also to read the list of testing points.
if __name__ == "__main__":

    #Empty lists for coordinates of points and polygons to go into
    coordinatex = []
    coordinatey = []
    shapex = []
    shapey = []
    coordinates = []
    xinside = []
    sample_output =[]
    boundbox_output = []

# A class containing the methods to import data from a csv file and convert it
# into points, polygon and obtain coordinates in [x,y] form


    class File_reader:

        def read_points(filename):
            with open(filename, 'r') as f:
                lines = f.readlines()[1:]
                for line in lines:
                    line = line.strip().split(',')
                    coordinatex.append(float(line[1]))
                    coordinatey.append(float(line[2]))

        def read_polygon(filename):
            with open(filename, 'r') as f:
                lines = f.readlines()[1:]
                for line in lines:
                    line = line.strip().split(',')
                    shapex.append(float(line[1]))
                    shapey.append(float(line[2]))

        def create_coordinates(filename):
            with open(filename, 'r') as f:
                lines = f.readlines()[1:]
                for line in lines:
                    line = line.strip().split(',')
                    coordinates.append(line[1:3])

        def read_sample_output(filename):
            with open(filename, 'r') as f:
               lines = f.readlines()[1:]
            for line in lines:
                line = line.strip().split(',')
                sample_output.append(str(line[1]))

    # Read the files
    File_reader.read_points("input.csv")
    File_reader.read_polygon("polygon.csv")
    File_reader.create_coordinates("input.csv")
    File_reader.read_sample_output("sample_output.csv")

    # Convert strings to floats
    coordinates = [[float(float(j)) for j in i] for i in coordinates]
    # print(coordinates)

    x_min = 0
    x_max = 4
    y_min = 0
    y_max = 7

    # Define values to define a minimum and maximum boundry box.
    boundboxx = [0, 0, 4, 4, 0]
    boundboxy = [0, 7, 7, 0, 0]

    # def point_location_generator:
    for i in range(len(coordinates)):
        if x_min < (coordinatex[i]) < x_max and y_min < (coordinatey[i]) < y_max:
            boundbox_output.append("inside")
        elif x_min == coordinatex[i] and y_min < coordinatey[i] < y_max:
            boundbox_output.append("boundary")
        elif x_max == coordinatex[i] and y_min < coordinatey[i] < y_max:
            boundbox_output.append("boundary")
        elif y_min == coordinatey[i] and x_min < coordinatex[i] < x_max:
            boundbox_output.append("boundary")
        elif y_max == coordinatey[i] and x_min < coordinatex[i] < x_max:
            boundbox_output.append("boundary")
        else:
            boundbox_output.append("outside")



    # Plots visualised through the matplotlib module
    plotter = Plotter()
    plotter.add_point(coordinatex[1], coordinatey[1], boundbox_output[1])
    plotter.add_point(coordinatex[2], coordinatey[2], boundbox_output[2])
    plotter.add_point(coordinatex[3], coordinatey[3], boundbox_output[3])
    plotter.add_point(coordinatex[4], coordinatey[4], boundbox_output[4])
    plotter.add_point(coordinatex[5], coordinatey[5], boundbox_output[5])
    plotter.add_point(coordinatex[6], coordinatey[6], boundbox_output[6])
    plotter.add_point(coordinatex[7], coordinatey[7], boundbox_output[7])
    plotter.add_point(coordinatex[8], coordinatey[8], boundbox_output[8])
    plotter.add_point(coordinatex[9], coordinatey[9], boundbox_output[9])
    plotter.add_point(coordinatex[10], coordinatey[10], boundbox_output[10])
    plotter.add_point(coordinatex[11], coordinatey[11], boundbox_output[11])
    plotter.add_point(coordinatex[12], coordinatey[12], boundbox_output[12])
    plotter.add_point(coordinatex[13], coordinatey[13], boundbox_output[13])
    plotter.add_point(coordinatex[14], coordinatey[14], boundbox_output[14])
    plotter.add_point(coordinatex[15], coordinatey[15], boundbox_output[15])
    plotter.add_point(coordinatex[16], coordinatey[16], boundbox_output[16])
    plotter.add_point(coordinatex[17], coordinatey[17], boundbox_output[17])
    plotter.add_point(coordinatex[18], coordinatey[18], boundbox_output[18])
    plotter.add_point(coordinatex[19], coordinatey[19], boundbox_output[19])
    plotter.add_point(coordinatex[20], coordinatey[20], boundbox_output[20])
    plotter.add_point(coordinatex[21], coordinatey[21], boundbox_output[21])
    plotter.add_point(coordinatex[22], coordinatey[22], boundbox_output[22])
    plotter.add_point(coordinatex[23], coordinatey[23], boundbox_output[23])
    plotter.add_point(coordinatex[24], coordinatey[24], boundbox_output[24])
    plotter.add_point(coordinatex[25], coordinatey[25], boundbox_output[25])
    plotter.add_point(coordinatex[26], coordinatey[26], boundbox_output[26])
    plotter.add_point(coordinatex[27], coordinatey[27], boundbox_output[27])
    plotter.add_point(coordinatex[28], coordinatey[28], boundbox_output[28])
    plotter.add_point(coordinatex[29], coordinatey[29], boundbox_output[29])
    plotter.add_point(coordinatex[30], coordinatey[30], boundbox_output[30])
    plotter.add_point(coordinatex[31], coordinatey[31], boundbox_output[31])
    plotter.add_point(coordinatex[31], coordinatey[31], boundbox_output[31])
    plotter.add_point(coordinatex[32], coordinatey[32], boundbox_output[32])
    plotter.add_point(coordinatex[33], coordinatey[33], boundbox_output[33])
    plotter.add_point(coordinatex[33], coordinatey[33], boundbox_output[33])
    plotter.add_point(coordinatex[34], coordinatey[34], boundbox_output[34])
    plotter.add_point(coordinatex[35], coordinatey[35], boundbox_output[35])
    plotter.add_point(coordinatex[36], coordinatey[36], boundbox_output[36])
    plotter.add_point(coordinatex[37], coordinatey[37], boundbox_output[37])
    plotter.add_point(coordinatex[38], coordinatey[38], boundbox_output[38])
    plotter.add_point(coordinatex[39], coordinatey[39], boundbox_output[39])
    plotter.add_point(coordinatex[40], coordinatey[40], boundbox_output[40])
    plotter.add_point(coordinatex[41], coordinatey[41], boundbox_output[41])
    plotter.add_point(coordinatex[42], coordinatey[43], boundbox_output[43])
    plotter.add_point(coordinatex[44], coordinatey[44], boundbox_output[44])
    plotter.add_point(coordinatex[45], coordinatey[45], boundbox_output[45])
    plotter.add_point(coordinatex[46], coordinatey[46], boundbox_output[46])
    plotter.add_point(coordinatex[47], coordinatey[47], boundbox_output[47])
    plotter.add_point(coordinatex[48], coordinatey[48], boundbox_output[48])
    plotter.add_point(coordinatex[49], coordinatey[49], boundbox_output[49])
    plotter.add_point(coordinatex[50], coordinatey[50], boundbox_output[50])
    plotter.add_point(coordinatex[60], coordinatey[60], boundbox_output[60])
    plotter.add_point(coordinatex[61], coordinatey[61], boundbox_output[61])
    plotter.add_point(coordinatex[62], coordinatey[62], boundbox_output[62])
    plotter.add_point(coordinatex[63], coordinatey[63], boundbox_output[63])
    plotter.add_point(coordinatex[64], coordinatey[64], boundbox_output[64])
    plotter.add_point(coordinatex[65], coordinatey[65], boundbox_output[65])
    plotter.add_point(coordinatex[66], coordinatey[66], boundbox_output[66])
    plotter.add_point(coordinatex[67], coordinatey[67], boundbox_output[67])
    plotter.add_point(coordinatex[68], coordinatey[68], boundbox_output[68])
    plotter.add_point(coordinatex[69], coordinatey[69], boundbox_output[69])
    plotter.add_point(coordinatex[70], coordinatey[70], boundbox_output[70])
    plotter.add_point(coordinatex[68], coordinatey[68], boundbox_output[68])
    plotter.add_point(coordinatex[68], coordinatey[68], boundbox_output[68])
    plotter.add_point(coordinatex[68], coordinatey[68], boundbox_output[68])




    plotter.add_boarder(boundboxx, boundboxy)
    plotter.add_polygon(shapex, shapey)
    plotter.show()
