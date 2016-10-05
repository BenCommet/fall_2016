#!/usr/bin/env python
import networkx as nx
import scipy as sp
import numpy
import matplotlib.pyplot as plt
import pydotplus
# G = nx.Graph()
# G.add_edge(1, 2)
# G.add_edge(1, 4)
# G.add_edge(1, 6)
# G.add_edge(2, 4)
# G.add_edge(2, 0)
# G.add_edge(2, 5)
# G.add_edge(2, 3)
# G.add_edge(4, 6)
# G.add_edge(4, 7)
# G.add_edge(4, 0)
# G.add_edge(4, 5)
# G.add_edge(5, 0)
# G.add_edge(7, 0)

# print "Question 1"

# for i in G.edges():
# 	print i

# unformatted = nx.adjacency_matrix(G)
# adjusted = unformatted.todense()
# print adjusted

# for line in nx.generate_adjlist(G):
# 	print(line)

print "Question 2"
matrix = numpy.matrix([
	[0, 1, 0, 0, 0, 0, 0],
	[1, 0, 1, 0, 1, 0, 1],
	[0, 1, 0, 1, 1, 0, 1],
	[0, 0, 1, 0, 0, 0, 0],
	[0, 1, 1, 0, 0, 1, 0],
	[0, 0, 0, 0, 1, 0, 1],
	[0, 1, 1, 0, 0, 1, 0]
	])
G = nx.from_numpy_matrix(matrix)

nx.draw(G)
plt.savefig("graph")

unformatted = nx.adjacency_matrix(G)
adjusted = unformatted.todense()
print adjusted

for line in nx.generate_adjlist(G):
	print(line)