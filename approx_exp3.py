import matplotlib.pyplot as plt
import graph

#nodes = 5 6 7 8 9 , edges = 10
def experiment(approxI,m):
    i_range = list(range(5,10))
    results={}
    for i in i_range:
        results[i] = 0
        for _ in range(m):
            random_graph = graph.create_random_graph(i, 10)
            if approxI==0:
                results[i] += len(graph.MVC(random_graph))
            elif approxI==1:
                results[i] += len(graph.approx1(random_graph))
            elif approxI==2:
                results[i] += len(graph.approx2(random_graph))
            elif approxI==3:
                results[i] += len(graph.approx3(random_graph))
        
    return i_range, [results[i] for i in i_range]

def plot_results():
    approxI_values = [0, 1, 2, 3]
    m = 100 #repeat each experiment 100 times
    
    plt.figure(figsize=(10, 6))
    for approxI in approxI_values:
        x, y = experiment(approxI, m)
        if approxI==0:
            plt.plot(x, y, label=f'MVC')
        else:
            plt.plot(x, y, label=f'approx={approxI}')

    plt.title('Approximation of MVC')
    plt.xlabel('Number of nodes (i)')
    plt.ylabel('Values of MVC')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Run the experiment and generate the plot
plot_results()
