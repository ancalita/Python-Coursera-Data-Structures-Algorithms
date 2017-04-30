Determining an Order of Courses
Problem Introduction
When you are sure that there are no cyclic dependencies in the given CS curriculum, you would like to find an order of all courses that is consistent with all dependencies.
For this, you find a topological ordering of the corresponding directed graph.
Problem Description
Task. Compute a topological ordering of a given directed acyclic graph (DAG) with n vertices and m edges.
Input Format. A graph is given in the standard format.
Constraints. 1 <= n <= 10^5, 0 <= m <= 10^5. The given graph is guaranteed to be acyclic.
Output Format. Output any topological ordering of its vertices.
(Many DAGs have more than just one topological ordering. You may output any of them.)
