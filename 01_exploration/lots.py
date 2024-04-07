#!/usr/bin/env python
# coding: utf-8

# In[1]:


from functions.utils_lots import *
import warnings

warnings.filterwarnings('ignore')

# # Les attributs

# In[2]:


lots = load_data(path='donnees/Lots.csv')

# In[3]:
print("\n")
print("# Table lots")
print(lots)

# In[4]:


lot_dtypes = get_dtypes(lots)

# In[5]:


lot_dtypes

# # Attribut lotId

# In[6]:


lotId = lots[['lotId']]

# In[7]:

print("\n")
print("# Attribut lotId")
print(lotId)

# In[8]:


lotId_vc = get_vc(lots, column='lotId')

# In[9]:

print("\n")
print("## Occurences des valeurs de l'attribut lotId")
print(lotId_vc)

# In[10]:


lotId_na = get_na(lots, column='lotId')

# In[11]:

print("\n")
print("## Problèmes de l'attribut lotId")
print(lotId_na)

# In[ ]:


# # Attribut tedCanId

# In[12]:


tedCanId = lots[['tedCanId']]

# In[13]:

print("\n")
print("# Attribut tedCanId")
print(tedCanId)

# In[14]:


tedCanId_vc = get_vc(lots, column='tedCanId')

# In[15]:

print("\n")
print("## Occurences des valeurs de l'attribut tedCanId")
print(tedCanId_vc)

# In[16]:


tedCanId_na = get_na(lots, column='tedCanId')

# In[17]:

print("\n")
print("## Problèmes de l'attribut tedCanId")
print(tedCanId_na)

# In[ ]:


# # Attribut correctionsNb

# In[18]:


correctionsNb = lots[['correctionsNb']]

# In[19]:

print("\n")
print("# L'attribut correctionsNb")
print(correctionsNb)

# In[20]:


correctionsNb_vc = get_vc(lots, column='correctionsNb')

# In[21]:

print("\n")
print("## L'occurrence des valeurs de l'attribut orrectionsNb")
print(correctionsNb_vc)

# In[22]:


correctionsNb_na = get_na(lots, column='correctionsNb')

# In[23]:

print("\n")
print("## Les problèmes de l'attribut correctionsNb")
print(correctionsNb_na)

# In[ ]:


# # Attribut cancelled

# In[24]:


cancelled = lots[['cancelled']]

# In[25]:

print("\n")
print("# Attribut cancelled")
print(cancelled)

# In[26]:

cancelled_vc = get_vc(lots, column='cancelled')

# In[27]:

print("\n")
print("## Occurrences des valeurs de l'attribut cancelled")
print(cancelled_vc)

# In[28]:

cancelled_na = get_na(lots, column='cancelled')

# In[29]:

print("\n")
print("## Problèmes de l'attribut cancelled")
print(cancelled_na)

# In[ ]:


# # Attribut awardDate

# In[30]:


awardDate = lots[['awardDate']]

# In[31]:

print("\n")
print("# Attribut awardDate")
print(awardDate)

# In[32]:


awardDate_vc = get_vc(lots, column='awardDate')

# In[33]:

print("\n")
print("## Occurrences des valeurs de l'attribut awardDate")
print(awardDate_vc)

# In[34]:

awardDate_na = get_na(lots, column='awardDate')

# In[35]:

print("\n")
print("## Problèmes de l'attribut awardDate")
print(awardDate_na)

# In[36]:

print("\n")
print("## Problèmes de l'attribut awardDate: images/01_problemes_awardDate_01.png")
plot_proportion(
    data=awardDate_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs awardDate',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_awardDate_01.png',
    logy=False
)

# In[37]:


awardDate_cat = categorized_awardDate(awardDate)

# In[38]:

print("\n")
print("## Catégorisation des problèmes de l'attribut awardDate")
print(awardDate_cat)

# In[39]:

awardDate_cat_vc = get_vc(awardDate_cat, column='category')

# In[40]:

print("\n")
print("## Occurrences des catégories de problèmes de l'attribut awardDate")
print(awardDate_cat_vc)

# In[41]:

