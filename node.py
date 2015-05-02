import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
f = open('higgs-retweet_network.edgelist','r')

most = 10000
for line in f:
	nodes = line.split()
	nodeFrom = int(nodes[0])
	nodeTo = int(nodes[1])
	G.add_edge(nodeFrom, nodeTo)
	#print "Add edge from ", nodeFrom, " to ", nodeTo
	# if most == 0:
	# 	break
	most -= 1

print G.order()

l = []
for n in G:
	numfollower = len(G.in_edges(n))
	#print G.in_edges(n), numfollower
	l.append([n, numfollower])

l = sorted(l, key=lambda s: s[1], reverse=True)
print l[:100]


# nx.draw(G)
# plt.show()