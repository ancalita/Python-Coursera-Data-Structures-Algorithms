Building Roads to Connect Cities
Problem Introduction
In this problem, the goal is to build roads between some pairs of the given cities such that there is a path between any two cities and the total length of the roads is minimized.

Task. Given n points on a plane, connect them with segments of minimum total length such that there is a path between any two points.
Recall that the length of a segment with endpoints (x1,y1) and (x2,y2) is equal to 􏰢sqrt((x1 − x2)^2 + (y1 − y2)^2).
Input Format. The first line contains the number n of points. Each of the following n lines defines a point (xi, yi).
Constraints. 1 ≤ n ≤ 200; −10^3 ≤ xi,yi ≤ 10^3 are integers. All points are pairwise different, no three points lie on the same line.
Output Format. Output the minimum total length of segments.
The absolute value of the difference between the answer of your program and the optimal value should be at most 10^−6. 
To ensure this, output your answer with at least seven digits after the decimal point (otherwise your answer, while being computed correctly, can turn out to be wrong because of rounding issues).
