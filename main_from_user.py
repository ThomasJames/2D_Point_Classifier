from plotter import Plotter
import matplotlib.pyplot as plt
from main_from_file import ReadFile
from main_from_file import locate_points
from main_from_file import compute_y
from main_from_file import minimum_bound
from main_from_file import ray_casting
from main_from_file import is_on_line
from main_from_file import generate_coordinates
from main_from_file import locate_point

if __name__ == "__main__":
    shape_x = []
    shape_y = []
    point_coordinates = []
    location = [None] * 1
    point_x = float(input("input the x coordinate: "))
    point_y = float(input("input the y coordinate: "))
    point_coordinates = (point_x, point_y)
    print(point_coordinates)

    ReadFile.access_csv_file("polygon.csv", shape_x, shape_y)
    shape_coordinates = generate_coordinates(shape_x, shape_y)

    locate_point(point_x, point_y, shape_x, shape_y, point_coordinates, shape_coordinates, location)

    print("The value point you have selected was ", str(point_coordinates), " This sits on the ",  (location))



    # Points plotted with locations
    plotter = Plotter()
    plotter.add_point(point_x, point_y, location[0])
    plotter.add_polygon(shape_x, shape_y)
    plt.xlabel("(x)")
    plt.ylabel("(y)")
    plt.title("what is the point?")
    plotter.show()
