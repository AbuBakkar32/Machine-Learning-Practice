
import matplotlib.pyplot as plt



# In[2]:


import pandas as pd


# In[3]:


df = pd.DataFrame({'A':range(10),'B':range(5,15)})


# In[10]:


df.plot.line(title='Info')


# In[14]:


plt.plot(df.A, label='A')
plt.plot(df.B, label='B')
plt.xlabel('index')
plt.ylabel('values')
plt.title('Info')
plt.legend()


# In[16]:


plt.scatter(x=df.A,y=df.B, s=10)


# In[17]:


import numpy as np
df = pd.DataFrame({'X1': np.arange(10)})


# In[18]:


df['X2'] = df.X1 * df.X1


# In[20]:


df['X3'] = df.X1 * df.X1 * df.X1


# In[21]:


df


# In[37]:


df.plot(linewidth=5,colormap='Set3', title='degree info')


# In[38]:


from sklearn.datasets import load_iris


# In[39]:


iris = load_iris()


# In[40]:


iris.feature_names


# In[43]:


iris.target_names


# In[46]:


plt.scatter(x=iris.data[:,0],y=iris.data[:,1],c=iris.target, s=iris.data[:,2]*10)
plt.xlabel('sepel length')
plt.ylabel('sepel width')
plt.title('IRIS')


# In[48]:


df.plot.bar()


# In[50]:


X = iris.data[:,0]


# In[51]:


Y = iris.data[:,1]


# In[53]:


plt.scatter(X,Y,s=10)


# In[54]:


income_data = pd.read_csv('https://raw.githubusercontent.com/zekelabs/machine-learning-for-beginners/master/data/adult.data.txt', header=None)


# In[55]:


income_data.columns = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship'
        ,'race','sex','capital-gain','capital-loss','hours-per-week','native-country','Salary']


# In[61]:


plt.scatter(income_data['education-num'],income_data['hours-per-week'], s=1, alpha=.1)


# In[66]:


pd.DataFrame(data = iris.data, columns=iris.feature_names)


# In[ ]:




