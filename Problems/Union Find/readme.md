# Union Find | Disjoint Sets

- Union Find is a data structure keeps track of a set of elements that are partitioned into a number of disjoint subsets.
- It has two operations union(p, q) and find(p).
- The find/search finds the subset element p belongs to.
and union/merge merges the subsets containing p and q.
- It memory usage is O(N), and each find and union operations are near O(1) in time.
- The algorithm can be used to find all connected components in a network.
- It is also used in kruskal's algorithm to find the minimal spanning tree for a graph.