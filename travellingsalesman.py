#The tours in the TSP can be represented as a vector of cities
#Documentation -> https://tsplib95.readthedocs.io/en/stable/

import tsplib95
import networkx
import acopy
from satsp import solver

def sa(graph):
    """Simulated Annealing Algorithm
    """

    solver.Solve(city_list = graph, epochs = 400, stopping_count = 500)
    solver.PrintSolution

def aco(graph):
    """Ant Colony Optimisation Algorithm"""

    solver = acopy.Solver(rho=.03, q=1)
    colony = acopy.Colony(alpha=1, beta=3)
    tour = solver.solve(graph, colony, limit=500)
    print(tour)

if __name__=='__main__':
    tsp = tsplib95.load('burma14.tsp')
    problem_graph = tsp.get_graph()
    print("Ant Colony Optimisation test")
    aco(problem_graph)
    print("Simulated Annealing test")
    sa(problem_graph)