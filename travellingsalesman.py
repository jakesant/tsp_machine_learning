import tsplib95 #https://tsplib95.readthedocs.io/en/stable
import networkx #https://networkx.org/documentation/stable/
import acopy #https://acopy.readthedocs.io/en/latest/
from satsp import solver #https://pypi.org/project/satsp/
import matplotlib.pyplot as pyplot
import time

def sa(graph):
    """Simulated Annealing Algorithm
    """

    solver.Solve(city_list = graph, epochs = 10, stopping_count = 15)
    solver.PrintSolution

def aco(graph):
    """Ant Colony Optimisation Algorithm"""

    solver = acopy.Solver(rho=.03, q=1)
    timer = acopy.plugins.Timer()
    solver.add_plugin(timer) #Will give us
    colony = acopy.Colony(alpha=1, beta=3)
    tour = solver.solve(graph, colony, limit=10)
    print("Total time taken", timer.duration)
    print("Time per iteration", timer.time_per_iter)
    print("Cost of tour", tour.cost)
    print("Path", tour.path)
    return tour

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
    tsp = tsplib95.load('burma14.tsp')
    problem_graph = tsp.get_graph()
    cities = load_file(problem_graph)
    #networkx.draw(problem_graph)
    print("Ant Colony Optimisation test")
    acotour = aco(problem_graph)
    print("Simulated Annealing test")
    sa(cities)
    draw(problem_graph, tsp, acotour)
    print("Ok")