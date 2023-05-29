#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


l = [x for x in range(5)]   ## produces a list of 5 elements


# In[5]:


s = pd.Series(l)


# In[6]:


s


# In[7]:


### we can access the 3rd element by s of 3


# In[8]:


s[3]


# In[9]:


s = pd.Series(l,index=['a','b','c','d','e'])


# In[10]:


s


# In[11]:


s['e']


# In[12]:


s['d']


# In[13]:


### a new series of arrays
s = pd.Series(l,index['a','b','c','d','d'])


# In[14]:


s['d']


# In[ ]:


### a new array series from the dictionary
data = {'a':1,'b':2,'c':3,'d':4} ## the code adds the indexes of the data


# In[15]:


s


# In[16]:


### let's do more exercises on the same
Council = {'Jomo':2020,'Odero':2017,'Erick':2021,'Jack':0,'Alex':2023}

### indexes of the data are added


# In[17]:


Council


# In[ ]:


### we canm access the data
### let's say we need d and e
s = pd.Series(Data,index=['a','b'])


# In[19]:


s


# In[20]:





# In[ ]:




