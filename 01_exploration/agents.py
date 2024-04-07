# %%
from functions.utils_lots import *
import warnings

warnings.filterwarnings('ignore')

# %% [markdown]
# ### Les attributs

# %%
agents = load_data(path='./donnees/agents.csv')

# %%
print("\n# Aperçu des Données Chargées")
print(agents)

# %%
agents_dtypes = get_dtypes(agents)

# %%
print("\n# Types de Données des Colonnes")
print(agents_dtypes)

# %% [markdown]
# ### Attribut agentId

# %%
print("\n# Attribut `agentId`")
agentsId = agents[['agentId']]

# %%
print(agentsId)
# %%
print("\n# Comptage des Valeurs `agentId`")
agentId_vc = get_vc(agents, column='agentId')

# %%
print(agentId_vc)
# %%
print("\n# Valeurs Manquantes pour `agentId`")
agentId_na = get_na(agents, column='agentId')

# %%
print(agentId_na)
# %% [markdown]
# ### attribut name

# Extraction de la colonne `name`
names = agents[['name']]
print("\n# Attribut `name`")
print(names)

# Comptage des valeurs uniques pour `name`
name_vc = get_vc(agents, column='name')
print("\n# Comptage des Valeurs pour `name`")
print(name_vc)

# Analyse des valeurs manquantes pour `name`
name_na = get_na(agents, column='name')
print("\n# Valeurs Manquantes pour `name`")
print(name_na)


# Extraction de la colonne `siret`
sirets = agents[['siret']]
print("\n# Attribut `siret`")
print(sirets)

# Comptage des valeurs uniques pour `siret`
siret_vc = get_vc(agents, column='siret')
print("\n# Comptage des Valeurs pour `siret`")
print(siret_vc)

# Analyse des valeurs manquantes pour `siret`
siret_na = get_na(agents, column='siret')
print("\n# Valeurs Manquantes pour `siret`")
print(siret_na)

# %%
print("## Problèmes de l'attribut siret: images/01_problemes_siret.png'")

plot_proportion(
    data=siret_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des identifiant siret', 
    xtitle='siret', 
    ytitle='proportion',
    saveas='../images/01_problemes_siret.png',

    logy=False
)

# %% [markdown]
# ### attribut adress

# %%
adress = agents[['address']]
print("\n# Aperçu des adresses")
print(adress)

# Comptage des valeurs uniques pour `address`
address_vc = get_vc(agents, column='address')
print("\n# Comptage des Valeurs Uniques pour `address`")
print(address_vc)

# Analyse des valeurs manquantes pour `address`
address_na = get_na(agents, column='address')
print("\n# Valeurs Manquantes pour `address`")
print(address_na)
# %%
print("## Problèmes de l'attribut address: images/01_problemes_adress.png'")

plot_proportion(
    data=address_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des adresses', 
    xtitle='adresse', 
    ytitle='proportion',
    saveas='../images/01_problemes_adress.png',

    logy=False
)

# %%


# %% [markdown]
# ### attribut city
city = agents[['city']]
print("\n# Aperçu des villes")
print(city)

# Comptage des valeurs uniques pour `city`
city_vc = get_vc(agents, column='city')
print("\n# Comptage des Valeurs Uniques pour `city`")
print(city_vc)

# Analyse des valeurs manquantes pour `city`
city_na = get_na(agents, column='city')
print("\n# Valeurs Manquantes pour `city`")
print(city_na)

# %%
print("## Problèmes de l'attribut address: images/01_problemes_city.png'")

plot_proportion(
    data=city_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des valeurs city', 
    xtitle='city', 
    ytitle='proportion',
    saveas='../images/01_problemes_city.png',

    logy=False
)

# %% [markdown]
# ### attribut zipcode
zipcode = agents[['zipcode']]
print("\n# Aperçu des codes postaux")
print(zipcode)

