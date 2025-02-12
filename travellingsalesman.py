import tsplib95 #https://tsplib95.readthedocs.io/en/stable
import acopy #https://acopy.readthedocs.io/en/latest/
from satsp import solver #https://pypi.org/project/satsp/
import time

"""Instances and their best known solutions
http://elib.zib.de/pub/mp-testdata/tsp/tsplib/stsp-sol.html

berlin52 : 7542
st70 : 675
pr107 : 44303
ch150 : 6528
"""

def sa(cities):
    """Simulated Annealing Algorithm"""

    configs = [
        #alpha, epochs
        [.01, 1000],
        [.5, 1000,],
        [.99, 1000],
        [.01, 2000],
        [.5, 2000,],
        [.99, 2000],
        [.01, 3000],
        [.5, 3000,],
        [.99, 3000]
    ]

    for index, config in enumerate(configs):
        start_time = time.time()
        solver.Solve(city_list = cities, alpha = config[0], epochs = config[1], screen_output=False)
        end_time = time.time()
        time_taken = end_time - start_time
        print("Test:", index+1)
        print("Alpha value:", config[0])
        print("Best TSP distance: ",solver.GetBestDist()) #Outputs cost of the best tour
        print("Best TSP tour: ", solver.GetBestTour())
        print("Total time taken:", time_taken, "seconds")
        print("")

def aco(graph):
    """Ant Colony Optimisation Algorithm
    
    Tests out multiple configurations for ACO parameters"""
    
    configs = [
       #rho, q, alpha, beta, limit
        [.03, 1, 1, 3, 500],
        [.03, 5, 1, 3, 500],
        [.03, 10, 1, 3, 500],
        [.03, 25, 1, 3, 500],
        [.06, 1, 1, 3, 500],
        [.06, 5, 1, 3, 500],
        [.06, 10, 1, 3, 500],
        [.06, 25, 1, 3, 500]
    ]

    for index, config in enumerate(configs):
        print("Test:", index+1)
        solver = acopy.Solver(rho=config[0], q=config[1])
        timer = acopy.plugins.Timer()
        solver.add_plugin(timer)
        colony = acopy.Colony(alpha=config[2], beta=config[3])
        tour = solver.solve(graph, colony, limit=config[4])
        print("Total time taken:", timer.duration)
        print("Time per iteration:", timer.time_per_iter)
        print("Cost of tour:", tour.cost)
        print("Tour:", tour.path)
        print("")

def load_file(G):
    """Stores the problem as a list of cities with their coordinates"""

    cities = []

    nodes = G.get_nodes()
    for index, node in enumerate(nodes):
        index+=1
        G.node_coords[node]
        cities.append([index, G.node_coords[node][0], G.node_coords[node][1]])
    
    return cities

if __name__=='__main__':
    files = ['berlin52.tsp', 'st70.tsp', 'pr107.tsp', 'ch150,tsp']

    for file in files:
        tsp = tsplib95.load(file)
        problem_graph = tsp.get_graph() #Converts to problem graph for ACO
        cities = load_file(tsp) #Converts to list for SA
        print("----Ant Colony Optimisation----")
        print("Instance name:", file)
        aco(problem_graph)
        print("")
        print("----Simulated Annealing----")
        print("Instance name:", file)
        sa(cities)