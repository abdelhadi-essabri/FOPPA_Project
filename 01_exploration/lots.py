#!/usr/bin/env python
# coding: utf-8

# In[1]:


from functions.utils import *
import warnings

warnings.filterwarnings('ignore')


# # Les attributs

# In[2]:


lots = load_data(path='../donnees/Lots.csv')


# In[3]:


lots


# In[4]:


lot_dtypes = get_dtypes(lots)


# In[5]:


lot_dtypes


# # Attribut lotId

# In[6]:


lotId = lots[['lotId']]


# In[7]:


lotId


# In[8]:


lotId_vc = get_vc(lots, column='lotId')


# In[9]:


lotId_vc


# In[10]:


lotId_na = get_na(lots, column='lotId')


# In[11]:


lotId_na


# In[ ]:





# # Attribut tedCanId

# In[12]:


tedCanId = lots[['tedCanId']]


# In[13]:


tedCanId


# In[14]:


tedCanId_vc = get_vc(lots, column='tedCanId')


# In[15]:


tedCanId_vc


# In[16]:


tedCanId_na = get_na(lots, column='tedCanId')


# In[17]:


tedCanId_na


# In[ ]:





# # Attribut correctionsNb

# In[18]:


correctionsNb = lots[['correctionsNb']]


# In[19]:


correctionsNb


# In[20]:


correctionsNb_vc = get_vc(lots, column='correctionsNb')


# In[21]:


correctionsNb_vc


# In[22]:


correctionsNb_na = get_na(lots, column='correctionsNb')


# In[23]:


correctionsNb_na


# In[ ]:





# # Attribut cancelled

# In[24]:


cancelled = lots[['cancelled']]


# In[25]:


cancelled


# In[26]:


cancelled_vc = get_vc(lots, column='cancelled')


# In[27]:


cancelled_vc


# In[28]:


cancelled_na = get_na(lots, column='cancelled')


# In[29]:


cancelled_na


# In[ ]:





# # Attribut awardDate

# In[30]:


awardDate = lots[['awardDate']]


# In[31]:


awardDate


# In[32]:


awardDate_vc = get_vc(lots, column='awardDate')


# In[33]:


awardDate_vc


# In[34]:


awardDate_na = get_na(lots, column='awardDate')


# In[35]:


awardDate_na


# In[36]:


plot_proportion(
    data=awardDate_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs awardDate', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=False
)


# In[37]:


awardDate_cat = categorized_awardDate(awardDate)


# In[38]:


awardDate_cat


# In[39]:


awardDate_cat_vc = get_vc(awardDate_cat, column='category')


# In[40]:


awardDate_cat_vc 


# In[41]:


plot_proportion(
    data=awardDate_cat_vc,
    xcol='valeur', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs awardDate', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=True
)


# # Attribut awardEstimatedPrice

# In[42]:


awardEstimatedPrice = lots[['awardEstimatedPrice']]


# In[43]:


awardEstimatedPrice


# In[44]:


awardEstimatedPrice_vc = get_vc(lots, column='awardEstimatedPrice')


# In[45]:


awardEstimatedPrice_vc


# In[46]:


awardEstimatedPrice_na = get_na(lots, column='awardEstimatedPrice')


# In[47]:


awardEstimatedPrice_na


# In[48]:


plot_proportion(
    data=awardEstimatedPrice_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de awardEstimatedPrice', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=False
)


# In[49]:


awardEstimatedPrice_cat = categorized_awardEstimatedPrice(awardEstimatedPrice)


# In[50]:


awardEstimatedPrice_cat


# In[51]:


awardEstimatedPrice_cat_vc = get_vc(awardEstimatedPrice_cat, column='category')


# In[52]:


awardEstimatedPrice_cat_vc


# In[53]:


plot_proportion(
    data=awardEstimatedPrice_cat_vc,
    xcol='valeur', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs awardEstimatedPrice', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=True
)


# # Attribut awardPrice

# In[54]:


awardPrice = lots[['awardPrice']]


# In[55]:


awardPrice


# In[56]:


awardPrice_vc = get_vc(lots, column='awardPrice')


# In[57]:


awardPrice_vc


# In[58]:


awardPrice_na = get_na(lots, column='awardPrice')


# In[59]:


awardPrice_na


# In[60]:


plot_proportion(
    data=awardPrice_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de awardPrice', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=False
)


# In[61]:


awardPrice_cat = categorized_awardPrice(awardPrice)


# In[62]:


awardPrice_cat


# In[63]:


awardPrice_cat_vc = get_vc(awardPrice_cat, column='category')


# In[64]:


awardPrice_cat_vc


# In[65]:


plot_proportion(
    data=awardPrice_cat_vc,
    xcol='valeur', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs awardPrice', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=True
)


# # Attribut cpv

# In[66]:


cpv = lots[['cpv']]


