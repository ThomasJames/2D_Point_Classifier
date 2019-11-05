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


    #Class containing a selection of methods

    class File_reader:

        #Method to read coordinates
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

    File_reader.create_coordinates("polygon.csv")
    print(coordinates)


    # values to define a minimum and maximum to draw the boundry box in plotter .
    boundboxx = [0, 0, 4, 4, 0]
    boundboxy = [0, 7, 7, 0, 0]

    # Values to define the min/max boundries of the maximum boundry box
    x_min = 0
    x_max = 4
    y_min = 0
    y_max = 7

    # work out a way to input the values of max and min to a method - To give a bounding of ay box
    # def point_location_generator:

    def minimumbound(x_min, x_max, y_min, y_max):
        for i in range(len(coordinatex)):
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


    minimumbound(0, 4, 0, 7)


    
    




    # Create a list from 1 - 100, that can be used for indexing of the
    count = 1
    id = []
    idstring = []
    while (count < 101):
        id.append(count)
        count = count + 1

    # Write the
    output_file = open("mbr_output.csv", "w")
    for i in boundbox_output:
        output_file.write(i + "\n")

######################################################################################################################################

    list = []
    # def polyboardercheck2(b):
    #     for i in range(19):
    #         if shapey[i] <= coordinatey[b] <= shapey[i+1]:
    #             if coordinatex[b] == shapex[i] or shapex[i+1]:
    #                 list.append("boundary")
    #                 break
    #             else:
    #                 if coordinatey[b] == (coordinatex[b] - shapex[i]) / (shapey[i+2] - shapey[i]) * (shapey[i+2] - shapey[i]) + shapey[i]:
    #                     list.append("boundary")
    #                     break
    #         else:
    #             list.append("unclassified")
    #             break


    def polyboardercheck2(b):
        for i in range(19):
            if shapey[i] <= coordinatey[b] <= shapey[i+1]:          # if point y is between the two y values of the line
                if coordinatex[b] == shapex[i] or shapex[i+1]:      # if point x is equal to one of the x values of the line
                    list.append("boundary")                         # add "boundry to the lsit"
                    break                                           # Break the loop
            elif shapex[i] <= coordinatex[b] <= shapex[i+1]:        # if point x is between the two x values of the line
                if coordinatey[b] == shapey[i] or shapey[i+1]:      # if point y is equal to  one of the y values of the line
                    list.append("boundry")                          # add "boundry to the lsit"
                    break                                           #break the lloop
                                                                    #If pointy is equal to x solved
            elif coordinatey == (coordinatex[b] - shapex[i]) / (shapey[i+2] - shapey[i]) * (shapey[i+2] - shapey[i]) + shapey[i]:
                        list.append("boundry")                      # add "boundry to the lsit"
                        break                                       # Break the loop
            else:
                list.append("unclassified")                         # The point is not on the line so we add "unclassified" to the lsit
                break

    for n in range(len(coordinatex)):
        polyboardercheck2(n)

        # Questions -
        # Why doesnt the control statement work/ Why is the elif staement skipping?
        # what do you do with the loop closure.
        #

    print(list)


 # Plots visualised through the matplotlib module
    plotter = Plotter()
    plotter.add_point(coordinatex[1], coordinatey[1], list[1])
    plotter.add_point(coordinatex[2], coordinatey[2], list[2])
    plotter.add_point(coordinatex[3], coordinatey[3], list[3])
    plotter.add_point(coordinatex[4], coordinatey[4], list[4])
    plotter.add_point(coordinatex[5], coordinatey[5], list[5])
    plotter.add_point(coordinatex[6], coordinatey[6], list[6])
    plotter.add_point(coordinatex[7], coordinatey[7], list[7])
    plotter.add_point(coordinatex[8], coordinatey[8], list[8])
    plotter.add_point(coordinatex[9], coordinatey[9], list[9])
    plotter.add_point(coordinatex[10], coordinatey[10], list[10])
    plotter.add_point(coordinatex[11], coordinatey[11], list[11])
    plotter.add_point(coordinatex[12], coordinatey[12], list[12])
    plotter.add_point(coordinatex[13], coordinatey[13], list[13])
    plotter.add_point(coordinatex[14], coordinatey[14], list[14])
    plotter.add_point(coordinatex[15], coordinatey[15], list[15])
    plotter.add_point(coordinatex[16], coordinatey[16], list[16])
    plotter.add_point(coordinatex[17], coordinatey[17], list[17])
    plotter.add_point(coordinatex[14], coordinatey[14], list[14])
    plotter.add_point(coordinatex[15], coordinatey[15], list[15])
    plotter.add_point(coordinatex[17], coordinatey[17], list[17])
    plotter.add_point(coordinatex[16], coordinatey[16], list[16])
    plotter.add_point(coordinatex[17], coordinatey[17], list[17])
    plotter.add_point(coordinatex[18], coordinatey[18], list[18])
    plotter.add_point(coordinatex[19], coordinatey[19], list[19])
    plotter.add_point(coordinatex[20], coordinatey[20], list[20])
    plotter.add_point(coordinatex[81], coordinatey[81], list[81])
    plotter.add_point(coordinatex[82], coordinatey[82], list[82])
    plotter.add_point(coordinatex[83], coordinatey[83], list[83])
    plotter.add_point(coordinatex[84], coordinatey[84], list[84])
    plotter.add_point(coordinatex[85], coordinatey[85], list[85])
    plotter.add_point(coordinatex[86], coordinatey[86], list[86])
    plotter.add_point(coordinatex[87], coordinatey[87], list[87])
    plotter.add_point(coordinatex[88], coordinatey[88], list[88])
    plotter.add_point(coordinatex[89], coordinatey[89], list[89])
    plotter.add_point(coordinatex[90], coordinatey[90], list[90])
    plotter.add_point(coordinatex[91], coordinatey[91], list[91])
    plotter.add_point(coordinatex[92], coordinatey[92], list[92])
    plotter.add_point(coordinatex[93], coordinatey[93], list[93])
    plotter.add_point(coordinatex[94], coordinatey[94], list[94])


    plotter.add_boarder(boundboxx, boundboxy)
    plotter.add_polygon(shapex, shapey)
    plotter.show()





    


    

















































































