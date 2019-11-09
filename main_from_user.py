from plotter import Plotter
import matplotlib.pyplot as plt
from main_from_file import ReadFile
from main_from_file import generate_coordinates
from main_from_file import locate_point

if __name__ == "__main__":

    shape_x = []
    shape_y = []
    point_coordinates = []
    location = [None] * 1  # Set variable for a single coordinate

    # Additional feature to ask user if they would like to use the default polygon, or another polygon.
    answer = input("Would you like to test the default polygon? (yes/no): ")
    if answer == None:
        ReadFile.access_csv_file("polygon.csv", shape_x, shape_y)
        shape_coordinates = generate_coordinates(shape_x, shape_y) # If no answer is given, then the default polygon is used
    if answer == "yes":
        ReadFile.access_csv_file("polygon.csv", shape_x, shape_y)  # If yes is given, the default polygon is used
        shape_coordinates = generate_coordinates(shape_x, shape_y)
    elif answer == "no":                                           # if no is given, a path is requested from the user
        ReadFile.access_csv_file(str(input("Ok, type in the csv path of your polygon: ")), shape_x, shape_y)
        shape_coordinates = generate_coordinates(shape_x, shape_y)
    else:
        print("Please enter yes or no.")  # Error handling function for if the input is not 'yes' or 'no'

    # Request user input for each x and y coordinate
    point_x = float(input("Input an x coordinate: "))
    point_y = float(input("Input a y coordinate: "))
    point_coordinates = (point_x, point_y)

    # Call the function to locate a single point
    locate_point(point_x, point_y, shape_x, shape_y, point_coordinates, shape_coordinates, location)

    # Prints a line of text with details of the input and the result
    print("The point you have selected was", str(point_coordinates), "This sits on the", (str(location)[1:-1]))

    # Points plotted with locations
    plotter = Plotter()
    plotter.add_point(point_x, point_y, location[0])
    plotter.add_polygon(shape_x, shape_y)
    plt.plot(shape_x, shape_y)
    plt.xlabel("(x)")
    plt.ylabel("(y)")
    plt.title("Wheres the point?")
    plotter.show()