# In[67]:


cpv


# In[68]:


cpv_vc = get_vc(lots, column='cpv')


# In[69]:


cpv_vc


# In[70]:


cpv_na = get_na(lots, column='cpv')


# In[71]:


cpv_na


# In[72]:


plot_proportion(
    data=cpv_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de cpv', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=True
)


# In[ ]:





# # Attribut numberTenders

# In[73]:


numberTenders = lots[['numberTenders']]


# In[74]:


numberTenders


# In[75]:


numberTenders_vc = get_vc(lots, column='numberTenders')


# In[76]:


numberTenders_vc


# In[77]:


numberTenders_na = get_na(lots, column='numberTenders')


# In[78]:


numberTenders_na


# In[79]:


plot_proportion(
    data=numberTenders_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de numberTenders', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=False
)


# In[ ]:





# # Attribut onBehalf

# In[80]:


onBehalf = lots[['onBehalf']]


# In[81]:


onBehalf


# In[82]:


onBehalf_vc = get_vc(lots, column='onBehalf')


# In[83]:


onBehalf_vc


# In[84]:


onBehalf_na = get_na(lots, column='onBehalf')


# In[85]:


onBehalf_na


# In[86]:


plot_proportion(
    data=onBehalf_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de onBehalf', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=False
)


# In[ ]:





# # Attribut jointProcurement

# In[87]:


jointProcurement = lots[['jointProcurement']]


# In[88]:


jointProcurement


# In[89]:


jointProcurement_vc = get_vc(lots, column='jointProcurement')


# In[90]:


jointProcurement_vc


# In[91]:


jointProcurement_na = get_na(lots, column='jointProcurement')


# In[92]:


jointProcurement_na


# In[93]:


plot_proportion(
    data=jointProcurement_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de jointProcurement', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=False
)


# In[ ]:





# # Attribut fraAgreement

# In[94]:


fraAgreement = lots[['fraAgreement']]


# In[95]:


fraAgreement


# In[96]:


fraAgreement_vc = get_vc(lots, column='fraAgreement')


# In[97]:


fraAgreement_vc


# In[98]:


fraAgreement_na = get_na(lots, column='fraAgreement')


# In[99]:


fraAgreement_na


# In[ ]:





# # Attribut fraEstimated

# In[100]:


fraEstimated = lots[['fraEstimated']]


# In[101]:


fraEstimated


# In[102]:


fraEstimated_vc = get_vc(lots, column='fraEstimated')


# In[103]:


fraEstimated_vc


# In[104]:


fraEstimated_na = get_na(lots, column='fraEstimated')


# In[105]:


fraEstimated_na


# In[106]:


plot_proportion(
    data=fraEstimated_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de fraEstimated', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=False
)


# In[ ]:





# # Attribut lotsNumber

# In[107]:


lotsNumber = lots[['lotsNumber']]


# In[108]:


lotsNumber


# In[109]:


lotsNumber_vc = get_vc(lots, column='lotsNumber')


# In[110]:


lotsNumber_vc


# In[111]:


lotsNumber_na = get_na(lots, column='lotsNumber')


# In[112]:


lotsNumber_na


# In[113]:


plot_proportion(
    data=lotsNumber_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de lotsNumber', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=False
)


# In[114]:


lotsNumber_cat = categorized_lotNumber(lotsNumber)


# In[115]:


lotsNumber_cat


# In[116]:


lotsNumber_cat_vc = get_vc(lotsNumber, column='category')


# In[117]:


lotsNumber_cat_vc


# In[118]:


plot_proportion(
    data=lotsNumber_cat_vc,
    xcol='valeur', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs lotsNumber', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=True
)


# In[ ]:





# # Attribut accelerated

# In[119]:


accelerated = lots[['accelerated']]


# In[120]:


accelerated


# In[121]:


accelerated_vc = get_vc(lots, column='accelerated')


# In[122]:


accelerated_vc


# In[123]:


accelerated_na = get_na(lots, column='accelerated')


# In[124]:


accelerated_na


# In[125]:


plot_proportion(
    data=accelerated_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de accelerated', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=True
)


# In[ ]:





# # Attribut outOfDirectives

# In[126]:


outOfDirectives = lots[['outOfDirectives']]


# In[127]:


outOfDirectives


# In[128]:


outOfDirectives_vc = get_vc(lots, column='outOfDirectives')


# In[129]:


outOfDirectives_vc


# In[130]:


outOfDirectives_na = get_na(lots, column='outOfDirectives')


# In[131]:


outOfDirectives_na


# In[ ]:





# # Attribut contractorSme

# In[132]:


contractorSme = lots[['contractorSme']]


# In[133]:


contractorSme


# In[134]:


contractorSme_vc = get_vc(lots, column='contractorSme')


# In[135]:


contractorSme_vc