print("\n")
print("## Problèmes de l'attribut awardDate: images/01_problemes_awardDate_02.png")
plot_proportion(
    data=awardDate_cat_vc,
    xcol='valeur',
    ycol='proportion',
    title='Proportion des catégories de valeurs awardDate',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_awardDate_02.png',
    logy=True
)

# # Attribut awardEstimatedPrice

# In[42]:


awardEstimatedPrice = lots[['awardEstimatedPrice']]

# In[43]:

print("\n")
print("# Attribut awardEstimatedPrice")
print(awardEstimatedPrice)

# In[44]:


awardEstimatedPrice_vc = get_vc(lots, column='awardEstimatedPrice')

# In[45]:

print("\n")
print("## Occurrences des valeurs de l'attribut awardEstimatedPrice")
print(awardEstimatedPrice_vc)

# In[46]:

awardEstimatedPrice_na = get_na(lots, column='awardEstimatedPrice')

# In[47]:

print("\n")
print("## Problèmes de l'attribut awardEstimatedPrice")
print(awardEstimatedPrice_na)

# In[48]:

print("\n")
print("## Problèmes de l'attribut awardEstimatedPrice: images/01_problemes_awardEstimatedPrice_01.png")
plot_proportion(
    data=awardEstimatedPrice_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de awardEstimatedPrice',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_awardEstimatedPrice_01.png',
    logy=False
)

# In[49]:


awardEstimatedPrice_cat = categorized_awardEstimatedPrice(awardEstimatedPrice)

# In[50]:

print("\n")
print("## Catégorisation des problèmes de l'attribut awardEstimatedPrice")
print(awardEstimatedPrice_cat)

# In[51]:


awardEstimatedPrice_cat_vc = get_vc(awardEstimatedPrice_cat, column='category')

# In[52]:

print("\n")
print("## Occurrences des catégories de problèmes de l'attribut awardEstimatedPrice")
print(awardEstimatedPrice_cat_vc)

# In[53]:

print("\n")
print("## Problèmes de l'attribut awardEstimatedPrice: images/01_problemes_awardEstimatedPrice_02.png")
plot_proportion(
    data=awardEstimatedPrice_cat_vc,
    xcol='valeur',
    ycol='proportion',
    title='Proportion des catégories de valeurs awardEstimatedPrice',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_awardEstimatedPrice_02.png',
    logy=True
)

# # Attribut awardPrice

# In[54]:


awardPrice = lots[['awardPrice']]

# In[55]:

print("\n")
print("# Attribut awardPrice")
print(awardPrice)

# In[56]:

awardPrice_vc = get_vc(lots, column='awardPrice')

# In[57]:

print("\n")
print("## Occurrences des valeurs de l'attribut awardPrice")
print(awardPrice_vc)

# In[58]:


awardPrice_na = get_na(lots, column='awardPrice')

# In[59]:

print("\n")
print("## Problèmes de l'attribut awardPrice")
print(awardPrice_na)

# In[60]:

print("\n")
print("## Problèmes de l'attribut awardPrice: images/01_problemes_awardPrice_01.png")
plot_proportion(
    data=awardPrice_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de awardPrice',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_awardPrice_01.png',
    logy=False
)

# In[61]:


awardPrice_cat = categorized_awardPrice(awardPrice)

# In[62]:

print("\n")
print("## Catégorisation des problèmes de l'attribut awardPrice")
print(awardPrice_cat)

# In[63]:


awardPrice_cat_vc = get_vc(awardPrice_cat, column='category')

# In[64]:

print("\n")
print("## Occurrences des catégories de problèmes de l'attribut awardPrice")
print(awardPrice_cat_vc)

# In[65]:

print("\n")
print("## Problèmes de l'attribut awardDate: images/01_problemes_aawardPrice_02.png")
plot_proportion(
    data=awardPrice_cat_vc,
    xcol='valeur',
    ycol='proportion',
    title='Proportion des catégories de valeurs awardPrice',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_awardPrice_02.png',
    logy=True
)

# # Attribut cpv

# In[66]:


cpv = lots[['cpv']]

# In[67]:

print("\n")
print("# Attribut cpv")
print(cpv)

# In[68]:


cpv_vc = get_vc(lots, column='cpv')

# In[69]:

print("\n")
print("## Occurrences des valeurs de l'attribut cpv")
print(cpv_vc)

