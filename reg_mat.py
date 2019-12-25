#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np

#A = np.matrix([0,2,1])
A = np.random.rand(1,3) #    why not working for random matrixes
print("A = ")
print(A)
print(A.shape)
print()
#X = np.matrix( [[1,2,6], [5,10,0], [0,10,10]] )
X = np.random.rand(3,3)
print("X = ")
print(X)
print(X.shape)
print()
Y = np.dot(X,A.transpose())
print("Y = ")
print(Y)
print(Y.shape)
print()
reg_A = np.dot(np.linalg.inv(np.dot(X.transpose(),X)),np.dot(X.transpose(),Y))     # formula for LS method
print("REG_A = ")
print(reg_A)


# In[41]:


A = np.random.rand(1,3)
print("A = ")
print(A)
print()
X = np.random.rand(3,3)
print("X = ")
print(X)
print()
#Y = X*A.transpose()
Y = np.dot(X,A.transpose())
print("Y = ")
print(Y)
print(Y.shape)
print()


# In[ ]:




