import pickle
from os import listdir
from os.path import isfile, join
from pathlib import Path
import pandas as pd

#change this for windows path to f'{Path.home()}\\airo\\data'
myPath = f'{Path.home()}/airo/data'
onlyfiles = [f for f in listdir(myPath) if isfile(join(myPath,f))]
first=True
for f in onlyfiles:
    #should we concat them one by one
    #will this consume more memory
    if  first:
        with open (join(myPath,f),'rb') as file:
            data1 = pickle.load(file)
            first = False
    else:
        with open (join(myPath,f),'rb') as file:
            data2 = pickle.load(file)
            data1 = pd.concat([data1,data2])
            print(data1.info())

def alternate_load():
    #alternative loading for less memory usage
    with open (join(myPath,onlyfiles[0]),'rb') as file:
                data1 = pickle.load(file)
                first = False
    with open (join(myPath,onlyfiles[1]),'rb') as file:
                data2 = pickle.load(file)
                first = False
    with open (join(myPath,onlyfiles[2]),'rb') as file:
                data3 = pickle.load(file)
                first = False
    with open (join(myPath,onlyfiles[3]),'rb') as file:
                data4 = pickle.load(file)
                first = False
    with open (join(myPath,onlyfiles[4]),'rb') as file:
                data5 = pickle.load(file)
                first = False
    with open (join(myPath,onlyfiles[5]),'rb') as file:
                data6 = pickle.load(file)
                first = False
    with open (join(myPath,onlyfiles[6]),'rb') as file:
                data7 = pickle.load(file)
                first = False
    with open (join(myPath,onlyfiles[7]),'rb') as file:
                data8 = pickle.load(file)
                first = False
    with open (join(myPath,onlyfiles[8]),'rb') as file:
                data9 = pickle.load(file)
                first = False
    with open (join(myPath,onlyfiles[9]),'rb') as file:
                data10 = pickle.load(file)
                first = False
    data1 = pd.concat([data1,data2,data3,data4,data5,data6,data7,data8,data9,data10])
    print(data1.info())