# In[70]:


cpv_na = get_na(lots, column='cpv')

# In[71]:

print("\n")
print("## Problèmes de l'attribut cpv")
print(cpv_na)

# In[72]:

print("\n")
print("## Problèmes de l'attribut awardDate: images/01_problemes_cpv_01.png")
plot_proportion(
    data=cpv_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de cpv',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_cpv_01.png',
    logy=True
)

# In[ ]:


# # Attribut numberTenders

# In[73]:


numberTenders = lots[['numberTenders']]

# In[74]:

print("\n")
print("# Attribut numberTenders")
print(numberTenders)

# In[75]:


numberTenders_vc = get_vc(lots, column='numberTenders')

# In[76]:

print("\n")
print("## Occurrences des valeurs de l'attribut numberTenders")
print(numberTenders_vc)

# In[77]:


numberTenders_na = get_na(lots, column='numberTenders')

# In[78]:

print("\n")
print("## Problèmes de l'attribut numberTenders")
print(numberTenders_na)

# In[79]:

print("\n")
print("## Problèmes de l'attribut awardDate: images/01_problemes_numberTenders_01.png")
plot_proportion(
    data=numberTenders_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de numberTenders',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_numberTenders_01.png',
    logy=False
)

# In[ ]:


# # Attribut onBehalf

# In[80]:


onBehalf = lots[['onBehalf']]

# In[81]:

print("\n")
print("# Attribut onBehalf")
print(onBehalf)

# In[82]:


onBehalf_vc = get_vc(lots, column='onBehalf')

# In[83]:

print("\n")
print("## Occurrences des valeurs de l'attribut onBehalf")
print(onBehalf_vc)

# In[84]:


onBehalf_na = get_na(lots, column='onBehalf')

# In[85]:

print("\n")
print("## Problèmes de l'attribut onBehalf")
print(onBehalf_na)

# In[86]:

print("\n")
print("## Problèmes de l'attribut awardDate: images/01_problemes_onBehalf_01.png")
plot_proportion(
    data=onBehalf_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de onBehalf',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_onBehalf_01.png',
    logy=False
)

# In[ ]:


# # Attribut jointProcurement

# In[87]:


jointProcurement = lots[['jointProcurement']]

# In[88]:

print("\n")
print("# Attribut jointProcurement")
print(jointProcurement)

# In[89]:


jointProcurement_vc = get_vc(lots, column='jointProcurement')

# In[90]:

print("\n")
print("## Occurrences des valeurs de l'attribut jointProcurement")
print(jointProcurement_vc)

# In[91]:


jointProcurement_na = get_na(lots, column='jointProcurement')

# In[92]:

print("\n")
print("## Problèmes de l'attribut jointProcurement")
print(jointProcurement_na)

# In[93]:

print("\n")
print("## Problèmes de l'attribut awardDate: images/01_problemes_jointProcurement_01.png")
plot_proportion(
    data=jointProcurement_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de jointProcurement',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_jointProcurement_01.png',
    logy=False
)

# In[ ]:


# # Attribut fraAgreement

# In[94]:


fraAgreement = lots[['fraAgreement']]

# In[95]:

print("\n")
print("# Attribut fraAgreement")
print(fraAgreement)

# In[96]:


fraAgreement_vc = get_vc(lots, column='fraAgreement')

# In[97]:

print("\n")
print("## Occurrences des valeurs de l'attribut fraAgreement")
print(fraAgreement_vc)

# In[98]:

print("\n")
fraAgreement_na = get_na(lots, column='fraAgreement')

# In[99]:

print("\n")
print("## Problèmes de l'attribut fraAgreement")
print(fraAgreement_na)

# In[ ]:


# # Attribut fraEstimated

# In[100]:


fraEstimated = lots[['fraEstimated']]

# In[101]:

print("\n")
print("# Attribut fraEstimated")
print(fraEstimated)

# In[102]:

fraEstimated_vc = get_vc(lots, column='fraEstimated')

# In[103]:

print("\n")
print("## Occurrences des valeurs de l'attribut fraEstimated")
print(fraEstimated_vc)

# In[104]:

fraEstimated_na = get_na(lots, column='fraEstimated')

# In[105]:

