import matplotlib.pyplot as plt
import graph
#boundary case
#15 nodes, 100 edges
def experiment(x):
    MVC = 0
    approx1 = 0
    approx2 = 0
    approx3 = 0
    g = graph.create_random_graph(15, 100)
    for _ in range(x):#repeat each experiment 1000 times
        #record the MVC, approx1, approx2, and approx3
        MVC += len(graph.MVC(g))
        approx1 += len(graph.approx1(g))
        approx2 += len(graph.approx2(g))
        approx3 += len(graph.approx3(g))
    return MVC, approx1, approx2, approx3

#in this function, run experiment for j ranging from 0 to 1200 in increments of 100, and record the results on a plot
def plot_results():
    x_values = list(range(1,10))
    plt.figure(figsize=(10, 6))
    MVCs = []
    approx1s = []
    approx2s = []
    approx3s = []

    for x in x_values:
        MVC, approx1, approx2, approx3 = experiment(x)
        MVCs.append(MVC)
        approx1s.append(approx1)
        approx2s.append(approx2)
        approx3s.append(approx3)
    print(MVCs)
    print(approx1s)
    print(approx2s)
    print(approx3s)

    
    plt.plot(x_values, approx1s, 'b-', label='Approx1')
    plt.plot(x_values, approx2s, 'g-', label='Approx2')
    plt.plot(x_values, approx3s, 'y-', label='Approx3')
    plt.plot(x_values, MVCs, 'r-', label='MVC')
    

    plt.title('Approximation of MVC')
    plt.xlabel('Number of Nodes (i)')
    plt.ylabel('Approximation of MVC')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Run the experiment and generate the plot
plot_results()
    
