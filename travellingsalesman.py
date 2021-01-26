import tsplib95 #https://tsplib95.readthedocs.io/en/stable
import networkx #https://networkx.org/documentation/stable/
import acopy #https://acopy.readthedocs.io/en/latest/
from satsp import solver #https://pypi.org/project/satsp/
import matplotlib.pyplot as pyplot
import time

"""Instances and their best known solutions
http://elib.zib.de/pub/mp-testdata/tsp/tsplib/stsp-sol.html

berlin52 : 7542
st70 : 675
pr107 : 44303
ch150 : 6528
"""


def sa(graph, cities):
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
        print("Best TSP distance: ",solver.GetBestDist())
        print("Best TSP tour: ", solver.GetBestTour())
        print("Total time taken:", time_taken, "seconds")
        print("")

def aco(graph, tsp):
    """Ant Colony Optimisation Algorithm
    
    Tests out multiple configurations for ACO parameters"""
    
    configs = [
       #rho, q, alpha, beta, limit
        [.03, 1, 1, 6, 500],
        [.03, 5, 1, 6, 500],
        [.03, 10, 1, 6, 500],
        [.03, 25, 1, 6, 500],
        [.06, 1, 1, 6, 500],
        [.06, 5, 1, 6, 500],
        [.06, 10, 1, 6, 500],
        [.06, 25, 1, 6, 500]
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
        #draw(graph, tsp, tour)
        print("")

def load_file(G):
    """Stores the problem in a list of cities"""

    cities = []

    nodes = G.get_nodes()
    for index, node in enumerate(nodes):
        index+=1
        G.node_coords[node]
        cities.append([index, G.node_coords[node][0], G.node_coords[node][1]])
    
    return cities

def draw(G, tsp, tour):
    """Draws graph of solution"""

    colors = ['black', 'blue']
    pyplot.figure(dpi=300)
    _, ax = pyplot.subplots()
    pos = tsp.display_data or tsp.node_coords
    networkx.draw_networkx_nodes(G, pos=pos, ax=ax, node_color=(0.4157, 0.3529, 0.3490))
    networkx.draw_networkx_labels(G, pos=pos, labels={i: str(i) for i in range(1, len(G.nodes) + 1)}, font_size=8,
                            font_color='white')
    solution = tour.path
    path = solution
    networkx.draw_networkx_edges(G, pos=pos, edgelist=path, edge_color=colors[0])
    # If this doesn't exsit, x_axis and y_axis's numbers are not there.
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    pyplot.show(block=False)
    pyplot.pause(5)
    pyplot.close()

if __name__=='__main__':
    #files = ['berlin52.tsp', 'st70.tsp', 'pr107.tsp', 'ch150,tsp']
    files = ['st70.tsp']

    """for file in files:
        tsp = tsplib95.load(file)
        problem_graph = tsp.get_graph()
        cities = load_file(tsp)
        print("----Ant Colony Optimisation----")
        print("Instance name:", file)
        aco(problem_graph, tsp)
        print("----Simulated Annealing----")
        print("Instance name:", file)
        cities = load_file(tsp)
        sa(problem_graph, cities)"""

    for file in files:
        tsp = tsplib95.load(file)
        problem_graph = tsp.get_graph()
        print("Simulated Annealing")
        print("Instance name:", file)
        cities = load_file(tsp)
        sa(problem_graph, cities)

    """for file in files:
        tsp = tsplib95.load(file)
        problem_graph = tsp.get_graph()
        print("----Ant Colony Optimisation----")
        print("Instance name:", file)
        aco(problem_graph, tsp)"""

    #tsp = tsplib95.load('berlin52.tsp')
    #problem_graph = tsp.get_graph()
    #cities = load_file(problem_graph)
    #networkx.draw(problem_graph)
    #print("Ant Colony Optimisation test")
    #aco(problem_graph)
    #print("Simulated Annealing test")
    #sa(cities)
    #draw(problem_graph, tsp)
    print("Ok")