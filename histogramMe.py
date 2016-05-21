import os.path
__author__ = 'Mina'

# this code is used to calculate the distance between two CpG.
# you can input a path including the file that you need to statistic distance distribution.
# it coulde be a file or a directory
# output is an directory, we will create the result file whose name follow the input files.
# input format is position and methylation level.

disctanceDic = {}

def histogram(inputpath,outputpath):
    try:
        if os.path.isdir(inputpath):
            print("is directory")
            if inputpath[-1] == '/':
                inputpath = inputpath[:-1]
            for filename in os.listdir(inputpath):
                print(inputpath + "/" + filename)
                histoStatic(inputpath + "/" + filename)
                outhisto(inputpath + "/" + filename, outputpath)
                disctanceDic.clear()
        else:
            print("is file")
            print(inputpath)
            histoStatic(inputpath)
            outhisto(inputpath, outputpath)
            disctanceDic.clear()
    except FileExistsError:
        print("Your file or directory does not exist!")

def histoStatic(inputpath):
    try:
        input = open(inputpath)
        line1 = input.readline()
        flag = True
        if not line1 :
            flag = False
        while flag:
            line2 = input.readline()
            if not line2 or line2 == '':
                break
            pos1 = line1.split('\t')[0]
            pos2 = line2.split('\t')[0]
            distance = int(pos2)-int(pos1)
            if distance not in disctanceDic:
                disctanceDic[distance] = 0
            disctanceDic[distance] += 1
            line1 = line2

        # print(disctanceDic)
    except Exception as ex:
        print(ex)
    finally:
        try:
            input.close()
        except Exception as ex2:
            print(ex2)

def outhisto(inputpath, outputpath):
    try:
        output = open(outputpath + '/' + inputpath.split('/')[-1], 'w')
        print(disctanceDic)
        for item in disctanceDic:
            output.write(str(item) + '\t' + str(disctanceDic[item]) + '\n')
    except IOError as io:
        print(io)
    finally:
        try:
            output.close()
        except IOError as io2:
            print(io2)


if __name__ == '__main__':
    histogram("/Users/Mina/PycharmProjects/Me/Experiment_Data/Processed/2cell/chr2","/Users/Mina/PycharmProjects/Me/Experiment_Data/avgResult/test/histogram")