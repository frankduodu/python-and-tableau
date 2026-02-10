# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 15:23:45 2026

@author: user
"""
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#importing excel #
data = pd.read_excel('articles.xlsx')
#describing the data#
data.describe()
#column information#
data.info()
#counting the number of articles per source#
data.groupby(['source_id'])['article_id'].count()
articlespersource = data.groupby(['source_id'])['article_id'].count()
data.groupby(['source_id'])['engagement_reaction_count'].sum()
articlereaction = data.groupby(['source_id'])['engagement_reaction_count'].sum()
data = data.drop(['engagement_comment_plugin_count'], axis = 1)

#Defining function and for loops#
def favfood(menu):
    for x in (menu):
        print(x + ' ' 'top food')        
fastfood = ['rice','fufu', 'banku']
favfood(fastfood)

#creating a keyword#
keyword = 'crash'

#lets create a for loop to isolate each title row#
# length = len(data)
# keyword_flag = []
# for x in range(0,10):
#     heading = data['title'][x]
#     if keyword in heading:
#         flag =1
#     else:
#         flag = 0
#     keyword_flag.append(flag)

#creating a function#
def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag =1
            else:
                flag = 0
        except:
            
            flag = 0   
        keyword_flag.append(flag)
    return keyword_flag
keywordflag = keywordflag('murder')
        
#creating a new column to add the keyword#
data['keyword_flag'] = pd.Series(keywordflag)
# flagplot = data.groupby(['keyword_flag']).size()

#conducting sentiment analysis using vader#
sent_int = SentimentIntensityAnalyzer()
text = data['title'][16]
sent = sent_int.polarity_scores(text)
neg = sent['neg']
pos = sent['pos']
neu = sent['neu']


title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
length = len(data)
for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
      
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
            neg = 0
            pos = 0
            neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment 
data['title_neu_sentiment'] = title_neu_sentiment

data.to_excel('Blogme cleaned.xlsx', sheet_name = 'Blogmedata', index = False)  














