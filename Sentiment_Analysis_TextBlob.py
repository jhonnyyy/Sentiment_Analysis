#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from textblob import TextBlob

#We have considered the data in form of list of dict
data=[{'text':'ENTER TEXT HERE'},
      {'text':'ENTER TEXT HERE'},
      .....]


#To calculate the subjectivity of text
def subjectivity_score(text):
    return TextBlob(text).sentiment.subjectivity

#To calculate the polarity of text
def polarity_score(text):
    return TextBlob(text).sentiment.polarity

#To define the thresholds for the categorization
def getAnalysis(score):
    if score < 0:
        return "Negative"
    elif score == 0:
        return "Neutral"
    else:
        return "Positive"
    
    
    
def sentiment_analysis(list: data):
    for line in data:
        line['subjectivity_score']=subjectivity_score(line['text'])
        line['polarity_score']=polarity_score(line['text'])
        line['sentiment']=getAnalysis(line['polarity_score'])
        
    
    return data


#To run the code
sentiment_analysis(data)

#Value returned will be a list of dict with 3 more keys added to the each dict (as shown below)
"""
{'text': 'How are you doing',
  'subjectivity_score': 0.0,
  'polarity_score': 0.0,
  'sentiment': 'Neutral'}
"""


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[47]:





# In[48]:





# In[49]:





# In[52]:





# In[ ]:





# In[ ]:




