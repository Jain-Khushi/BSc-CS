import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_ellipse(width, height):
    ellipse = patches.Ellipse((1,1),width, height, fc='green'\
    ,ec='red',linestyle='dashed',angle=15)

    plt.gca().add_patch(ellipse)
    plt.axis('scaled')
    plt.title('Ellipse')
    plt.show()


def main():
    width = float(input('Enter the width: '))
    height = float(input('Enter the height: '))
    plot_ellipse(width,height)

main()