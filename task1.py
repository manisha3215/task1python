#!/usr/bin/env python
# coding: utf-8

# In[5]:


def outerfun(a,b=3):
    def innersum(a,b=3):
        return a+b
    s=innersum(5)
    return s
outerfun(5)
    
    
    


# In[11]:


str=input('enter a string')
s=''
c=''
for i in str:
    if (i.islower()):
        s=s+i
    else:
        c=c+i
print(s+c)
            


# In[13]:


list1=[1,2,3,4,5,6,7]
list2=[]
for i in list1:
    if i%2==0:
        list2.append(i)
        list1.remove(i)
print(list1)
print(list2)
        


# In[18]:


sample={ 88:'physics',  75:'maths',    72:'chemistry', 89:'Basic electrical' }
list=[]
list=sample.keys()
print(list)
i=min(list)
print(sample[i])


# In[19]:


S1={1,2,3,4,5,6,7,8,9}
S2={1,3,4,6,8,11,22,34,51,67}
S1=S1.difference(S2)
print(S1)


# In[ ]:



    


# In[ ]:





i=int(input('enter 1 for add,2 for substract,3 for multiply,4 for divide'))
print('enter two numbers')
a=int(input())
b=int(input())
if (i==1):
    add(a,b)
elif (i==2):
    sub(a,b)
elif (i==3):
    multiply(a,b)
elif (i==4):
    divide(a,b)
else:
    print('wrong choice')

def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x//y)


# In[ ]:




