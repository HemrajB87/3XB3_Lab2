import graph
import matplotlib.pyplot as plt

def random_graph_connected_probability_experiment(i, m):
    j_range = list(range(0, 1200, 10))
    results = {}

    for j in j_range:
        count_connected = 0
        for _ in range(m):
            random_graph = graph.create_random_graph(i, j)
            if graph.is_connected(random_graph):
                count_connected += 1
        results[j] = count_connected / m

    return j_range, [results[j] for j in j_range]

def plot_results():
    node_values = [50, 100, 150, 200]
    m = 100

    plt.figure(figsize=(10, 6))

    for i in node_values:
        x, y = random_graph_connected_probability_experiment(i, m)
        plt.plot(x, y, label=f'i={i} nodes')

    plt.title('Probability of Complete Connection in Random Graphs')
    plt.xlabel('Number of Edges (j)')
    plt.ylabel('Probability of Complete Connection')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Run the experiment and generate the plot
plot_results()