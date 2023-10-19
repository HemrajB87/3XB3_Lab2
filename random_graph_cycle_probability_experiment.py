import graph
import matplotlib.pyplot as plt

def random_graph_cycle_probability_experiment(i, m):
    max_edges = (i * (i - 1)) // 2
    j_range = list(range(0, 150))
    results = {}

    for j in j_range:
        count_cycles = 0
        for _ in range(m):
            random_graph = graph.create_random_graph(i, j)
            if graph.has_cycle(random_graph):
                count_cycles += 1
        results[j] = count_cycles / m

    return j_range, [results[j] for j in j_range]

def plot_results():
    node_values = [50, 100, 150, 200]
    m = 100

    plt.figure(figsize=(10, 6))

    for i in node_values:
        x, y = random_graph_cycle_probability_experiment(i, m)
        plt.plot(x, y, label=f'i={i} nodes')

    plt.title('Probability of Cycles in Random Graphs')
    plt.xlabel('Number of Edges (j)')
    plt.ylabel('Probability of Cycle')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Run the experiment and generate the plot
plot_results()
