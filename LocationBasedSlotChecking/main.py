import requests
import datetime
import csv
import googlemaps
import numpy as np
from SlotChecker import SlotCheck
from flask import Flask, flash, redirect, render_template,request,session,abort

gmaps = googlemaps.Client(key='AIzaSyAMp71qLXdZl5x80f0hjazPeUmtUyWAOIw')        #API Key
loc_data = "example1.csv"                                        #Dataset
h_list={}
x=0
with open(loc_data, 'r+') as file:
    reader = csv.reader(file)
    owner_list = list(reader)
for a in owner_list:
    if a[1][0]=='N':
        #print("\n")
        continue
    h_list[x,0]=a[4]
    h_list[x,1]=a[3]
    h_list[x,2]=a[1]
    h_list[x,3]=a[2]
    h_list[x,5]=a[0]
    x+=1
dist=25
pos = 0
dist1=[]
sort1=[]
app = Flask(__name__)
final=[]
x10=[]
@app.route("/")
def my_form():
    return render_template('test1.html')

@app.route("/",methods=['POST'])
def my_form_post():
    try:     
        dist=25
        lat = request.form['text1']
        long = request.form['text2']
        LatP = float(lat)
        LongP = float(long)
        for i in range(0,x):
            t = float(h_list[i,2])-float(LatP)
            p = float(h_list[i,3])-float(LongP)
            if t<0.1 and t>-0.1:
                if p<0.1 and p>-0.1:
                    LatD = h_list[i,2]
                    LongD = h_list[i,3]
                    distance = gmaps.distance_matrix([str(LatP) + " " + str(LongP)], [str(LatD) + " " + str(LongD)], mode='driving')['rows'][0]['elements'][0]
                    h_list[i,4]=distance["distance"]["text"]
                    h_list[i,7]=float(distance["distance"]["value"]/1000)
                    final.append(i)
                    #dist1.append(float(distance["distance"]["value"]/1000))
                    if (distance["distance"]["value"]/1000)<dist:
                        dist=distance["distance"]["value"]/1000
                        pos=i
                    #print("Name :",h_list[i,0],"\nAddress :",h_list[i,1],"\nDistance :",h_list[i,4],"\n")
                    
        nearest_park = str(h_list[pos,0])
        for i in final:
            dist1.append(h_list[i,7])
        dist1.sort()
        t1=0
        tester=[]
        FinalString=[]
        IDString=[]
        OutString=[]
        OutString1=[]
        for j in range(0,len(dist1)):
            for i in final:
                if i in tester:
                    continue
                if dist1[j]==h_list[i,7]:
                    tester.append(i)
                    #print("Name :",h_list[i,0],"\nAddress :",h_list[i,1],"\nDistance :",h_list[i,7],"\n")
                    FinalString.append("Name :"+str(h_list[i,0])+" Address :"+str(h_list[i,1])+" Distance :"+str(h_list[i,7]))
                    IDString.append(str(h_list[i,5]))
                    break
        if len(FinalString)<5:
            for i in range(len(FinalString),6):
                FinalString.append("None")
        sdate=request.form['sdate']
        stime=request.form['stime']
        edate=request.form['edate']
        etime=request.form['etime']
        st=str(stime[0:2])+str(stime[3:5])
        et=str(etime[0:2])+str(stime[3:5])
        x1 = SlotCheck(str(sdate),str(st),str(edate),str(et))
        with open("example1.csv",'r+') as file:
            reader = csv.reader(file)
            vendor_list = list(reader)

        arr1=[]
        arr2=[]
        arr3=[]

        for i in vendor_list:
            for j in range(1,int(i[7])+1):
                arr1.append([str(i[0]),str(j)])
            
                
        id1=0
        fl=0
        for i in arr1:
            if fl==1:
                if str(i[0])==id1:
                    continue
            if i in x1:
                continue
            else:
                arr2.append(i[0])
                id1=i[0]
            fl=1


        q=0
        for i in IDString:
            for j in arr2:
                if i in j:
                    OutString.append(FinalString[q])
                    break
            q+=1
        
            
        if len(OutString)<5:
            for i in range(len(OutString),6):
                OutString.append("None")
        
        
        return render_template("test1.html",name1=OutString[0],name2=OutString[1],name3=OutString[2],name4=OutString[3],name5=OutString[4])#processed_text
    except ValueError:
        return render_template("test1.html",name1="ValueError")
    except googlemaps.exceptions.TransportError:
        return render_template("test1.html",name1="TransportError")

if __name__ == "__main__":
    app.run()