print("\n")
print("## Problèmes de l'attribut fraEstimated")
print(fraEstimated_na)

# In[106]:

print("\n")
print("## Problèmes de l'attribut fraEstimated: images/01_problemes_fraEstimated_01.png")
plot_proportion(
    data=fraEstimated_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de fraEstimated',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_fraEstimated_01.png',
    logy=False
)

# In[ ]:


# # Attribut lotsNumber

# In[107]:


lotsNumber = lots[['lotsNumber']]

# In[108]:

print("\n")
print("# Attribut lotsNumber")
print(lotsNumber)

# In[109]:


lotsNumber_vc = get_vc(lots, column='lotsNumber')

# In[110]:

print("\n")
print("## Occurrences des valeurs de l'attribut lotsNumber")
print(lotsNumber_vc)

# In[111]:


lotsNumber_na = get_na(lots, column='lotsNumber')

# In[112]:

print("\n")
print("## Problèmes de l'attribut lotsNumber")
print(lotsNumber_na)

# In[113]:

print("\n")
print("## Problèmes de l'attribut lotsNumber: images/01_problemes_lotsNumber_01.png")
plot_proportion(
    data=lotsNumber_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de lotsNumber',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_lotsNumber_01.png',
    logy=False
)

# In[114]:


lotsNumber_cat = categorized_lotNumber(lotsNumber)

# In[115]:

print("\n")
print("## Catégorisation des problèmes de l'attribut lotsNumber")
print(lotsNumber_cat)

# In[116]:


lotsNumber_cat_vc = get_vc(lotsNumber, column='category')

# In[117]:

print("\n")
print("## Occurrences des catégories de problèmes de l'attribut lotsNumber")
print(lotsNumber_cat_vc)

# In[118]:

print("\n")
print("## Problèmes de l'attribut lotsNumber: images/01_problemes_lotsNumber_02.png")
plot_proportion(
    data=lotsNumber_cat_vc,
    xcol='valeur',
    ycol='proportion',
    title='Proportion des catégories de valeurs lotsNumber',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_lotsNumber_02.png',
    logy=True
)

# In[ ]:


# # Attribut accelerated

# In[119]:


accelerated = lots[['accelerated']]

# In[120]:

print("\n")
print("# Attribut accelerated")
print(accelerated)

# In[121]:


accelerated_vc = get_vc(lots, column='accelerated')

# In[122]:

print("\n")
print("## Occurrences des valeurs de l'attribut accelerated")
print(accelerated_vc)

# In[123]:

accelerated_na = get_na(lots, column='accelerated')

# In[124]:

print("\n")
print("## Problèmes de l'attribut accelerated")
print(accelerated_na)

# In[125]:

print("\n")
print("## Problèmes de l'attribut accelerated: images/01_problemes_accelerated_01.png")
plot_proportion(
    data=accelerated_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de accelerated',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_accelerated_01.png',
    logy=True
)

# In[ ]:


# # Attribut outOfDirectives

# In[126]:


outOfDirectives = lots[['outOfDirectives']]

# In[127]:

print("\n")
print("# Attribut outOfDirectives")
print(outOfDirectives)

# In[128]:


outOfDirectives_vc = get_vc(lots, column='outOfDirectives')

# In[129]:

print("\n")
print("## Occurrences des valeurs de l'attribut outOfDirectives")
print(outOfDirectives_vc)

# In[130]:


outOfDirectives_na = get_na(lots, column='outOfDirectives')

# In[131]:

print("\n")
print("## Problèmes de l'attribut outOfDirectives")
print(outOfDirectives_na)

# In[ ]:


# # Attribut contractorSme

# In[132]:


contractorSme = lots[['contractorSme']]

# In[133]:

print("\n")
print("# Attribut contractorSme")
print(contractorSme)

# In[134]:


contractorSme_vc = get_vc(lots, column='contractorSme')

# In[135]:

print("\n")
print("## Occurrences des valeurs de l'attribut contractorSme")
print(contractorSme_vc)

# In[136]:


contractorSme_na = get_na(lots, column='contractorSme')

# In[137]:

print("\n")
print("## Problèmes de l'attribut contractorSme")
print(contractorSme_na)

# In[138]:

