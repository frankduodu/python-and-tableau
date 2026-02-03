# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
#data = pd.read_csv("transaction.csv")#
data = pd.read_csv('transaction.csv', sep =';')
CostPerItem = 11.73
SellingPricePerItem = 21.11
#data.info()#
NumberOfItemsPurchased = 6

#creating a column in the dtaframe#
ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = ProfitPerItem * NumberOfItemsPurchased 

SellingPricePerTransaction = SellingPricePerItem *  NumberOfItemsPurchased


CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
#creating new column#

data['CostPerTransaction'] = CostPerTransaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']
data['Markup'] = data['ProfitPerTransaction']/data['CostPerTransaction']
#ROUNDING Markup#
RoundingMarkup = round(data['Markup'], 2)
data['Markup'] = RoundingMarkup
#print(data['Day'].dtype)#
#print(data['Month'].dtype)#
#print(data['Year'].dtype)#
#converting date types for concantenation#
Day = data['Day'].astype(str)
print(Day.dtype)
Year = data['Year'].astype(str)
print(Year.dtype)
Date = Day +"-" + data['Month']+ '-'+ Year
data['Date'] = Date
#extracting row from columns#
data.iloc[1]
data.iloc[0:3]
#brings in all rows on the 2nd column#
data.iloc[:,2]
#brings in all rows on the 2nd column#
data.iloc[4,2]
data.iloc[4,3]
#spliting column with mixed variables into separate column#
Split_Col = data['ClientKeywords'].str.split(',', expand = True)
data['ClientAge'] = Split_Col[0]
data['ClientType'] = Split_Col[1]
data['LengthOfContract'] = Split_Col[2] 
#removing unwanted characters#
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '')
#converting upper case characters to lower case#
data['ItemDescription'] = data['ItemDescription'].str.lower()
# merging files by importing new data/files by pandas read function#
seasons = pd.read_csv('value_inc_seasons.csv')

#splitting seasons data into separate colums#
seasons_split = seasons['Month;Season'].str.split(';', expand = True)
seasons['Month'] = seasons_split[0]
seasons['Season'] = seasons_split[1]
seasons = seasons.drop('Month;Season', axis =1)
#merging files#
data = pd.merge(data,seasons, on = 'Month')
data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis =1)
data = data.drop(['Year','Month'], axis=1)
#Exporting files #
data.to_csv('ValueInc_Cleaned.csv', index = False)
