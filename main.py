#!/usr/bin/env python
# coding: utf-8

# In[1]:


# main.py 파일
import test_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))

