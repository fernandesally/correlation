import csv
import numpy as np
import plotly.express as px

def getDataSource(path):
  coffee=[]
  hours=[]
  with open(path) as csv_file:
    df=csv.DictReader(csv_file)
    for row in df:
        coffee.append(float(row["Coffee in ml"]))  
        hours.append(float(row["sleep in hours"]))
  return{"x":coffee,"y":hours}

def findcor(datasource):
    corrr=np.corrcoef(datasource["x"],datasource["y"])
    print(corrr)

data="cups of coffee vs hours of sleep.csv"
datasource=getDataSource(data)
findcor(datasource)