print("\n")
print("## Problèmes de l'attribut contractorSme: images/01_problemes_contractorSme_01.png")
plot_proportion(
    data=contractorSme_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de contractorSme',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_contractorSme_01.png',
    logy=True
)

# In[139]:


contractorSme_cat = categorized_contractorSme(contractorSme)

# In[140]:

print("\n")
print("## Catégorisation des problèmes de l'attribut contractorSme")
print(contractorSme_cat)

# In[141]:


contractorSme_cat_vc = get_vc(contractorSme_cat, column='category')

# In[142]:

print("\n")
print("## Occurrences des catégories de problèmes de l'attribut contractorSme")
print(contractorSme_cat_vc)

# In[143]:

print("\n")
print("## Problèmes de l'attribut contractorSme: images/01_problemes_contractorSme_02.png")
plot_proportion(
    data=contractorSme_cat_vc,
    xcol='valeur',
    ycol='proportion',
    title='Proportion des catégories de valeurs contractorSme',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_contractorSme.png',
    logy=True
)

# In[ ]:


# # Attribut numberTendersSme

# In[144]:


numberTendersSme = lots[['numberTendersSme']]

# In[145]:

print("\n")
print("# Attribut numberTendersSme")
print(numberTendersSme)

# In[146]:


numberTendersSme_vc = get_vc(lots, column='numberTendersSme')

# In[147]:

print("\n")
print("## Occurrences des valeurs de l'attribut numberTendersSme")
print(numberTendersSme_vc)

# In[148]:


numberTendersSme_na = get_na(lots, column='numberTendersSme')

# In[149]:

print("\n")
print("## Problèmes de l'attribut numberTendersSme")
print(numberTendersSme_na)

# In[150]:

print("\n")
print("## Problèmes de l'attribut awardDate: images/01_problemes_numberTendersSme_01.png")
plot_proportion(
    data=numberTendersSme_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de numberTendersSme',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_numberTendersSme_01.png',
    logy=True
)

# In[ ]:


# # Attribut subContracted

# In[151]:


subContracted = lots[['subContracted']]

# In[152]:

print("\n")
print("# Attribut subContracted")
print(subContracted)

# In[153]:


subContracted_vc = get_vc(lots, column='subContracted')

# In[154]:

print("\n")
print("## Occurrences des valeurs de l'attribut subContracted")
print(subContracted_vc)

# In[155]:


subContracted_na = get_na(lots, column='subContracted')

# In[156]:

print("\n")
print("## Problèmes de l'attribut subContracted")
print(subContracted_na)

# In[157]:

print("\n")
print("## Problèmes de l'attribut awardDate: images/01_problemes_subContracted_01.png")
plot_proportion(
    data=subContracted_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de subContracted',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_subContracted_01.png',
    logy=False
)

# In[ ]:


# # Attribut gpa

# In[158]:


gpa = lots['gpa']

# In[159]:

print("\n")
print("# Attribut gpa")
print(gpa)

# In[160]:


gpa_vc = get_vc(lots, column='gpa')

# In[161]:

print("\n")
print("## Occurrences des valeurs de l'attribut gpa")
print(gpa_vc)

# In[162]:


gpa_na = get_na(lots, column='gpa')

# In[163]:

print("\n")
print("## Problèmes de l'attribut gpa")
print(gpa_na)

# In[164]:

print("\n")
print("## Problèmes de l'attribut awardDate: images/01_problemes_gpa_01.png")
plot_proportion(
    data=gpa_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de gpa',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_gpa_01.png',
    logy=False
)

# In[ ]:


# # Attribut multipleCae

# In[165]:


multipleCae = lots[['multipleCae']]

# In[166]:

print("\n")
print("# Attribut multipleCae")
print(multipleCae)

# In[167]:


multipleCae_vc = get_vc(lots, column='multipleCae')

# In[168]:

print("\n")
print("## Occurrences des valeurs de l'attribut multipleCae")
print(multipleCae_vc)

# In[169]:


multipleCae_na = get_na(lots, column='multipleCae')

# In[170]:

print("\n")
print("## Problèmes de l'attribut multipleCae")
print(multipleCae_na)

# In[171]:

