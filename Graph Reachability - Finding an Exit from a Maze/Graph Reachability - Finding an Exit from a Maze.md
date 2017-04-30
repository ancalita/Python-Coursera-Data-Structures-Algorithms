Finding an Exit from a Maze
Problem Introduction
A maze is a rectangular grid of cells with walls between some of adjacent cells.
You would like to check whether there is a path from a given cell to a given exit from a maze where an exit is also a cell that lies on the border of the maze.
For this, you represent the maze as an undirected graph: vertices of the graph are cells of the maze, two vertices are connected by an undirected edge if they are adjacent and there is no wall between them.
Then, to check whether there is a path between two given cells in the maze, it suffices to check that there is a path between the corresponding two vertices in the graph.
Problem Description
Task. Given an undirected graph and two distinct vertices 𝑢 and 𝑣, check if there is a path between 𝑢 and 𝑣.
Input Format. An undirected graph with 𝑛 vertices and 𝑚 edges. The next line contains two vertices 𝑢
and 𝑣 of the graph.
Constraints. 2≤𝑛≤10^3;1≤𝑚≤10^3;1≤𝑢,𝑣≤𝑛;𝑢̸=𝑣.
Output Format. Output 1 if there is a path between 𝑢 and 𝑣 and 0 otherwise.
