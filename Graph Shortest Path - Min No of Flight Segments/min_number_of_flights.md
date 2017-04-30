Computing the Minimum Number of Flight Segments
Problem Introduction
You would like to compute the minimum number of flight segments to get from one city to another one.
For this, you construct the following undirected graph: vertices represent cities, there is an edge between two vertices whenever there is a flight between the corresponding two cities.
Then, it suffices to find a shortest path from one of the given cities to the other one.
Problem Description
Task. Given an undirected graph with n vertices and m edges and two vertices u and v, compute the length of a shortest path between u and v (that is, the minimum number of edges in a path from u to v).
Input Format. A graph is given in the standard format. The next line contains two vertices u and v.
Constraints. 2≤n≤10^5,0≤m≤10^5,u̸=v,1≤u,v≤n.
Output Format. Output the minimum number of edges in a path from u to v, or −1 if there is no path.
