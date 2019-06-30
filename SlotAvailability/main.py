from flask import Flask, render_template, request
import csv
import datetime
app = Flask(__name__)

@app.route("/")
def my_form():
    return render_template('test1.html')


@app.route("/",methods=['POST'])
def my_form_post():
    sdate=request.form['sdate']
    stime=request.form['stime']
    edate=request.form['edate']
    etime=request.form['etime']
    st1=int(stime[0:2])
    et1=int(etime[0:2])
    data = csv.reader(open('Owner.csv'),delimiter=',')
    data1 = csv.reader(open('Owner.csv'),delimiter=',')
    flag=0
    flag1=0
    out1 = "No slot is available"
    out = "No slot is available"
    arr =[]
    if sdate==edate:
        for i in data:
            if sdate==i[2]:
                flag=0
                for j in range((int(st1)+3),(int(et1)+3)):
                    if i[j]=="1":
                        flag=1
                        break
                if flag==0:
                    arr.append(str(i[1]))
                    flag1 = 1
                
    else:
        x1 = datetime.date(int(sdate[0:4]),int(sdate[5:7]),int(sdate[8:10]))
        x2 = datetime.date(int(edate[0:4]),int(edate[5:7]),int(edate[8:10]))
        #print(datetime.timedelta(1))
        #print(x1+datetime.timedelta(1))
        d = str(x2-x1)
        d1 = d.split()
        delta = d1[0]
        for i in data:
            if sdate==i[2]:
                id1 = i[0]
                slot = i[1]
                flag=0
                for j in range((int(st1)+3),26):
                    if i[j]=="1":
                        flag=1
                        break
                if flag==1:
                    continue
                for k in data1:
                    if k[0]==id1:
                        if k[1]==slot:
                            newdate=x1
                            for l in range(1,int(delta)):
                                newdate=newdate+datetime.timedelta(1)
                                #print(newdate.strftime("%d-%m-%y"))
                                if k[2]==str(newdate):
                                    for m in range(3,26):
                                        if k[m]=="1":
                                            flag=1
                                            break
                                    if flag==1:
                                        break
                                      
                            if flag==1:
                                continue
                            
                        
            
                            if k[2]==str(newdate+datetime.timedelta(1)):
                                for n in range(3,(int(et1)+3)):
                                    if k[n]=="1":
                                            flag=1
                                            break
                            
                            if flag==1:
                                continue
                            
                if flag==1:
                    continue

                if flag==0:
                    arr.append(str(i[1]))
                    flag1 = 1
                    break
            else:
                continue
    if flag1==1:
         s = "Slot "+arr[0]+" is available"
         return render_template("test1.html",time1=s)
    elif flag1==0:
        return render_template("test1.html",time1=out)
        
        

if __name__=="__main__":
    app.run()
