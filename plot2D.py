import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

infile = './' # Change this to the data set you want to use.

colNames = ['x', 'y', 'id']
colVals = []

with open(infile, mode='r') as file:
  fl = file.readlines()
  for pt in fl:
    latLong = pt.strip().split(' ')
    latLong[0] = float(latLong[0])
    latLong[1] = float(latLong[1])
    colVals.append(latLong)

# This is to remove noise
temp = zip(*colVals)
temp = [item for item in colVals if item[2] != '0'] # scatter 2D


data = pd.DataFrame(temp, columns=colNames)

fig = px.scatter(data, x='x', y='y', color='id');
fig.show()

exit()