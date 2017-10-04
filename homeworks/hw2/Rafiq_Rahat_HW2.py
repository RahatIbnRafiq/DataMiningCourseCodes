#Assignment based on http://www.nasdaq.com/quotes/
#Feel free to use any libraries. 
#Make sure that the output format is perfect as mentioned in the problem.
#Also check the second row of the download dataset.
#If it follows a different format, avoid it or remove it.

import argparse
from csv import DictReader
import numpy as np
from sklearn import preprocessing
from scipy.stats.stats import pearsonr

def normalization ( fileName , normalizationType , attribute):
    '''
    Input Parameters:
        fileName: The comma seperated file that must be considered for the normalization
        attribute: The attribute for which you are performing the normalization
        normalizationType: The type of normalization you are performing
    Output:
        For each line in the input file, print the original "attribute" value and "normalized" value seperated by <TAB> 
    '''
    #TODO: Write code given the Input / Output Paramters.
    data = []
    total_data = DictReader(open(fileName, 'Ur'))
    for ii in total_data:
        if len(ii[str(attribute)]) == 0:
            continue
        data.append(float(ii[str(attribute)]))
        X_train = np.array(data)
        if normalizationType == "min_max":
            min_max_scaler = preprocessing.MinMaxScaler()
            X_result = min_max_scaler.fit_transform(X_train)
        else:
            std_scale = preprocessing.StandardScaler().fit(X_train)
            X_result = std_scale.transform(X_train)
        count = 0
        for x,y in zip(X_train,X_result):
            print str(x)+"\t"+str(y)
            count+= 1
        print count

def correlation ( attribute1 , fileName1 , attribute2, fileName2 ):
    '''
    Input Parameters:
        attribute1: The attribute you want to consider from file1
        attribute2: The attribute you want to consider from file2
        fileName1: The comma seperated file1
        fileName2: The comma seperated file2
        
    Output:
        Print the correlation coefficient 
    '''
    #TODO: Write code given the Input / Output Paramters.
    data1 = []
    total_data1 = DictReader(open(fileName1, 'Ur'))
    for ii in total_data1:
        if len(ii[str(attribute1)]) == 0:
            continue
        data1.append(float(ii[str(attribute1)]))
        
    data2 = []
    total_data2 = DictReader(open(fileName2, 'Ur'))
    for ii in total_data2:
        if len(ii[str(attribute2)]) == 0:
            continue
        data2.append(float(ii[str(attribute2)]))
    
    if len(data1) != len(data2):
        print " the variables are not of the same size. Do not know what to do!!!"
    
    X1 = np.array(data1)
    X2 = np.array(data2)
    print pearsonr(X1,X2)[0]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Data Mining HW2')
    parser.add_argument('-f1', type=str,
                            help="Location of filename1. Use only f1 when working with only one file.",
                            required=True)
    parser.add_argument("-f2", type=str, 
                            help="Location of filename2. To be used only when there are two files to be compared.",
                            required=False)
    parser.add_argument("-n", type=str, 
                            help="Type of Normalization. Select either min_max or z_score",
                            choices=['min_max','z_score'],
                            required=False)
    parser.add_argument("-a1", type=str, 
                            help="Type of Attribute for filename1. Select either open or high or low or close or volume",
                            choices=['open','high','low','close','volume'],
                            required=False)
    parser.add_argument("-a2", type=str, 
                            help="Type of Attribute for filename2. Select either open or high or low or close or volume",
                            choices=['open','high','low','close','volume'],
                            required=False)



    args = parser.parse_args()

    if ( args.n and args.a1 ):
        normalization( args.f1 , args.n , args.a1 )
    elif ( args.f2 and args.a1 and args.a2):
        correlation ( args.a1 , args.f1 , args.a2 , args.f2 )
    else:
        print "Kindly provide input of the following form:\nDMPythonHW2.py -f1 <filename1> -a1 <attribute> -n <normalizationType> \nDMPythonHW2.py -f1 <filename1> -a1 <attribute> -f2 <filename2> -a2 <attribute>"
