#The tours in the TSP can be represented as a vector of cities
#Documentation -> https://tsplib95.readthedocs.io/en/stable/

import tsplib95
import networkx

tsp = tsplib95.load('burma14.tsp')

#print(tsp.render()) #Outputs the contents of the TSP file

#print(list(tsp.get_nodes()))

print(list(tsp.get_edges()))
print(tsp.edge_weight_type)
test_edge = 3, 8
weight = tsp.get_weight(*test_edge)
print(weight)