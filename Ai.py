#library
import mysql.connector
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import time

#databse connector
cnx = mysql.connector.connect(user='root', password='ari4127977',
                              host='localhost',
                              database='t_gproject')
cursor = cnx.cursor()
cursor.execute("SELECT * FROM t_gproject.test2;")
data=cursor.fetchall()

#main
ndata=np.array(data)
dfdata=pd.DataFrame(data=ndata,columns=["price","cpu_core","ram_size","Hdd_size","monitor_size","target"])
X=dfdata.iloc[:,0:5].values
Y=dfdata.iloc[:,5].values
model=RandomForestClassifier(n_estimators=100)
model.fit(X,Y)

txt=["your budget(toman):  ",
     "your dream cpu(2,4,..):  ",
     "your ram size(2,4,...):  ",
     "your Endless HDD space(256,500,...):  ",
     "your perfect monitor size(14,15,...):  "]
Z=list()
for i in txt:
    vorodi=float(input(i))
    Z.append(vorodi)

Z=np.array(Z)
print("The AI agent has started working, please wait......")
Yp=model.predict([Z])
javab=int(Yp[0])
cursor.execute("SELECT name FROM t_gproject.pc_name,t_gproject.test2 WHERE (pc_name.ID=test2.ID) AND test2.ID=%i;"%javab)
r=cursor.fetchone()
time.sleep(2)
print("\n","we recomend you ------>>",r[0])
