Computing the Minimum Cost of a Flight Problem Introduction
Now, you are interested in minimizing not the number of segments, but the total cost of a flight.
For this you construct a weighted graph: the weight of an edge from one city to another one is the cost of the corresponding flight.
Problem Description
Task. Given an directed graph with positive edge weights and with n vertices and m edges as well as two vertices u and v, compute the weight of a shortest path between u and v (that is, the minimum total weight of a path from u to v).
Input Format. A graph is given in the standard format.
The next line contains two vertices u and v.
Constraints. 1 ≤ n ≤ 10^3, 0 ≤ m ≤ 10^5, u ̸= v, 1 ≤ u,v ≤ n, edge weights are non-negative integers not
exceeding 10^3.
Output Format. Output the minimum weight of a path from u to v, or −1 if there is no path.
