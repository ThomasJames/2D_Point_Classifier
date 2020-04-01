# Classifying_Coordinates_PIP
Program to take a coordinate, and return the location with respect to a polygon. 

# Minimum Bounding 
PiP is a computationally intensive operation. Therefore, it is common to first
get the MBR of a polygon and test whether the point lies inside this rectangle.
For the purposes of this assignment, the MBR can be found by simply taking
the minimum and maximum of both coordinates of the the polygon. If a given
point lies outside this rectangle, then it is definitely outside the polygon and
there is no need to proceed to the full PiP algorithm.

# Ray Casting 
The Ray Casting Algorithm - The RCA involves drawing a straight line
(in any direction) from the test point, and counting how many times it crosses
the boundary of the polygon. If the line crosses the boundary an odd number of
times then the point lies inside the polygon. If the line crosses the boundary an
even number of times then the point lies outside the polygon.

# Point on line 
If l2 is also parallel to the x-axis:
– If y1 = y2 then the problem reduces to checking if x1 is
less or equal than x3 or x4; If it is, then the lines are
crossing on an infinite number of points.
– If not then the lines are not crossing.
• In the other case:
– If y1 is between y3 and y4 the problem reduces to
checking if x is greater or equal than x1; If it is, then the
lines are crossing on one point.
– If not then the lines are not crossing.

# main_from_file.py
1. Read a list of coordinates from a CSV file and create a polygon;
2. Read a list of coordinates from a file and create a list of testing points;
3. Categorize these points into: “inside”, “outside” and “boundary”;
4. Output the result of each point in a CSV file;
5. Plot the points and polygon in a plot window.

# main_from_user.py
1. Read a list of coordinates from a CSV file and create a polygon;
2. Read a list of coordinates from shell;
3. Categorize this point into “inside”, “outside” and “boundary”;
4. Plot the point and polygon in a plot window.





