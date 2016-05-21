import numpy as np
import matplotlib.pyplot as plt


promoter = [["oocyte", "sperm", "2-cell", "4-cell", "E65", "E75", "ICM"], [0.21, 0.28, 0.12, 0.12, 0.09, 0.24, 0.30]]
exon = [["oocyte", "sperm", "2-cell", "4-cell", "E65", "E75", "ICM"], [0.5, 0.6, 0.4, 0.36, 0.18, 0.51, 0.58]]
# transcript = [["oocyte", "sperm", "2-cell", "4-cell", "E65", "E75", "ICM"], []]
utr3 = [["oocyte", "sperm", "2-cell", "4-cell", "E65", "E75", "ICM"], [0.7, 0.84, 0.53, 0.49, 0.26, 0.68, 0.76]]
utr5 = [["oocyte", "sperm", "2-cell", "4-cell", "E65", "E75", "ICM"], [0.08, 0.09, 0.08, 0.06, 0.04, 0.07, 0.1]]
xstick = ["oocyte", "sperm", "2-cell", "4-cell", "E65", "E75", "ICM"]


def draw():
    plt.figure(0)
    plt.suptitle(' Methylation level of different elements', fontsize=24, fontweight='bold')
    plt.xlabel("Period", fontsize=24)
    plt.ylabel("Average Methylation level", fontsize=24)
    plt.ylim((0, 1))
    plt.margins(0.05)

    plt.plot(range(len(promoter[0])), promoter[1], color='b', linewidth=4)
    plt.plot(range(len(exon[0])), exon[1], color='r', linewidth=4)
    plt.plot(range(len(utr3[0])), utr3[1], color='m', linewidth=4)
    plt.plot(range(len(utr5[0])), utr5[1], color='g', linewidth=4)
    plt.xticks(range(len(xstick)+2), xstick, size='large')

    plt.annotate("promoter", xy=(6.5, 0.3), color='b')
    plt.annotate("exon", xy=(6.5, 0.6),color='r')
    plt.annotate("3utr", xy=(6.5, 0.8),color='m')
    plt.annotate("5utr", xy=(6.5,0.1),color='g')


    plt.show()

if __name__ == '__main__':
    draw()



