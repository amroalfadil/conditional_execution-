#!/usr/bin/env python
# coding: utf-8

# In[1]:


12 < 4


# In[2]:


6>3


# In[3]:


8 >= 8


# In[4]:


2 <= 17


# In[5]:


5 == 4


# In[6]:


2 ** 3 > 1+5


# In[7]:


100


# In[8]:


1.3


# In[9]:


True


# In[10]:


False


# In[11]:


not True


# In[12]:


not False


# In[13]:


# only one operand comes on the right of the operator


# In[14]:


not not True


# In[15]:


# we try the binary operators next


# In[16]:


True and True


# In[17]:


True and False 


# In[18]:


# just the truth table 


# In[19]:


True or False


# In[20]:


True or True 


# In[21]:


# in or at least one of the operand is true


# In[22]:


# if we try to combined 


# In[23]:


True and False or not True and False


# In[24]:


# what we can do to make it true , the or need one side to be true 


# In[26]:


True and True or not True and False


# In[27]:


# same float and int can be stored in veriables bolean can be store in veriables


# In[28]:


weekend = True


# In[29]:


raining = False


# In[30]:


#go_out = weekend and not raining 


# In[31]:


#go_out


# In[33]:


# we can turne above as function, take boolean as aregumant , or return boolean as a result


# In[34]:


def go_out(weekend,raining):
    return weekend and not raining # will be true only if it is a weekend and not raining.


# In[35]:


go_out(True, True)


# In[36]:


go_out(True, True)


# In[37]:


go_out(False, True)


# comparison operator 

# In[38]:


1 == 1


# In[39]:


# if we do one = we changing the value of x


# In[40]:


x = 42


# In[41]:


x =10


# In[42]:


y =20


# In[43]:


x == y


# In[44]:


y= 10


# In[45]:


x == y


# In[46]:


1 != 1


# In[47]:


1 < 2


# In[48]:


1 > 2


# In[49]:


# above are strict enequalities , blow nonstrict equalities


# In[50]:


1 <= 2


# In[51]:


1 >= 2


# In[52]:


x = 10 


# In[53]:


# if we want to check x between 5 and 20 


# In[54]:


x >= 5 and x <=20


# In[55]:


# python can take diffrent syntax 


# In[56]:


5 <= x <=20


# In[70]:


def go_out(weekend,raining, temperature):
    return weekend and not raining and 20 <= temperature <30 
# will be true only if it is a weekend and not raining.and temperature less than or equal to 20 and less than 30


# In[73]:


go_out(True, False, 29)


# In[74]:


# the line of code is long we can make it shorter 
def go_out(weekend,raining, temperature):
    warm = 20 <= temperature <30 
    return weekend and not raining and warm


# In[75]:


go_out(True , False, 25)


# if and Else Blocks

# In[76]:


if True:
    print("Hello")


# In[77]:


if False:
    print("Hello")


# In[82]:


number = 5
if number >= 100:
    print("number is large")
    number /=2  # number = number/2
else:
    print("number is small")
    number *= 2
print("number is",number)


# Elif Block

# In[83]:


# if we have 3 possible things might happend


# In[89]:


temperature = 19

if 20<= temperature <= 30:
    print("okay")
else: # if you skip aboe block you go to below block
    if temperature < 20:
        print("too cold")
    else:
        print("too hot")
        


# In[90]:


# combine the else and if and make it elif will be easier to follow


# In[91]:


temperature = 19

if 20<= temperature <= 30:
    print("okay")
elif temperature < 20: # if you skip aboe block you go to below block
    print("too cold")
else:
    print("too hot")


# In[92]:


# there is no single way to structre the code you can do it in diffrent ways


# In[94]:


temperature = 35

if temperature < 20:
    print("too cold")
elif temperature <= 30: # if you skip aboe block you go to below block
    print("okay")
else:
    print("too hot")


# In[95]:


# the order is very important make sure it is in order 


# In[ ]:





# In[ ]:





# piecewise Functions

# In[103]:


def absval(x):
    if x > 0: # if x is positive
        return x
    elif x< 0: # elif x is negative 
        return -x
    else:
        return 0
    # what we can do to remove something is redundant 
    


# In[104]:


def absval(x):
    if x >= 0: # if x is positive
        return x
    elif x< 0: # elif x is negative 
        return -x


# In[105]:


def absval(x):
    if x >= 0: # if x is positive
        return x
    else: # elif x is negative 
        return -x


# In[107]:


def absval(x):
    if x >= 0: # if x is positive
        return x
    return -x # sometimes you don't need another else just use return 


# reverse functions

# In[ ]:


def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-2) + fib(n-1)

