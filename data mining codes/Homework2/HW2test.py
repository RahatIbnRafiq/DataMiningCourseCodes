
from csv import DictReader
import numpy as np
from sklearn import preprocessing
from scipy.stats.stats import pearsonr 
import matplotlib
import matplotlib.pyplot as plt 
from datetime import datetime
from numpy.random import normal

def correlationCoeff(): 
    a = [1,4,6]
    b = [1,4]   
    print pearsonr(a,b)


def normalizationWord():
    data = []
    total_data = DictReader(open("HistoricalQuotes.csv", 'Ur'))
    for ii in total_data:
        if len(ii["volume"]) == 0:
            continue
        data.append(float(ii["volume"]))
    X_train = np.array(data[0:10])
    min_max_scaler = preprocessing.MinMaxScaler()
    X_train_minmax = min_max_scaler.fit_transform(X_train)
    
    for x,y in zip(X_train,X_train_minmax):
        print str(x)+"-------------"+str(y)
    
    print "_____________________________________________"
    
    X_train = np.array(data[0:10])
    std_scale = preprocessing.StandardScaler().fit(X_train)
    X_train_zscore = std_scale.transform(X_train)
    
    for x,y in zip(X_train,X_train_zscore):
        print str(x)+"-------------"+str(y)

def singlePlot():
    highData = []
    lowData = []
    dates = []
    total_data = DictReader(open("3years.csv", 'Ur'))
    for ii in total_data:
        if len(ii["high"]) == 0:
            continue
        highData.append(float(ii["high"]))
        lowData.append(float(ii["low"]))
        date = str(ii["date"])
        dates.append(datetime.strptime(date, '%m/%d/%Y'))
    x = np.array(dates)
    plt.plot(x,highData,label="high",color="black")
    plt.plot(x,lowData,label="low",color="blue")
    legend = plt.legend(loc='upper left', shadow=True,prop={'size':22})
    legend.get_frame().set_facecolor('#00FFCC')
    plt.show()
    

def boxPlot():
    openData = []
    closeData =  []
    total_data = DictReader(open("3years.csv", 'Ur'))
    for ii in total_data:
        if len(ii["open"]) == 0:
            continue
        openData.append(float(ii["open"]))
        closeData.append(float(ii["close"]))
    openData.sort()
    closeData.sort()
    openD = np.array(openData)
    closeD = np.array(closeData)
    
    data_to_plot = [openD, closeD]
    fig = plt.figure(2, figsize=(9, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot)
    color = ["black","blue"]
    index = 0
    for box in bp['boxes']:
        box.set( color=color[index], linewidth=2)
        index+= 1
    
    plt.xlabel("black for open, blue for close")
    plt.show()

    
    


#normalizationWord()

#correlationCoeff()

#singlePlot()

#boxPlot()





def histogram():
    volumeData = []
    total_data = DictReader(open("3years.csv", 'Ur'))
    for ii in total_data:
        if len(str(ii["close"])) == 0:
            continue
        volumeData.append(float(ii["close"]))
    print len(volumeData)
    print volumeData
    #gaussian_numbers = normal(size=1000)
    #print gaussian_numbers
    #volumeData = [1,1,1,1,2,2,3,4,5,5,5,6,7,8,9,9,9,9,10]
    plt.hist(volumeData,bins=10)
    #plt.title("Gaussian Histogram")
    plt.xlabel("close")
    plt.ylabel("# of quotes")
    plt.show()











boxPlot()




print "done"