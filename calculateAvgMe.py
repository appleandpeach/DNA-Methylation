import os.path
import numpy as np
import matplotlib.pyplot as plt
__author__ = 'Mina'

# input can be a directory or a file, all the results will be written in a new file located in the output path.
# output path is a file.
# the input file format:
# two columns, one is CpG site position num and the other is DNA methylation level of the site, delimited by tab.

avgList = []
varianceList = []

def splitsinglefile(inputpath,outputpath):
    try:
        if os.path.isdir(inputpath):
            print("is directory")
            if inputpath[-1] == '/':
                inputpath = inputpath[:-1]
            for filename in os.listdir(inputpath):
                print(inputpath + "/" + filename)
                avgme(inputpath + "/" + filename)
                varianceme(inputpath + "/" + filename)
                outavg(inputpath + "/" + filename, outputpath)
        else:
            print("is file")
            print(inputpath)
            avgme(inputpath)
            varianceme(inputpath)
            outavg(inputpath, outputpath)
    except FileExistsError:
        print("Your file or directory does not exist!")

def avgme(inputsinglefile):
    try:
        input = open(inputsinglefile)
        # output = open(outputpath, 'a')
        sum = 0
        cnt = 0
        while True:
            line = input.readline()
            if not line or line == '':
                break
            cnt += 1
            sum += float(line.split('\t')[-1].rstrip())
        avgList.append(sum/cnt)
        # output.write(inputsinglefile.split('/')[-1] + '\t' + str(sum/cnt) + '\n')
    except IOError:
        print("Can't find the file or your file is broken.")
    except Exception as ex:
        print(ex)
    finally:
        input.close()
        # output.close()

def varianceme(inputpath):
    try:
        input = open(inputpath)
        cnt = 0
        sum = 0
        while True:
            line = input.readline()
            if not line or line == '':
                break
            cnt += 1
            sum = (float(line.split('\t')[-1].rstrip()) - avgList[-1]) ** 2
        varianceList.append(sum/(cnt-1))
    except IOError as io:
        print(io)
    except ValueError as value:
        print(value)
    finally:
        input.close()

def outavg(inputpath, outputpath):
    try:
        output = open(outputpath,'a')
        output.write(inputpath.split('/')[-2] + '\t' + inputpath.split('/')[-1] + '\t' + str(avgList[-1]) + '\t' + str(varianceList[-1]) + '\n')
    except IOError as io:
        print(io)
    except ValueError as value:
        print(value)
    finally:
        output.close()

cell_type = ['2cell', '4cell', 'E65', 'E75', 'ICM', 'oocyte', 'sperm']
dic_2cell = {}
dic_4cell = {}
dic_E65 = {}
dic_E75 = {}
dic_ICM = {}
dic_oocyte = {}
dic_sperm = {}

def insertdata(path):
    drawfile = open(path)
    strline = drawfile.readlines()
    for line in strline:
        linelist = line.split('\t')
        if linelist[0] == '2cell':
            dic_2cell[linelist[1][3:]] = [linelist[2],linelist[3].rstrip()]
        if linelist[0] == '4cell':
            dic_4cell[linelist[1][3:]] = [linelist[2],linelist[3].rstrip()]
        if linelist[0] == 'E65':
            dic_E65[linelist[1][3:]] = [linelist[2],linelist[3].rstrip()]
        if linelist[0] == 'E75':
            dic_E75[linelist[1][3:]] = [linelist[2],linelist[3].rstrip()]
        if linelist[0] == 'ICM':
            dic_ICM[linelist[1][3:]] = [linelist[2],linelist[3].rstrip()]
        if linelist[0] == 'oocyte':
            dic_oocyte[linelist[1][3:]] = [linelist[2],linelist[3].rstrip()]
        if linelist[0] == 'sperm':
            dic_sperm[linelist[1][3:]] = [linelist[2],linelist[3].rstrip()]
    # print(dic_2cell)

def chr_period():
    list_all = []
    list_2cell = []
    list_4cell = []
    list_E65 = []
    list_E75 = []
    list_ICM = []
    list_oocyte = []
    list_sperm = []

    for item in range(19):
        list_2cell.append(dic_2cell[str(item+1)][0])
        list_4cell.append(dic_4cell[str(item+1)][0])
        list_E65.append(dic_E65[str(item+1)][0])
        list_E75.append(dic_E75[str(item+1)][0])
        list_ICM.append(dic_ICM[str(item+1)][0])
        list_oocyte.append(dic_oocyte[str(item+1)][0])
        list_sperm.append(dic_sperm[str(item+1)][0])

    list_2cell.append(dic_2cell['X'][0])
    list_2cell.append(dic_2cell['Y'][0])
    list_4cell.append(dic_4cell['X'][0])
    list_4cell.append(dic_4cell['Y'][0])
    list_E65.append(dic_E65['X'][0])
    list_E65.append(dic_E65['Y'][0])
    list_E75.append(dic_E75['X'][0])
    list_E75.append(dic_E75['Y'][0])
    list_ICM.append(dic_ICM['X'][0])
    list_ICM.append(dic_ICM['Y'][0])
    list_oocyte.append(dic_oocyte['X'][0])
    list_sperm.append(dic_sperm['Y'][0])

    list_all.append(list_2cell)
    list_all.append(list_4cell)
    list_all.append(list_E65)
    list_all.append(list_E75)
    list_all.append(list_ICM)
    list_all.append(list_oocyte)
    list_all.append(list_sperm)
    return list_all

