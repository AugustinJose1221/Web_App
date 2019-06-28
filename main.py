'''
import csv
import googlemaps
import numpy as np
'''
from flask import Flask, flash, redirect, render_template,request,session,abort
'''
gmaps = googlemaps.Client(key='AIzaSyAMp71qLXdZl5x80f0hjazPeUmtUyWAOIw')        #API Key
data = "example1.csv"                                        #Dataset
h_list={}
x=0
with open(data, 'r+') as file:
    reader = csv.reader(file)
    hospital_list = list(reader)
for a in hospital_list:
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
'''
app = Flask(__name__)

@app.route("/")
def my_form():
    return render_template('test.html')

@app.route("/",methods=['POST'])
def my_form_post():
    '''
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
                h_list[i,7]=distance["distance"]["value"]/1000
                if (distance["distance"]["value"]/1000)<dist:
                    dist=distance["distance"]["value"]/1000
                    pos=i
                #print("Name :",h_list[i,0],"\nAddress :",h_list[i,1],"\nDistance :",h_list[i,4],"\n")
    '''
    nearest_park = "Django's garage" #str(h_list[pos,0])
    greet = "Nearest parking lot is "+nearest_park
    return render_template("test.html",name=greet)#processed_text

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
