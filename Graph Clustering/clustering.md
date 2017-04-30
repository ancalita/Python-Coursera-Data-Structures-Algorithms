Clustering
Clustering is a fundamental problem in data mining.
The goal is to partition a given set of objects into subsets (or clusters) in such a way that any two objects from the same subset are close (or similar) to each other, while any two objects from different subsets are far apart.
Task. Given n points on a plane and an integer k, compute the largest possible value of d such that the given points can be partitioned into k non-empty subsets in such a way that the distance between any two points from different subsets is at least d.
Input Format. The first line contains the number n of points.
Each of the following n lines defines a point (xi,yi). The last line contains the number k of clusters.
Constraints. 2 ≤ k ≤ n ≤ 200; −10^3 ≤ xi, yi ≤ 10^3 are integers. All points are pairwise different.
Output Format. Output the largest value of d.
The absolute value of the difference between the answer of your program and the optimal value should be at most 10^−6.
To ensure this, output your answer with at least seven digits after the decimal point (otherwise your answer, while being computed correctly, can turn out to be wrong because of rounding issues).
