import csv
import plotly.express as px
import plotly.figure_factory as ff 
import pandas as pd 

dataFile=pd.read_csv("csv/average.csv")

fig=ff.create_distplot([dataFile["Avg Rating"].tolist()],["Avg Rating"],show_hist=False)
fig.show()