def chr_period_variance():
    list_all = []
    list_2cell = []
    list_4cell = []
    list_E65 = []
    list_E75 = []
    list_ICM = []
    list_oocyte = []
    list_sperm = []

    for item in range(19):
        list_2cell.append(dic_2cell[str(item+1)][1])
        list_4cell.append(dic_4cell[str(item+1)][1])
        list_E65.append(dic_E65[str(item+1)][1])
        list_E75.append(dic_E75[str(item+1)][1])
        list_ICM.append(dic_ICM[str(item+1)][1])
        list_oocyte.append(dic_oocyte[str(item+1)][1])
        list_sperm.append(dic_sperm[str(item+1)][1])

    list_2cell.append(dic_2cell['X'][1])
    # list_2cell.append(dic_2cell['Y'][1])
    list_4cell.append(dic_4cell['X'][1])
    # list_4cell.append(dic_4cell['Y'][1])
    list_E65.append(dic_E65['X'][1])
    # list_E65.append(dic_E65['Y'][1])
    list_E75.append(dic_E75['X'][1])
    # list_E75.append(dic_E75['Y'][1])
    list_ICM.append(dic_ICM['X'][1])
    # list_ICM.append(dic_ICM['Y'][1])
    # list_oocyte.append(dic_oocyte['X'][1])
    # list_sperm.append(dic_sperm['Y'][1])

    list_all.append(list_2cell)
    list_all.append(list_4cell)
    list_all.append(list_E65)
    list_all.append(list_E75)
    list_all.append(list_ICM)
    list_all.append(list_oocyte)
    list_all.append(list_sperm)
    return list_all

def drawpic(path):
    try:
        insertdata(path)
        plt.figure(0)
        plt.suptitle('Average of Methylation level', fontsize=26, fontweight='bold')
        plt.xlabel("chromosome_mouse", fontsize=24)
        plt.ylabel("Avg Methy level", fontsize=24)
        plt.xlim((0, 25))
        dic_1 = chr_period()


        listx = []
        for i in range(21):
            listx.append(i+1)

        # for i in dic_1:
        #     for j in range(len(i)):
        #         i[j] = float(i[j])
        # print(dic_1)

        plt.scatter(listx, dic_1[0], color='b')
        plt.plot(listx, dic_1[0], color='b')
        plt.annotate("2cell", xy=(22,0.48),color='b')
        plt.scatter(listx, dic_1[1], color='r')
        plt.plot(listx, dic_1[1], color='r')
        plt.annotate("4cell", xy=(22,0.4),color='r')
        plt.scatter(listx, dic_1[2], color='y')
        plt.plot(listx, dic_1[2], color='y')
        plt.annotate("E65", xy=(22,0.62),color='y')
        plt.scatter(listx, dic_1[3], color='k')
        plt.plot(listx, dic_1[3], color='k')
        plt.annotate("E75", xy=(22,0.75),color='k')
        plt.scatter(listx, dic_1[4], color='c')
        plt.plot(listx, dic_1[4], color='c')
        plt.annotate("ICM", xy=(22,0.25),color='c')
        plt.scatter(listx[:-1], dic_1[5], color='m')
        plt.plot(listx[:-1], dic_1[5], color='m')
        plt.annotate("oocyte", xy=(22,0.55),color='m')
        listx[-2] = 21
        plt.scatter(listx[:-1], dic_1[6], color='g')
        plt.plot(listx[:-1], dic_1[6], color='g')
        plt.annotate("sperm", xy=(22,0.83),color='g')
        plt.xticks(np.arange(min(listx), max(listx)+1))
        plt.show()

    except IOError as io:
        print(io)
    # except ValueError as value:
    #     print(value)

def draw_variance():
    plt.figure(1)
    x = []
    y = [0.04, 0.03, 0.04, 0.11, 0.08, 0.02, 0.01, 0.03, 0.07, 0.05, 0.02, 0.02, 0.02, 0.07, 0.06, 0.13, 0.02, 0.02, 0.06, 0.08, 4.41]
    for i in range(21):
        x.append(i+1)
    plt.suptitle('Average variance of Methylation level', fontsize=24, fontweight='bold')
    plt.xlabel("chromosome_mouse", fontsize=20)
    plt.ylabel("Avg variance  1E-6", fontsize=20)
    plt.xlim((0, 25))
    plt.xticks(np.arange(min(x), max(x)+1))
    plt.plot(x, y, color='k', linewidth=3)
    plt.show()


if __name__ == "__main__":

    # for item in cell_type:
    #     inputpath = "/Users/Mina/PycharmProjects/Me/Experiment_Data/Processed/" + item
    #     outputpath = "/Users/Mina/PycharmProjects/Me/Experiment_Data/avgResult/avgVarianc"
    #     splitsinglefile(inputpath, outputpath)
    #
    drawpic("/Users/Mina/PycharmProjects/Me/Experiment_Data/avgResult/avgVarianc")
    # draw_variance()

