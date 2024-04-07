# %%
from functions.utils_agents import *
import warnings

warnings.filterwarnings('ignore')

# %% [markdown]
# ### On va exploiter la base sirene pour ajouter d'autres attributs à la table agents pour voir si ça va influencer sur la formation des clusters en faisant un comparaison entre les clusters qu'on a dans lla partie Questionnement  pour les agents

# %%
sirene = load_data(path='../donnees/siret_extended.csv')

# %%
print("\n# Aperçu des données chargées de SIRENE")
print(sirene.head())


# %%
print("\n# Types de données dans le dataframe SIRENE")
print(sirene.dtypes)

# %% [markdown]
# ### Chargement des clusters d'agents sans données SIRENE
# Ici, nous chargeons les données des clusters préalablement formés pour les agents, sans intégrer les informations supplémentaires de la base SIRENE. Cela nous permet d'effectuer une comparaison avant et après l'enrichissement des données.

# %%
clustersWithoutSirene = load_data('../donnees/agents_cleaned_clusters.csv')
print("\n# Aperçu initial des clusters sans données SIRENE")
print(clustersWithoutSirene.head())

# %% [markdown]
# ### Nettoyage des clusters
# Nous retirons la colonne 'cluster' des données pour préparer les clusters à être enrichis avec des informations supplémentaires de la base SIRENE. Cela nous permet de repartir d'une base neutre pour l'enrichissement.

# %%
clustersWithoutSirene = clustersWithoutSirene.drop('cluster', axis=1, errors='ignore')
print("\n# Aperçu des données après suppression de la colonne 'cluster'")
print(clustersWithoutSirene.head())

# %% [markdown]
# ### Fusion avec les données SIRENE
# Ensuite, nous enrichissons les clusters d'agents en fusionnant avec des informations sélectionnées de la base SIRENE (siret,


# %%
# %% [markdown]
# ### Fusion avec les données SIRENE
# Nous fusionnons les clusters d'agents avec des informations sélectionnées de la base SIRENE. Cette étape permet d'enrichir nos données avec des informations pertinentes pour une analyse plus approfondie.

# %%
clusterSirene = clustersWithoutSirene.merge(sirene[['siret', 'trancheEffectifsEtablissement', 'categorieEntreprise']], how='left', on='siret')
print("\n# Aperçu des clusters après fusion avec les données SIRENE")
print(clusterSirene.head())

# %% [markdown]
# ### Nettoyage des données enrichies
# Nous procédons au nettoyage des données enrichies pour s'assurer de la cohérence et de la précision des informations sur les tranches d'effectifs et les catégories d'entreprise.

# %%
tranchEffectif = clean_tranchEffectif_based_on_categorieEntreprise(clusterSirene)
print("\n# Aperçu des tranches d'effectifs nettoyées")
print(tranchEffectif.head())

clusterSirene = replace_original_with_cleaned(
    original=clusterSirene.copy(), 
    column='trancheEffectifsEtablissement', 
    cleaned=tranchEffectif['cleaned_trancheEffectifsEtablissement'].values, 
    path='../donnees/agents_sirene_cleaned.csv'
)
print("\n# Aperçu des clusters après nettoyage des tranches d'effectifs")
print(clusterSirene.head())

categorie = clean_categorieEntreprise_based_on_tranchEffectif(clusterSirene)
print("\n# Aperçu des catégories d'entreprise nettoyées")
print(categorie.head())

clusterSirene = replace_original_with_cleaned(
    original=clusterSirene.copy(), 
    column='categorieEntreprise', 
    cleaned=categorie['cleaned_categorieEntreprise'].values, 
    path='../donnees/agents_sirene_cleaned.csv'
)
print("\n# Aperçu des clusters après nettoyage des catégories d'entreprise")
print(clusterSirene.head())

# %% [markdown]
# ### Sélection des colonnes pour le clustering
# Identification et préparation des colonnes numériques et catégorielles à utiliser pour le clustering. Cela inclut l'exclusion de certaines colonnes spécifiques pour affiner notre analyse.

# %%
numeric_columns = get_dtypes_columns(clusters_sirene, dtypes=['number'], to_remove=['agentId'])
print("\n# Colonnes numériques sélectionnées initialement")
print(numeric_columns)

numeric_columns.pop(0)  # Suppression de la première colonne numérique, si nécessaire
print("\n# Colonnes numériques après ajustement")
print(numeric_columns)

categorical_columns = get_dtypes_columns(clusters_sirene, dtypes=['object'], to_remove=['name'])
print("\n# Colonnes catégorielles sélectionnées")
print(categorical_columns)