# In[136]:


contractorSme_na = get_na(lots, column='contractorSme')


# In[137]:


contractorSme_na


# In[138]:


plot_proportion(
    data=contractorSme_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de contractorSme', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=True
)


# In[139]:


contractorSme_cat = categorized_contractorSme(contractorSme)


# In[140]:


contractorSme_cat


# In[141]:


contractorSme_cat_vc = get_vc(contractorSme_cat, column='category')


# In[142]:


contractorSme_cat_vc


# In[143]:


plot_proportion(
    data=contractorSme_cat_vc,
    xcol='valeur', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs contractorSme', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=True
)


# In[ ]:





# # Attribut numberTendersSme

# In[144]:


numberTendersSme = lots[['numberTendersSme']]


# In[145]:


numberTendersSme


# In[146]:


numberTendersSme_vc = get_vc(lots, column='numberTendersSme')


# In[147]:


numberTendersSme_vc


# In[148]:


numberTendersSme_na = get_na(lots, column='numberTendersSme')


# In[149]:


numberTendersSme_na


# In[150]:


plot_proportion(
    data=numberTendersSme_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de numberTendersSme', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=True
)


# In[ ]:





# # Attribut subContracted

# In[151]:


subContracted = lots[['subContracted']]


# In[152]:


subContracted


# In[153]:


subContracted_vc = get_vc(lots, column='subContracted')


# In[154]:


subContracted_vc


# In[155]:


subContracted_na = get_na(lots, column='subContracted')


# In[156]:


subContracted_na


# In[157]:


plot_proportion(
    data=subContracted_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de subContracted', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=False
)


# In[ ]:





# # Attribut gpa

# In[158]:


gpa = lots['gpa']


# In[159]:


gpa


# In[160]:


gpa_vc = get_vc(lots, column='gpa')


# In[161]:


gpa_vc


# In[162]:


gpa_na = get_na(lots, column='gpa')


# In[163]:


gpa_na


# In[164]:


plot_proportion(
    data=gpa_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de gpa', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=False
)


# In[ ]:





# # Attribut multipleCae

# In[165]:


multipleCae = lots[['multipleCae']]


# In[166]:


multipleCae


# In[167]:


multipleCae_vc = get_vc(lots, column='multipleCae')


# In[168]:


multipleCae_vc


# In[169]:


multipleCae_na = get_na(lots, column='multipleCae')


# In[170]:


multipleCae_na


# In[171]:


plot_proportion(
    data=multipleCae_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de multipleCae', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=False
)


# In[ ]:





# # Attribut typeOfContract

# In[172]:


typeOfContract = lots[['typeOfContract']]


# In[173]:


typeOfContract


# In[174]:


typeOfContract_vc = get_vc(lots, column='typeOfContract')


# In[175]:


typeOfContract_vc


# In[176]:


typeOfContract_na = get_na(lots, column='typeOfContract')


# In[177]:


typeOfContract_na


# In[ ]:





# # Attribut topType

# In[178]:


topType = lots[['topType']]


# In[179]:


topType


# In[180]:


topType_vc = get_vc(lots, column='topType')


# In[181]:


topType_vc


# In[182]:


topType_na = get_na(lots, column='topType')


# In[183]:


topType_na


# In[184]:


plot_proportion(
    data=topType_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de topType', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=True
)


# # Attribut renewal

# In[185]:


renewal = lots[['renewal']]


# In[186]:


renewal


# In[187]:


renewal_vc = get_vc(lots, column='renewal')


# In[188]:


renewal_vc


# In[189]:


renewal_na = get_na(lots, column='renewal')


# In[190]:


renewal_na


# In[191]:


plot_proportion(
    data=renewal_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de renewal', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=False
)


# In[ ]:





# # Attribut contractDuration

# In[192]:


contractDuration = lots[['contractDuration']]


# In[193]:


contractDuration


# In[194]:


contractDuration_vc = get_vc(lots, column='contractDuration')


# In[195]:


contractDuration_vc


# In[196]:


contractDuration_na = get_na(lots, column='contractDuration')


# In[197]:


contractDuration_na


# In[198]:


plot_proportion(
    data=contractDuration_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de contractDuration', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=False
)


# In[ ]:





# # Attribut publicityDuration

# In[199]:


publicityDuration = lots[['publicityDuration']]


# In[200]:


publicityDuration


# In[201]:


publicityDuration_vc = get_vc(lots, column='publicityDuration')


# In[202]:


publicityDuration_vc


# In[203]:


publicityDuration_na = get_na(lots, column='publicityDuration')


# In[204]:


publicityDuration_na


# In[205]:


plot_proportion(
    data=publicityDuration_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des catégories de valeurs de publicityDuration', 
    xtitle='catégorie de valeur', 
    ytitle='proportion',
    logy=False
)


# In[ ]:




