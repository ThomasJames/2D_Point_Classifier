# Classifying_Coordinates_PIP
Program to take a coordinate, and return the location with respect to a polygon. 
Three major functions were constructed;

1. Minimum bounding algorithm - Constructs a minimum bounding box around the polygon. All points located outside the bounding box are labeled as "outside" - points located inside the bounding box are labelled as 

2. The Ray Casting Algorithm - The RCA involves drawing a straight line
(in any direction) from the test point, and counting how many times it crosses
the boundary of the polygon. If the line crosses the boundary an odd number of
times then the point lies inside the polygon. If the line crosses the boundary an
even number of times then the point lies outside the polygon.

