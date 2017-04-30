Detecting Anomalies in Currency Exchange Rates
Problem Description
You are given a list of currencies c1,c2,...,cn together with a list of ex- change rates: rij is the number of units of currency cj that one gets for one unit of ci.
You would like to check whether it is possible to start with one unit of some currency, perform a sequence of exchanges, and get more than one unit of the same currency.
In other words, you would like to find currencies ci1,ci2,...,cik such that ri1,i2 ·ri2,i3 ·rik−1,ik,rik,i1 >1.
For this, you construct the following graph: vertices are currencies c1, c2, . . . , cn, the weight of an edge from ci to cj is equal to − log rij .
There it suffices to check whether is a negative cycle in this graph.
Indeed, assume that a cycle ci → cj → ck → ci has negative weight.
This means that −(logcij + logcjk + logcki) < 0 and hence logcij + logcjk + logcki > 0.
This, in turn, means that rijrjkrki =2logcij2logcjk2logcki =2logcij+logcjk+logcki >1.
Task. Given an directed graph with possibly negative edge weights and with n vertices and m edges, check whether it contains a cycle of negative weight.
Input Format. A graph is given in the standard format.
Constraints. 1 ≤ n ≤ 10^3, 0 ≤ m ≤ 10^4, edge weights are integers of absolute value at most 103.
Output Format. Output 1 if the graph contains a cycle of negative weight and 0 otherwise.
