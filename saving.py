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
saving = quandl.get("FRED/PSAVERT", start_date="1990-01-01", authtoken="YOUR_KEY")  # Import data using API call and applicable rules
jobs = quandl.get("FRED/UNRATE", start_date="1990-12-31", end_date="2018-03-01", authtoken="YOUR_KEY")

#print(saving,jobs)                        # Show data in workspace

saving.to_csv('save.csv')             # Export Data as .csv
jobs.to_csv('jobs.csv')

headers=['Date','Value','Value']

df1=pd.read_csv('save.csv',names=headers)
df2=pd.read_csv('save.csv',names=headers)
df3=pd.read_csv('jobs.csv',names=headers)

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
axes.set_yticks(axes.get_yticks()[::6])
axes.set_xticks(axes.get_xticks()[::18])

#Label graph
plt.title('Unemployment Rate vs Saving Rate (1990 - 2018)')

plt.gca().legend(('Saving','Unemployment'))        #Set and label legend

#Show plot
plt.show()
