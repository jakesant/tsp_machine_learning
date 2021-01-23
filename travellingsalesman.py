import tsplib95 #https://tsplib95.readthedocs.io/en/stable
import networkx #https://networkx.org/documentation/stable/
import acopy #https://acopy.readthedocs.io/en/latest/
from satsp import solver #https://pypi.org/project/satsp/
import matplotlib.pyplot as pyplot
import time

"""Instances and their best known solutions
http://elib.zib.de/pub/mp-testdata/tsp/tsplib/stsp-sol.html

berlin52 : 7542
burma14: 3323
pr107 : 44303
"""


def sa(graph):
    """Simulated Annealing Algorithm
    """

    solver.Solve(city_list = graph, epochs = 10, stopping_count = 15)
    solver.PrintSolution

def aco(graph):
    """Ant Colony Optimisation Algorithm
    
    Tests out multiple configurations for ACO parameters"""
    
    configs = [
                [.03, 1, 1, 3, 500],
                [.03, 5, 1, 3, 500],
                [.03, 10, 1, 3, 500],
                [.03, 25, 1, 3, 500],
                [.03, 1, 2, 3, 500],
                [.03, 5, 2, 3, 500],
                [.03, 10, 2, 3, 500],
                [.03, 25, 2, 3, 500],
                [.03, 1, 2, 4, 500],
                [.03, 5, 2, 4, 500],
                [.03, 10, 2, 4, 500],
                [.03, 25, 2, 4, 500]
            ]

    for index, config in enumerate(configs):
        print("Test:", index+1)
        solver = acopy.Solver(rho=config[0], q=config[1])
        timer = acopy.plugins.Timer()
        solver.add_plugin(timer)
        colony = acopy.Colony(alpha=config[2], beta=config[3])
        tour = solver.solve(graph, colony, limit=config[4])
        print("Total time taken", timer.duration)
        print("Time per iteration", timer.time_per_iter)
        print("Cost of tour", tour.cost)
        print("Path", tour.path)
        print("")

def load_file(G):
    """Stores the problem in a list of cities"""

    p = []
    n = list(G.edges)
    i = 1
    for x in n:
        y = list(x)
        y.insert(0, i)
        p.append(y)
        i += 1

    return p

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
    pyplot.show()

if __name__=='__main__':
    files = ['burma14.tsp', 'berlin52.tsp', 'pr107.tsp', 'gil262.tsp']

    for file in files:
        tsp = tsplib95.load(file)
        problem_graph = tsp.get_graph()
        print("Ant Colony Optimisation test")
        aco(problem_graph)

    tsp = tsplib95.load('berlin52.tsp')
    problem_graph = tsp.get_graph()
    cities = load_file(problem_graph)
    #networkx.draw(problem_graph)
    print("Ant Colony Optimisation test")
    aco(problem_graph)
    print("Simulated Annealing test")
    #sa(cities)
    #draw(problem_graph, tsp)
    #print("Ok")