# Comptage des valeurs uniques pour `zipcode`
zipcode_vc = get_vc(agents, column='zipcode')
print("\n# Comptage des Valeurs Uniques pour `zipcode`")
print(zipcode_vc)

# Analyse des valeurs manquantes pour `zipcode`
zipcode_na = get_na(agents, column='zipcode')
print("\n# Valeurs Manquantes pour `zipcode`")
print(zipcode_na)

# %%
print("## Problèmes de l'attribut address: images/01_problemes_zipcode.png'")

plot_proportion(
    data=city_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des valeurs zipcode', 
    xtitle='zipcode', 
    ytitle='proportion',
    saveas='../images/01_problemes_zipcode.png',

    logy=False
)

# %% [markdown]
# ### attribut coutry
country = agents[['country']]
print("\n# Aperçu des pays")
print(country)

# Comptage des valeurs uniques pour `country`
country_vc = get_vc(agents, column='country')
print("\n# Comptage des Valeurs Uniques pour `country`")
print(country_vc)

# Analyse des valeurs manquantes pour `country`
country_na = get_na(agents, column='country')
print("\n# Valeurs Manquantes pour `country`")
print(country_na)

# %%
print("## Problèmes de l'attribut address: images/01_problemes_country.png'")

plot_proportion(
    data=city_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des valeurs country', 
    xtitle='country', 
    ytitle='proportion',
    saveas='../images/01_problemes_country.png',

    logy=False
)

# %% [markdown]
# ### attribut department
department = agents[['department']]
print("\n# Aperçu des départements")
print(department)

# Comptage des valeurs uniques pour `department`
department_vc = get_vc(agents, column='department')
print("\n# Comptage des Valeurs Uniques pour `department`")
print(department_vc)

# Analyse des valeurs manquantes pour `department`
department_na = get_na(agents, column='department')
print("\n# Valeurs Manquantes pour `department`")
print(department_na)

# %%
print("## Problèmes de l'attribut address: images/01_problemes_departement.png'")

plot_proportion(
    data=department_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des valeurs departement', 
    xtitle='departement', 
    ytitle='proportion',
    saveas='../images/01_problemes_departement.png',

    logy=False
)

# %% [markdown]
# ### attribut longitude
longitude = agents[['longitude']]
print("\n# Aperçu des longitudes")
print(longitude)

# Comptage des valeurs uniques pour `longitude`
longitude_vc = get_vc(agents, column='longitude')
print("\n# Comptage des Valeurs Uniques pour `longitude`")
print(longitude_vc)

# Analyse des valeurs manquantes pour `longitude`
longitude_na = get_na(agents, column='longitude')
print("\n# Valeurs Manquantes pour `longitude`")
print(longitude_na)




# %%
print("## Problèmes de l'attribut address: images/01_problemes_longitude.png'")

plot_proportion(
    data=longitude_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des valeurs longtitude', 
    xtitle='longitude', 
    ytitle='proportion',
    saveas='../images/01_problemes_longitude.png',

    logy=False
)

# %%


# %% [markdown]
# ### attribuit latitude
latitude = agents[['latitude']]
print("\n# Aperçu des latitudes")
print(latitude)

# Comptage des valeurs uniques pour `latitude`
latitude_vc = get_vc(agents, column='latitude')
print("\n# Comptage des Valeurs Uniques pour `latitude`")
print(latitude_vc)

# Analyse des valeurs manquantes pour `latitude`
latitude_na = get_na(agents, column='latitude')
print("\n# Valeurs Manquantes pour `latitude`")
print(latitude_na)

# %%
print("## Problèmes de l'attribut address: images/01_problemes_longitude.png'")

plot_proportion(
    data=longitude_na,
    xcol='attribut', 
    ycol='proportion', 
    title='Proportion des valeurs latitude', 
    xtitle='latitude', 
    ytitle='proportion',
    saveas='../images/01_problemes_latitude.png',

    logy=False
)


