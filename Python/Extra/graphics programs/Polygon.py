import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_polygon(points):
    poly = patches.Polygon(points, fc='cyan',ec='red',linestyle='dashed')

    plt.gca().add_patch(poly)
    plt.axis('scaled')
    plt.title('Polygon')
    plt.show()


def main():
    points = eval(input('Enter the points: '))
    plot_polygon(points)

main()