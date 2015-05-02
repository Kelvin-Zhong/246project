import networkx as nx
G = nx.Graph()
f = open('higgs-social_network.edgelist','r')

for line in f:
	nodes = line.split()
	nodeFrom = int(nodes[0])
	nodeTo = int(nodes[1])
	G.add_edge(nodeFrom, nodeTo)
	print "Add edge from ", nodeFrom, " to ", nodeTo