# %% [markdown]
# ### Détermination du nombre optimal de clusters (k)
# Utilisation de la méthode k-means sur une plage de valeurs de k pour identifier le nombre optimal de clusters à utiliser pour notre analyse.

# %%
best_k = run_multiple_kmeans(
    data=clusters_sirene, 
    numeric_columns=numeric_columns, 
    categorical_columns=categorical_columns,
    end=20,
    saveas='../images/05_extension_agents_01.png'
)
print("\n# Nombre optimal de clusters (k)")
print(best_k)

# %% [markdown]
# ### Application de l'algorithme K-Means
# Avec le nombre optimal de clusters identifié, nous appliquons l'algorithme K-Means pour segmenter nos données.

# %%
clusters_1, inertia_1 = do_kmeans(
    data=clusterSirene, 
    numeric_columns=numeric_columns, 
    categorical_columns=categorical_columns,
    k=best_k
)
save_data(clusters_1, path='../donnees/agents_sirene_clusters.csv')
clusters_1 = load_data('../donnees/agents_sirene_clusters.csv')
print("\n# Aperçu des données après clustering")
print(clusters_1.head())

# %% [markdown]
# ### Analyse des résultats du clustering
# Nous effectuons différentes analyses sur les clusters obtenus, y compris la visualisation des proportions de clusters, l'analyse des pays et villes par cluster, et l'examen des corrélations.

# Analyse des proportions de clusters
cluster_1_gb = get_gb_count(clusters_1, by_col='cluster')
plot_proportion(
    data=cluster_1_gb, 
    xcol='cluster', 
    ycol='proportion',
    title='Proportion des agents par cluster',
    xtitle='cluster',
    ytitle='proportion',
    logy=True
)

# %% [markdown]
# ### Visualisation de la proportion des agents par cluster
# Nous visualisons la répartition des agents parmi les différents clusters pour mieux comprendre la segmentation réalisée par l'algorithme de clustering.

# %%
plot_proportion(
    data=cluster_1_gb, 
    xcol='cluster', 
    ycol='proportion',
    title='Proportion des agents par cluster',
    xtitle='cluster',
    ytitle='proportion',
    logy=True
)

# %% [markdown]
# ### Calcul de la moyenne et du mode pour chaque cluster
# Pour chaque cluster, nous calculons la moyenne pour les attributs numériques et le mode pour les attributs catégoriels. Cela nous aide à caractériser chaque cluster en termes de propriétés statistiques.

# %%
get_moyenne_mode(
    data=clusters_1,
    numeric_features=numeric_columns,
    categorical_features=categorical_columns,
    k_best=best_k
)

# %% [markdown]
# ### Analyse de la distribution des pays par cluster
# Nous examinons la distribution des pays au sein de chaque cluster. Cela permet de déterminer si certains clusters sont plus représentatifs de certaines régions géographiques que d'autres.

# %%
gb_pays = grouby_by_values(
    data=clusters_1,
    by=['cluster', 'country_group'],
    column='country',
    threshold=500,
)
plot_categorial_categorical(
    data=gb_pays,
    title="Distribution des pays par cluster",
    xlabel="cluster",
    ylabel="country",
    logy=True,
    saveas='../images/05_extension_agents_01_clusterbycountry.png'
)

# %% [markdown]
# ### Analyse de la distribution des villes par cluster
# De manière similaire à l'analyse des pays, nous étudions la distribution des villes au sein des clusters pour identifier d'éventuelles concentrations géographiques spécifiques à certains clusters.

# %%
gb_city = grouby_by_values(
    data=clusters_1,
    by=['cluster', 'city_group'],
    column='city',
    threshold=1800
)
plot_categorial_categorical(
    data=gb_city,
    title="Distribution des villes par cluster",
    xlabel="cluster",
    ylabel="city",
    logy=True,
    saveas='../images/05_extension_agents_01_clusterbycity.png'
)

# %% [markdown]
# ### Analyse des corrélations catégorielles et numériques par cluster
# Nous explorons les corrélations entre les variables catégorielles et numériques au sein de chaque cluster. Cela permet d'identifier les attributs les plus influents dans la formation des clusters.

# %%
cluster_1_corr_cat, cluster_1_corr_num = get_all_corr_cat(
    data=clusters_1, 
    col='cluster', 
    num_cols=numeric_columns, 
    cat_cols=categorical_columns
)
print("\n# Corrélations catégorielles par cluster")
print(cluster_1_corr_cat.sort_values(by='cluster', ascending=False))
print("\n# Corrélations numériques par cluster")
print(cluster_1_corr_num)




