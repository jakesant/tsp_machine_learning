#The tours in the TSP can be represented as a vector of cities
#Documentation -> https://tsplib95.readthedocs.io/en/stable/

import tsplib95
import networkx
import acopy

def sa():
    """Simulated Annealing Algorithm
    """

def aco():
    """Ant Colony Optimisation Algorithm"""

    solver = acopy.Solver(rho=.03, q=1)
    colony = acopy.Colony(alpha=1, beta=3)
    tour = solver.solve(G, colony, limit=100)
    print(tour)

tsp = tsplib95.load('burma14.tsp')

G = tsp.get_graph()

aco()
print("Ok")

#print(tsp.render()) #Outputs the contents of the TSP file

print(list(tsp.get_nodes())) #Prints all nodes
print(list(tsp.get_edges())) #Prints all edges
alledges = tsp.get_edges()
test_edge = 3, 8
weight = tsp.get_weight(*test_edge)
print(weight)
qw = tsp.get_graph()
qw.nodes

"""
print(tsp.edge_weight_type)
"""
