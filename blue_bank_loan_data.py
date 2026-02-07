# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 17:14:19 2026

@author: user
"""
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# pulling and opening json file #

json_file = open('loan_data_json.json')
data =json.load(json_file)
#converting json file to dataframe#
loandata = pd.DataFrame(data)
#checking unique values in specific column#
loandata['purpose'].unique()
#describing the data#
loandata.describe()
loandata['dti'].describe()
#converting log annual income to annual income#
income = np.exp(loandata['log.annual.inc'])
loandata['AnnualIncome'] =  income
#using for loop and if statement to assign category to Fico#
length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 600 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
             cat = 'Good'
        elif category >= 700:
             cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = "Error-Unknown"
    ficocat.append(cat)
ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat
# i= 1
# while i<10:
#     print(i)
#     i = i + 1

# using df.loc condition#
#df.loc[df['column name'], condition, new column name] equate it the value#
loandata.loc[loandata['int.rate'] >= 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'
#using groupby to collect data at a specific coulmn by row fico.category#
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color ='red',width = 0.2)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'green', width = 0.1)
plt.show()

#scatter plot#
xpoint = loandata['dti']
ypoint = loandata['AnnualIncome']
plt.scatter(xpoint,ypoint, color = 'blue')
plt.show()

#converting the files to csv#
loandata.to_csv('loan_cleaned.csv', index = True)


    
         
        

