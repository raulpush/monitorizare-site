__author__ = 'v-anmure'
import csv
import os



def line(filename):
    path = os.path.dirname(os.path.abspath(__file__))
    f = open(path+"/"+filename)
    csv_f = csv.reader(f)
    list =[]
    for row in csv_f:
        list.append(row)

    myMap = {}
    for a in range(1, len(list)):
        key = str(a)
        myMap[key]={}
    for i in range(0, len(list[0])):
        for j in range(1, len(list)):
            key = str(j)
            myMap[key][list[0][i]]=list[j][i]
    return myMap


