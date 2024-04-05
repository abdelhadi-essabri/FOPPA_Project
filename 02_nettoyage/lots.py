#!/usr/bin/env python
# coding: utf-8

# In[1]:


from functions.utils import *
import warnings

warnings.filterwarnings('ignore')

# In[2]:


lots = load_data(path='donnees/Lots.csv')

# In[3]:

print()
print("# TABLE Lots avant nettoyage")
print(lots)

# In[ ]:


# # Attribut awardDate

# In[4]:


awardDate = lots[['awardDate']]

# In[5]:

print()
print("# Attribut awardDate avant nettoyage")
print(awardDate)

# In[6]:


awardDate = clean_awardDate(awardDate)

# In[7]:

print()
print("# Attribut awardDate après nettoyage")
print(awardDate)

# In[8]:


lots = replace_original_with_cleaned(
    original=lots,
    column='awardDate',
    cleaned=awardDate['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut awardEstimatedPrice

# In[9]:


awardEstimatedPrice = lots[['awardEstimatedPrice']]

# In[10]:

print()
print("# Attribut awardEstimatedPrice avant nettoyage")
print(awardEstimatedPrice)

# In[11]:


awardEstimatedPrice = clean_awardEstimatedPrice(awardEstimatedPrice)

# In[12]:

print()
print("# Attribut awardEstimatedPrice après nettoyage")
print(awardEstimatedPrice)

# In[13]:


lots = replace_original_with_cleaned(
    original=lots,
    column='awardEstimatedPrice',
    cleaned=awardEstimatedPrice['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut awardPrice

# In[14]:


awardPrice = lots[['awardPrice']]

# In[15]:

print()
print("# Attribut awardPrice avant nettoyage")
print(awardPrice)

# In[16]:


awardPrice = clean_awardPrice(awardPrice)

# In[17]:

print()
print("# Attribut awardPrice après nettoyage")
print(awardPrice)

# In[18]:


lots = replace_original_with_cleaned(
    original=lots,
    column='awardPrice',
    cleaned=awardPrice['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut cpv

# In[19]:


cpv = lots[['cpv']]

# In[20]:

print()
print("# Attribut cpv avant nettoyage")
print(cpv)

# In[21]:


cpv = clean_cpv(cpv)

# In[22]:

print()
print("# Attribut cpv après nettoyage")
print(cpv)

# In[23]:


lots = replace_original_with_cleaned(
    original=lots,
    column='cpv',
    cleaned=cpv['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut numberTenders

# In[24]:


numberTenders = lots[['numberTenders']]

# In[25]:

print()
print("# Attribut numberTenders avant nettoyage")
print(numberTenders)

# In[26]:


numberTenders = clean_numberTenders(numberTenders)

# In[27]:

print()
print("# Attribut numberTenders après nettoyage")
print(numberTenders)

# In[28]:


lots = replace_original_with_cleaned(
    original=lots,
    column='numberTenders',
    cleaned=numberTenders['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut onBehalf

# In[29]:


onBehalf = lots[['onBehalf']]

# In[30]:

print()
print("# Attribut onBehalf avant nettoyage")
print(onBehalf)

# In[31]:


onBehalf = clean_onBehalf(onBehalf)

# In[32]:

print()
print("# Attribut onBehalf après nettoyage")
print(onBehalf)

# In[33]:


lots = replace_original_with_cleaned(
    original=lots,
    column='onBehalf',
    cleaned=onBehalf['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut jointProcurement

# In[34]:


jointProcurement = lots[['jointProcurement']]

# In[35]:

print()
print("# Attribut jointProcurement avant nettoyage")
print(jointProcurement)

# In[36]:


jointProcurement = clean_jointProcurement(jointProcurement)

# In[37]:

print()
print("# Attribut jointProcurement après nettoyage")
print(jointProcurement)

# In[38]:


lots = replace_original_with_cleaned(
    original=lots,
    column='jointProcurement',
    cleaned=jointProcurement['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut fraEstimated

# In[39]:


fraEstimated = lots[['fraEstimated']]

# In[40]:

print()
print("# Attribut fraEstimated avant nettoyage")
print(fraEstimated)

# In[41]:


fraEstimated = clean_fraEstimated(fraEstimated)

# In[42]:

print()
print("# Attribut fraEstimated après nettoyage")
print(fraEstimated)

# In[43]:


lots = replace_original_with_cleaned(
    original=lots,
    column='fraEstimated',
    cleaned=fraEstimated['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut lotsNumber

# In[44]:


lotsNumber = lots[['lotsNumber']]

# In[45]:

print()
print("# Attribut lotsNumber avant nettoyage")
print(lotsNumber)

# In[46]:


lotsNumber = clean_lotsNumber(lotsNumber)

# In[47]:

print()
print("# Attribut lotsNumber après nettoyage")
print(lotsNumber)

# In[48]:


lots = replace_original_with_cleaned(
    original=lots,
    column='lotsNumber',
    cleaned=lotsNumber['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut accelerated

# In[49]:


accelerated = lots[['accelerated']]

# In[50]:

print()
print("# Attribut accelerated avant nettoyage")
print(accelerated)

# In[51]:


accelerated = clean_accelerated(accelerated)

# In[52]:

print()
print("# Attribut accelerated après nettoyage")
print(accelerated)

# In[53]:


lots = replace_original_with_cleaned(
    original=lots,
    column='accelerated',
    cleaned=accelerated['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# # Attribut contractorSme

# In[54]:


contractorSme = lots[['contractorSme']]

# In[55]:

print()
print("# Attribut contractorSme avant nettoyage")
print(contractorSme)

# In[56]:


contractorSme = clean_contractorSme(contractorSme)

# In[57]:

print()
print("# Attribut contractorSme après nettoyage")
print(contractorSme)

# In[58]:


lots = replace_original_with_cleaned(
    original=lots,
    column='contractorSme',
    cleaned=contractorSme['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut numberTendersSme

# In[59]:


numberTendersSme = lots[['numberTendersSme']]

# In[60]:

print()
print("# Attribut numberTendersSme avant nettoyage")
print(numberTendersSme)

# In[61]:


numberTendersSme = clean_numberTendersSme(numberTendersSme)

# In[62]:

print()
print("# Attribut numberTendersSme après nettoyage")
print(numberTendersSme)

# In[63]:


lots = replace_original_with_cleaned(
    original=lots,
    column='numberTendersSme',
    cleaned=numberTendersSme['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut subContracted

# In[64]:


subContracted = lots[['subContracted']]

# In[65]:

print()
print("# Attribut subContracted avant nettoyage")
print(subContracted)

# In[66]:


subContracted = clean_subContracted(subContracted)

# In[67]:

print()
print("# Attribut subContracted après nettoyage")
print(subContracted)

# In[68]:


lots = replace_original_with_cleaned(
    original=lots,
    column='subContracted',
    cleaned=subContracted['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut gpa

# In[69]:


gpa = lots[['gpa']]

# In[70]:

print()
print("# Attribut gpa avant nettoyage")
print(gpa)

# In[71]:


gpa = clean_gpa(gpa)

# In[72]:

print()
print("# Attribut gpa après nettoyage")
print(gpa)

# In[73]:


lots = replace_original_with_cleaned(
    original=lots,
    column='gpa',
    cleaned=gpa['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut multipleCae

# In[74]:


multipleCae = lots[['multipleCae']]

# In[75]:

print()
print("# Attribut multipleCae avant nettoyage")
print(multipleCae)

# In[76]:


multipleCae = clean_multipleCae(multipleCae)

# In[77]:

print()
print("# Attribut multipleCae après nettoyage")
print(multipleCae)

# In[78]:


lots = replace_original_with_cleaned(
    original=lots,
    column='multipleCae',
    cleaned=multipleCae['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut topType

# In[79]:


topType = lots[['topType']]

# In[80]:

print()
print("# Attribut topType avant nettoyage")
print(topType)

# In[81]:


topType = clean_topType(topType)

# In[82]:

print()
print("# Attribut topType après nettoyage")
print(topType)

# In[83]:


lots = replace_original_with_cleaned(
    original=lots,
    column='topType',
    cleaned=topType['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut renewal

# In[84]:


renewal = lots[['renewal']]

# In[85]:

print()
print("# Attribut renewal avant nettoyage")
print(renewal)

# In[86]:


renewal = clean_renewal(renewal)

# In[87]:

print()
print("# Attribut renewal après nettoyage")
print(renewal)

# In[88]:


lots = replace_original_with_cleaned(
    original=lots,
    column='renewal',
    cleaned=renewal['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut contractDuration

# In[89]:


contractDuration = lots[['contractDuration']]

# In[90]:

print()
print("# Attribut contractDuration avant nettoyage")
print(contractDuration)

# In[91]:


contractDuration = clean_contractDuration(contractDuration)

# In[92]:

print()
print("# Attribut contractDuration après nettoyage")
print(contractDuration)

# In[93]:


lots = replace_original_with_cleaned(
    original=lots,
    column='contractDuration',
    cleaned=contractDuration['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# # Attribut publicityDuration

# In[94]:


publicityDuration = lots[['publicityDuration']]

# In[95]:

print()
print("# Attribut publicityDuration avant nettoyage")
print(publicityDuration)

# In[96]:


publicityDuration = clean_publicityDuration(publicityDuration)

# In[97]:

print()
print("# Attribut publicityDuration après nettoyage")
print(publicityDuration)

# In[98]:


lots = replace_original_with_cleaned(
    original=lots,
    column='publicityDuration',
    cleaned=publicityDuration['cleaned'].values,
    path='donnees/lots_cleaned.csv'
)

# In[ ]:


# In[99]:

print()
print("# Table lots après nettoyage")
print(lots)

# In[ ]:
