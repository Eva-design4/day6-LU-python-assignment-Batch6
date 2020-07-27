#!/usr/bin/env python
# coding: utf-8

# # Assignment 1: 
# 
# Convert to dictionary , In one line code using list comprehension(without using zip method)

# In[1]:


list1 = [1,2,3,4,5,7,8]
list2 = ["a","b","c","d","e"]
my_dict = {list1[i]:list2[i] for i in range(len(list2))}
print(my_dict)


# In[ ]:




