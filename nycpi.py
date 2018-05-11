# Importing Quandl data for analysis (using Pandas, Matplotlib, Numpy)
import quandl
import random
import pandas as pd
import csv                        # Allows importation/exporation of data as .csv file
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import numpy as np

#Account for reporting date slippage between Jobs and Savings figures (BLS vs BEA)
nycpi = quandl.get("FRED/CUURA101SA0", start_date="1990-01-01", authtoken="_uhAD1-g9JdY2teUwiAb")  # Import data using API call and applicable rules
cpi = quandl.get("FRED/CPIAUCSL", start_date="1990-01-01", authtoken="_uhAD1-g9JdY2teUwiAb")

nycpi.to_csv('nycpi.csv')             # Export Data as .csv
cpi.to_csv('cpi.csv')

headers=['Date','Value','Value']

df1=pd.read_csv('nycpi.csv',names=headers)
df2=pd.read_csv('nycpi.csv',names=headers)
df3=pd.read_csv('cpi.csv',names=headers)

z=df1['Date']                                     # Define vectors spaces
x=df2['Value']
y=df3['Value']

print(z,x,y)

plt.plot(z,x,y)                                    # Plot using newly defined variables

axes = plt.gca()                                   # Define axes
plt.ylim(0, 10)                         # Set y axis limits
plt.ylim(plt.ylim()[::-1])                         # invert order of numbers on y axis

plt.gcf().autofmt_xdate()                          # beautify the x-labels

# Adjust axis scales
axes.set_yticks(axes.get_yticks()[::90])
axes.set_xticks(axes.get_xticks()[::16])

#Label graph
plt.title('New York vs National CPI (1947 - 2018)')

plt.gca().legend(('NY','National'))        #Set and label legend

#Show plot
plt.show()
