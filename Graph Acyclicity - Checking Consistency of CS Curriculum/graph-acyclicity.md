Checking Consistency of CS Curriculum
Problem Introduction
A Computer Science curriculum specifies the prerequisites for each course as a list of courses that should be taken before taking this course.
You would like to perform a consistency check of the curriculum, that is, to check that there are no cyclic dependencies.
For this, you construct the following directed graph: vertices correspond to courses, there is a directed edge (u,v) is the course u should be taken before the course v.
Then, it is enough to check whether the resulting graph contains a cycle.
Problem Description
Task. Check whether a given directed graph with n vertices and m edges contains a cycle.
Input Format. A graph is given in the standard format.
Constraints. 1<=n<=10^3,0<=m<=10^3.
Output Format. Output 1 if the graph contains a cycle and 0 otherwise.