print("\n")
print("## Problèmes de l'attribut awardDate: images/01_problemes_awardDate_01.png")
plot_proportion(
    data=multipleCae_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de multipleCae',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_multipleCae_01.png',
    logy=False
)

# In[ ]:


# # Attribut typeOfContract

# In[172]:


typeOfContract = lots[['typeOfContract']]

# In[173]:

print("\n")
print("# Attribut typeOfContract")
print(typeOfContract)

# In[174]:


typeOfContract_vc = get_vc(lots, column='typeOfContract')

# In[175]:

print("\n")
print("## Occurrences des valeurs de l'attribut typeOfContract")
print(typeOfContract_vc)

# In[176]:


typeOfContract_na = get_na(lots, column='typeOfContract')

# In[177]:

print("\n")
print("## Problèmes de l'attribut typeOfContract")
print(typeOfContract_na)

# In[ ]:


# # Attribut topType

# In[178]:


topType = lots[['topType']]

# In[179]:

print("\n")
print("# Attribut topType")
print(topType)

# In[180]:

topType_vc = get_vc(lots, column='topType')

# In[181]:

print("\n")
print("## Occurrences des valeurs de l'attribut topType")
print(topType_vc)

# In[182]:


topType_na = get_na(lots, column='topType')

# In[183]:

print("\n")
print("## Problèmes de l'attribut topType")
print(topType_na)

# In[184]:

print("\n")
print("## Problèmes de l'attribut awardDate: images/01_problemes_topType_01.png")
plot_proportion(
    data=topType_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de topType',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_topType_01.png',
    logy=True
)

# # Attribut renewal

# In[185]:


renewal = lots[['renewal']]

# In[186]:

print("\n")
print("# Attribut renewal")
print(renewal)

# In[187]:

renewal_vc = get_vc(lots, column='renewal')

# In[188]:

print("\n")
print("## Occurrences des valeurs de l'attribut renewal")
print(renewal_vc)

# In[189]:


renewal_na = get_na(lots, column='renewal')

# In[190]:

print("\n")
print("## Problèmes de l'attribut renewal")
print(renewal_na)

# In[191]:

print("\n")
print("## Problèmes de l'attribut awardDate: images/01_problemes_renewal_01.png")
plot_proportion(
    data=renewal_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de renewal',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_renewal_01.png',
    logy=False
)

# In[ ]:


# # Attribut contractDuration

# In[192]:


contractDuration = lots[['contractDuration']]

# In[193]:

print("\n")
print("# Attribut contractDuration")
print(contractDuration)

# In[194]:


contractDuration_vc = get_vc(lots, column='contractDuration')

# In[195]:

print("\n")
print("## Occurrences des valeurs de l'attribut contractDuration")
print(contractDuration_vc)

# In[196]:


contractDuration_na = get_na(lots, column='contractDuration')

# In[197]:

print("\n")
print("## Problèmes de l'attribut contractDuration")
print(contractDuration_na)

# In[198]:

print("\n")
print("## Problèmes de l'attribut contractDuration: images/01_problemes_contractDuration_01.png")
plot_proportion(
    data=contractDuration_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de contractDuration',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_contractDuration_01.png',
    logy=False
)

# In[ ]:


# # Attribut publicityDuration

# In[199]:


publicityDuration = lots[['publicityDuration']]

# In[200]:

print("\n")
print("# Attribut publicityDuration")
print(publicityDuration)

# In[201]:


publicityDuration_vc = get_vc(lots, column='publicityDuration')

# In[202]:

print("\n")
print("## Occurrences des valeurs de l'attribut publicityDuration")
print(publicityDuration_vc)

# In[203]:


publicityDuration_na = get_na(lots, column='publicityDuration')

# In[204]:
print("\n")
print("## Problèmes de l'attribut publicityDuration")
print(publicityDuration_na)

# In[205]:

print("\n")
print("## Problèmes de l'attribut awardDate: images/01_problemes_publicityDuration_01.png")
plot_proportion(
    data=publicityDuration_na,
    xcol='attribut',
    ycol='proportion',
    title='Proportion des catégories de valeurs de publicityDuration',
    xtitle='catégorie de valeur',
    ytitle='proportion',
    saveas='images/01_problemes_publicityDuration_01.png',
    logy=False
)

# In[ ]:
