#!/usr/bin/env python
import csv
import networkx as nx
import scipy as sp
import numpy
import matplotlib.pyplot as plt
import pydotplus

G = nx.Graph()

with open('redditQuery.csv', 'rb') as csvfile:
	queryReader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
	count = 0
	for row in queryReader:
		G.add_edge(row[0], row[1])

nx.draw(G)
plt.savefig("graph")