#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 입력을 받습니다.
number = int(input("정수 입력> "))

# 조건문을 사용합니다.
if number % 2 == 0:
    # 조건이 참일 때, 즉 짝수 조건
    print("짝수입니다.")
    # 조건이 거짓일 때, 즉 홀수 조건
else:
    print("홀수입니다.")

