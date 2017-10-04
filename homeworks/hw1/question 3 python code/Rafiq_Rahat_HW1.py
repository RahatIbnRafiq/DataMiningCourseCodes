#Assignment based on MAGIC Gamma Telescope Data Set ( http://archive.ics.uci.edu/ml/datasets/MAGIC+Gamma+Telescope )

import argparse
import numpy as np
import matplotlib.pyplot as plt

class dataSet:
    """
    Class to store the MAGIC Gamma Telescope Data Set
    """
    def __init__(self, location):
        with open (location, "r") as myfile:
            self.readData=myfile.readlines();
def calculate( data, ithAttribute):
    """
    Input Parameters:
        data: The data that is read from the file.
        ithAttribute: The ith Attribute for which the various properties must be calculated.

    Default value of 0,infinity,-infinity are assigned to all the variables as required. 
    Objective of the function is to calculate:  N (number of objects), min, max, mean, standard deviation, Q1, median, Q3, IQR
    """

    #noOfObjects , minValue , maxValue , mean , standardDeviation , q1 , median , q3 ,iqr = [0,"inf","-inf",0,0,0,0,0,0]
    #TODO : Write code to assign the values to the respective variables.


    #return noOfObjects , minValue , maxValue, mean, standardDeviation , q1 , median , q3 , iqr
    
    list1 = []
    
    attr4 = [] 
    attr5 = []
    
    for line in data:
        line = line.strip()
        values = line.split(",")
        list1.append(float(values[ithAttribute-1]))
        attr4.append(values[3])
        attr5.append(values[4])
    noOfObjects = len(list1)
    minValue = min(list1)
    maxValue = max(list1)
    standardDeviation = np.std(list1)
    mean = np.mean(list1)
    q1 = np.percentile(list1, 25)
    q3 = np.percentile(list1, 75)
    iqr = np.percentile(list1, 75) - np.percentile(list1, 25)
    median = np.median(list1)
    
    plt.plot(attr4, attr5, 'ro')
    plt.xlabel("attribute 4")
    plt.ylabel("attribute 5")
    plt.show()
    
    return noOfObjects , minValue , maxValue, mean, standardDeviation , q1 , median , q3 , iqr

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Data Mining HW1')
    parser.add_argument('--i', type=int,
                            help="ith attribute of the dataset ( limit 1 to 10 )",
                            default=5,
                            choices=set((1,2,3,4,5,6,7,8,9,10)) ,
                            required=True)
    parser.add_argument("--data", type=str, 
                            help="Location of the downloaded file",
                            default="magic04.data.txt", 
                            required=False)
    args = parser.parse_args()
    data = dataSet(args.data)

    print ','.join(map(str,calculate(data.readData,args.i)))
    #calculate(data.readData,args.i)
