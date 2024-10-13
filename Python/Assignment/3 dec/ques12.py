import matplotlib.pyplot as plt


def plot_histogram(data):
    plt.hist(data)
    plt.xlabel("VALUES")
    plt.ylabel("FREQUENCY")
    plt.title("HISTOGRAM")
    plt.xlim(min(data) - 1, max(data) + 1)
    plt.show()


data = eval(input("Enter a list of 'n' integers to be plotted as histogram : "))
plot_histogram(data)

