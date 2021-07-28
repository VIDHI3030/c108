import csv
import plotly.express as px
import plotly.figure_factory as ff 
import pandas as pd 

dataFile=pd.read_csv("csv/normal.csv")

fig=ff.create_distplot([dataFile["Weight"].tolist()],["Weight"],show_hist=False)
fig.show()