import csv
#import pandas as pd
#import numpy as np
import datetime 
def SlotCheck(Sdate,Stime,Edate,Etime):
    arr1=[]
    arr2=[]
    arr3=[]
    Arr1=[]
    Arr2=[]
    Arr3=[]
    tester=0
    x=0
    tester=0
    flag=0
    data="Owner.csv"
    with open(data,'r') as file:
        reader = csv.reader(file)
        vendor_list = list(reader)
    if Sdate==Edate:
        tester=0
        for i in vendor_list:
            if tester==0:
                tester=1
                continue
            if str(i[3])==str(i[5]):
                if Sdate==i[3]:
                    arr1.append(i)
        for j in arr1:
            tester=0
            if int(Stime)<int(j[4]) and int(Etime)<int(j[4]):
                tester=1
            elif int(Stime)>int(j[6]) and int(Etime)>int(j[6]):
                tester=1
            if tester==0:
                arr2.append(j)
        x=0
        for i in arr2:
            ID=i[0]
            Slot=i[1]
            flag=0
            if x==1:
                for j in arr3:
                    if ID in j and Slot in j:
                        flag=1
                        break
                if flag==1:
                    continue
            arr3.append([i[0],i[1]])
            x=1
        return arr3
                
    
    x1 = datetime.date(int(Sdate[0:4]),int(Sdate[5:7]),int(Sdate[8:10]))
    x2 = datetime.date(int(Edate[0:4]),int(Edate[5:7]),int(Edate[8:10]))
    STime1 = datetime.datetime(int(Sdate[0:4]),int(Sdate[5:7]),int(Sdate[8:10]),int(Stime[0:2]),int(Stime[2:4]),0)
    ETime1 = datetime.datetime(int(Edate[0:4]),int(Edate[5:7]),int(Edate[8:10]),int(Etime[0:2]),int(Etime[2:4]),0)
    d = str(x2-x1)
    d1 = d.split()
    if int(d1[0])>0:
        #print("Success")
        tester=0
        for i in vendor_list:
            if tester==0:
                tester=1
                continue
            x3 = datetime.date(int(i[3][0:4]),int(i[3][5:7]),int(i[3][8:10]))
            d4 = str(x3-x1)
            T = d4[0]+str(1)
            if int(T)>=0:
                Arr1.append(i)     
        for j in Arr1:
            STime2 = datetime.datetime(int(j[3][0:4]),int(j[3][5:7]),int(j[3][8:10]),int(j[4][0:2]),int(j[4][3:5]),0)
            ETime2 = datetime.datetime(int(j[5][0:4]),int(j[5][5:7]),int(j[5][8:10]),int(j[6][0:2]),int(j[6][3:5]),0)
            d2=str(STime2-ETime1)
            d3=str(STime1-ETime2)
            t1=d2[0]+str(1)
            t2=d3[0]+str(1)
            tester=0
            if int(t1)>0:
                tester=1
            elif int(t2)>0:
                tester=1
            if tester==0:
                Arr2.append(j)

        x=0
        for i in Arr2:
            ID=i[0]
            Slot=i[1]
            flag=0
            if x==1:
                for j in Arr3:
                    if ID in j and Slot in j:
                        flag=1
                        break
                if flag==1:
                    continue
            Arr3.append([i[0],i[1]])
            x=1


        return Arr3
    
    elif int(d1[0])<0:
        print("Invalid date")
        return 0
''' 
for i in SlotCheck("2019-07-06","0810","2019-07-06","1130"):
    print(i)
'''               
