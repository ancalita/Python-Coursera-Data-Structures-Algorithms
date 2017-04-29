Compute tree height
Problem Introduction
Trees are used to manipulate hierarchical data such as hierarchy of categories of a retailer or the directory structure on your computer.
They are also used in data analysis and machine learning both for hierarchical clustering and building complex predictive models, including some of the best-performing in practice algorithms like Gradient Boosting over Decision Trees and Random Forests.
Problem Description
Task: Compute and output its height. Recall that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.
Input Format. The first line contains the number of vertices 𝑛. The second line contains 𝑛 integer numbers from −1 to 𝑛−1 — parents of vertices. If the 𝑖-th one of them (0 ≤ 𝑖 ≤ 𝑛−1) is −1, vertex 𝑖 is the root, otherwise it’s 0-based index of the parent of 𝑖-th vertex.
It is guaranteed that there is exactly one root. It is guaranteed that the input represents a tree.
Constraints. 1 ≤ 𝑛 ≤ 105.
Output Format. Output the height of the tree.
