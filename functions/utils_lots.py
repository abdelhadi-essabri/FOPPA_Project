import os
import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import IsolationForest
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from tqdm import tqdm
from scipy.stats import f_oneway, chi2_contingency
import seaborn as sns
import lime
import lime.lime_tabular


# EXPLORATION
def load_data(path):
    """
    Function permettant de charger les données
    :param path:
    :return:
    """
    return pd.read_csv(path, sep=',')


def save_data(df, path):
    """
    Function permettant de sauvegarder les données
    :param df:
    :param path:
    :return:
    """
    df.to_csv(path, index=False)


def get_dtypes(df):
    """
    Function permettant d'afficher les types des colonnes sous formes de dataframe
    :param df:
    :return:
    """
    return pd.DataFrame({'attribut': df.dtypes.index, 'type': df.dtypes.values})


def get_vc(df, column):
    """
    Fonction pour retourner la nombre d'élément par valeur sous forme de dataframe
    :param column:
    :param df:
    :return:
    """
    vc = df[column].value_counts()
    vc_df = pd.DataFrame({'valeur': vc.index, 'count': vc.values})
    vc_df['proportion'] = (vc_df['count'] / vc_df['count'].sum()) * 100
    return vc_df


def get_na(df, column):
    """
    Fonction pour retourner les valeurs manquantes sous formes de dataframe
    :param column:
    :param df: dataframe contenant les données
    :return:
    """
    data = {
        'attribut': ['manque', 'exist'],
        'count': [df[column].isna().sum(), df[column].notna().sum()]
    }
    data_df = pd.DataFrame(data)
    data_df['proportion'] = (data_df['count'] / data_df['count'].sum()) * 100
    return data_df


def plot_proportion(data, xcol, ycol, title, xtitle, ytitle, saveas, logy=True, xrot=0):
    """
    Permet de representer les proportions de catégories de données
    :param xrot:
    :param saveto:
    :param data:
    :param xcol:
    :param ycol:
    :param title:
    :param xtitle:
    :param ytitle:
    :param logy:
    :return:
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.xticks(fontsize=6)

    X = data[xcol].values.astype(str)
    y = data[ycol].values

    # Utiliser une colormap pour les couleurs des barres
    # Assurez-vous que les valeurs y sont normalisées pour la colormap
    norm = mcolors.Normalize(vmin=y.min(), vmax=y.max())
    mapper = cm.ScalarMappable(norm=norm, cmap='viridis')
    colors = mapper.to_rgba(y)

    # Ajouter une barre de couleur (légende) pour indiquer les valeurs
    cbar = fig.colorbar(mapper, ax=ax)
    cbar.set_label('Couleurs')

    ax.bar(X, y, color=colors)
    plt.xticks(rotation=xrot)
    if logy:
        ax.set_yscale('log')
    ax.set_title(title)
    ax.set_xlabel(xtitle)
    ax.set_ylabel(ytitle)

    folder = os.path.dirname(saveas)
    os.makedirs(folder, exist_ok=True)
    plt.savefig(saveas)


def get_awardDate_cat(value):
    """
    Methode pour calculer la class d'une valeur de awardDate
    :param value:
    :return:
    """
    if isinstance(value, (float, int)) and np.isnan(value):
        return 'missing'
    elif value < 2010:
        return '< 2010'
    elif value > 2020:
        return '> 2020'
    else:
        return '[2010-2020]'


def categorized_awardDate(df):
    """
    Permet de catégoriser les valeurs de l'attribut awardDate
    :param df:
    :return:
    """
    df['awardDate'] = pd.to_datetime(df['awardDate'])
    df['year'] = df['awardDate'].dt.year
    df['category'] = df['year'].apply(get_awardDate_cat)
    return df


def get_awardEstimatedPrice_cat(value):
    """
    Methode pour calculer la class d'une valeur de awardEstimatedPrice
    :param value:
    :return:
    """
    pattern = r'^(\d)\1{3,}$'
    if isinstance(value, (float, int)) and np.isnan(value):
        return 'missing'
    elif value <= 1:
        return '≤ 1'
    elif re.match(pattern, str(int(value))):
        return 'repetition'
    else:
        return 'correct'


def categorized_awardEstimatedPrice(df):
    """
    Permet de catégoriser les valeurs de l'attribut awardEstimatedPrice
    :param df:
    :return:
    """
    df['category'] = df['awardEstimatedPrice'].apply(get_awardEstimatedPrice_cat)
    return df


def get_awardPrice_cat(value):
    """
    Methode pour calculer la class d'une valeur de awardPrice
    :param value:
    :return:
    """
    pattern = r'^(\d)\1{3,}$'
    if isinstance(value, (float, int)) and np.isnan(value):
        return 'missing'
    elif value <= 1:
        return '≤ 1'
    elif re.match(pattern, str(int(value))):
        return 'repetition'
    else:
        return 'correct'


def categorized_awardPrice(df):
    """
    Permet de catégoriser les valeurs de l'attribut awardPrice
    :param df:
    :return:
    """
    df['category'] = df['awardPrice'].apply(get_awardPrice_cat)
    return df


def get_lotNumber_cat(value):
    """
    Méthode pour calculer la classe d'une valeur de lotsNumber
    :param value: La valeur à évaluer
    :return: La classe de la valeur
    """
    if str(value).isdigit():
        return 'correct'
    elif isinstance(value, (float, int)) and np.isnan(value):
        return 'missing'
    else:
        return 'not numeric'


def categorized_lotNumber(df):
    """
    Permet de catégoriser les valeurs de l'attribut lotsNumber
    :param df:
    :return:
    """
    df['category'] = df['lotsNumber'].apply(get_lotNumber_cat)
    return df


def get_contractorSme_cat(value):
    """
    Méthode pour calculer la classe d'une valeur de contractorSme
    :param value: La valeur à évaluer
    :return: La classe de la valeur
    """
    if isinstance(value, (float, int)) and np.isnan(value):
        return 'missing'
    elif value not in ['Y', 'N']:
        return 'repetition'
    else:
        return 'correct'


def categorized_contractorSme(df):
    """
    Permet de catégoriser les valeurs de l'attribut contractorSme
    :param df:
    :return:
    """
    df['category'] = df['contractorSme'].apply(get_contractorSme_cat)
    return df


# NETTOYAGE

def replace_awardDate(stats, value):
    """
    Methode pour remplacer les valeurs problématiques  de awardDate
    :param stats:
    :param value:
    :return:
    """
    mode = stats['mode']
    year = value.year
    if isinstance(year, (float, int)) and np.isnan(year):
        return mode
    elif year < 2010:
        return value
    elif year > 2020:
        return value
    else:
        return value


def clean_awardDate(df):
    """
    Permet de nettoyer l'attribut awardDate
    :param df:
    :return:
    """
    df['awardDate'] = pd.to_datetime(df['awardDate'])
    stats = {
        'mode': df['awardDate'].mode()[0]
    }
    df['cleaned'] = df['awardDate'].apply(lambda x: replace_awardDate(stats, x))
    return df


def replace_awardEstimatedPrice(stats, value):
    """
    Methode pour remplacer les valeurs de awardEstimatedPrice
    :param stats:
    :param value:
    :return:
    """
    pattern = r'^(\d)\1{3,}$'
    median = stats['median']
    if isinstance(value, (float, int)) and np.isnan(value):
        return median
    elif value <= 1:
        return value
    elif re.match(pattern, str(int(value))):
        return value
    else:
        return value


def clean_awardEstimatedPrice(df):
    """
    Permet de nettoyer l'attribut awardEstimatedPrice
    :param df:
    :return:
    """
    stats = {
        'median': df['awardEstimatedPrice'].median()
    }
    df['cleaned'] = df['awardEstimatedPrice'].apply(lambda x: replace_awardEstimatedPrice(stats, x))
    return df


def replace_awardPrice(stats, value):
    """
    Methode pour remplacer les valeurs de awardPrice
    :param stats:
    :param value:
    :return:
    """
    pattern = r'^(\d)\1{3,}$'
    median = stats['median']
    if isinstance(value, (float, int)) and np.isnan(value):
        return median
    elif value <= 1:
        return value
    elif re.match(pattern, str(int(value))):
        return value
    else:
        return value


def clean_awardPrice(df):
    """
    Permet de nettoyer l'attribut awardPrice
    :param df:
    :return:
    """
    stats = {
        'median': df['awardPrice'].median()
    }
    df['cleaned'] = df['awardPrice'].apply(lambda x: replace_awardPrice(stats, x))
    return df


def replace_cpv(stats, value):
    """
    Methode pour remplacer les valeurs de cpv
    :param stats:
    :param value:
    :return:
    """
    mode = stats['mode']
    if isinstance(value, (float, int)) and np.isnan(value):
        return mode
    else:
        return value


def clean_cpv(df):
    """
    Permet de nettoyer l'attribut cpv
    :param df:
    :return:
    """
    stats = {
        'mode': df['cpv'].mode()[0]
    }
    df['cleaned'] = df['cpv'].apply(lambda x: replace_cpv(stats, x))
    return df


def replace_numberTenders(stats, value):
    """
    Methode pour les valeurs de numberTenders
    :param stats:
    :param value:
    :return:
    """
    mode = stats['mode']
    if isinstance(value, (float, int)) and np.isnan(value):
        return mode
    else:
        return value


def clean_numberTenders(df):
    """
    Permet de nettoyer l'attribut numberTenders
    :param df:
    :return:
    """
    stats = {
        'mode': df['numberTenders'].mode()[0]
    }
    df['cleaned'] = df['numberTenders'].apply(lambda x: replace_numberTenders(stats, x))
    return df


def replace_onBehalf(stats, value):
    """
    Methode pour les valeurs de onBehalf
    :param stats:
    :param value:
    :return:
    """
    mode = stats['mode']
    if isinstance(value, (float, int)) and np.isnan(value):
        return mode
    else:
        return value


def clean_onBehalf(df):
    """
    Permet de nettoyer l'attribut onBehalf
    :param df:
    :return:
    """
    stats = {
        'mode': df['onBehalf'].mode()[0]
    }
    df['cleaned'] = df['onBehalf'].apply(lambda x: replace_onBehalf(stats, x))
    return df


def replace_jointProcurement(stats, value):
    """
    Methode pour les valeurs de jointProcurement
    :param stats:
    :param value:
    :return:
    """
    mode = stats['mode']
    if isinstance(value, (float, int)) and np.isnan(value):
        return mode
    else:
        return value


def clean_jointProcurement(df):
    """
    Permet de nettoyer l'attribut jointProcurement
    :param df:
    :return:
    """
    stats = {
        'mode': df['jointProcurement'].mode()[0]
    }
    df['cleaned'] = df['jointProcurement'].apply(lambda x: replace_jointProcurement(stats, x))
    return df


def replace_fraEstimated(stats, value):
    """
    Methode pour les valeurs de fraEstimated
    :param stats:
    :param value:
    :return:
    """
    mode = stats['mode']
    if isinstance(value, (float, int)) and np.isnan(value):
        return mode
    else:
        return value


def clean_fraEstimated(df):
    """
    Permet de nettoyer l'attribut fraEstimated
    :param df:
    :return:
    """
    stats = {
        'mode': df['fraEstimated'].mode()[0]
    }
    df['cleaned'] = df['fraEstimated'].apply(lambda x: replace_fraEstimated(stats, x))
    return df


def replace_lotsNumber(stats, value):
    """
    Methode pour les valeurs de lotsNumber
    :param stats:
    :param value:
    :return:
    """
    mode = stats['mode']
    if str(value).isdigit():
        return value
    elif isinstance(value, (float, int)) and np.isnan(value):
        return mode
    else:
        return mode


def clean_lotsNumber(df):
    """
    Permet de nettoyer l'attribut lotsNumber
    :param df:
    :return:
    """
    stats = {
        'mode': df['lotsNumber'].mode()[0]
    }
    df['cleaned'] = df['lotsNumber'].apply(lambda x: replace_lotsNumber(stats, x))
    return df


def replace_accelerated(stats, value):
    """
    Methode pour les valeurs de accelerated
    :param stats:
    :param value:
    :return:
    """
    x = stats['x']
    if isinstance(value, (float, int)) and np.isnan(value):
        return x
    else:
        return value


def clean_accelerated(df):
    """
    Permet de nettoyer l'attribut accelerated
    :param df:
    :return:
    """
    stats = {
        'x': 'N'
    }
    df['cleaned'] = df['accelerated'].apply(lambda x: replace_accelerated(stats, x))
    return df


def replace_contractorSme(stats, value):
    """
    Méthode de remplacer les valeurs de contractorSme
    :param stats:
    :param value: La valeur à évaluer
    :return: La classe de la valeur
    """
    mode = stats['mode']
    if isinstance(value, (float, int)) and np.isnan(value):
        return mode
    elif value not in ['Y', 'N']:
        return mode
    else:
        return value


def clean_contractorSme(df):
    """
    Permet de nettoyer l'attribut contractorSme
    :param df:
    :return:
    """
    stats = {
        'mode': df['contractorSme'].mode()[0]
    }
    df['cleaned'] = df['contractorSme'].apply(lambda x: replace_contractorSme(stats, x))
    return df


def replace_numberTendersSme(stats, value):
    """
    Methode pour les valeurs de numberTendersSme
    :param stats:
    :param value:
    :return:
    """
    mode = stats['mode']
    if isinstance(value, (float, int)) and np.isnan(value):
        return mode
    else:
        return value


def clean_numberTendersSme(df):
    """
    Permet de nettoyer l'attribut numberTendersSme
    :param df:
    :return:
    """
    stats = {
        'mode': df['numberTendersSme'].mode()[0]
    }
    df['cleaned'] = df['numberTendersSme'].apply(lambda x: replace_numberTendersSme(stats, x))
    return df


def replace_subContracted(stats, value):
    """
    Methode pour les valeurs de subContracted
    :param stats:
    :param value:
    :return:
    """
    mode = stats['mode']
    if isinstance(value, (float, int)) and np.isnan(value):
        return mode
    else:
        return value


def clean_subContracted(df):
    """
    Permet de nettoyer l'attribut subContracted
    :param df:
    :return:
    """
    stats = {
        'mode': df['subContracted'].mode()[0]
    }
    df['cleaned'] = df['subContracted'].apply(lambda x: replace_subContracted(stats, x))
    return df


def replace_gpa(stats, value):
    """
    Methode pour les valeurs de gpa
    :param stats:
    :param value:
    :return:
    """
    mode = stats['mode']
    if isinstance(value, (float, int)) and np.isnan(value):
        return mode
    else:
        return value


def clean_gpa(df):
    """
    Permet de nettoyer l'attribut gpa
    :param df:
    :return:
    """
    stats = {
        'mode': df['gpa'].mode()[0]
    }
    df['cleaned'] = df['gpa'].apply(lambda x: replace_gpa(stats, x))
    return df


def replace_multipleCae(stats, value):
    """
    Methode pour les valeurs de multipleCae
    :param stats:
    :param value:
    :return:
    """
    mode = stats['mode']
    if isinstance(value, (float, int)) and np.isnan(value):
        return mode
    else:
        return value


def clean_multipleCae(df):
    """
    Permet de nettoyer l'attribut multipleCae
    :param df:
    :return:
    """
    stats = {
        'mode': df['multipleCae'].mode()[0]
    }
    df['cleaned'] = df['multipleCae'].apply(lambda x: replace_multipleCae(stats, x))
    return df


def replace_topType(stats, value):
    """
    Methode pour les valeurs de topType
    :param stats:
    :param value:
    :return:
    """
    mode = stats['mode']
    if isinstance(value, (float, int)) and np.isnan(value):
        return mode
    else:
        return value


def clean_topType(df):
    """
    Permet de nettoyer l'attribut topType
    :param df:
    :return:
    """
    stats = {
        'mode': df['topType'].mode()[0]
    }
    df['cleaned'] = df['topType'].apply(lambda x: replace_topType(stats, x))
    return df


def replace_renewal(stats, value):
    """
    Methode pour les valeurs de renewal
    :param stats:
    :param value:
    :return:
    """
    mode = stats['mode']
    if isinstance(value, (float, int)) and np.isnan(value):
        return mode
    else:
        return value


def clean_renewal(df):
    """
    Permet de nettoyer l'attribut renewal
    :param df:
    :return:
    """
    stats = {
        'mode': df['renewal'].mode()[0]
    }
    df['cleaned'] = df['renewal'].apply(lambda x: replace_renewal(stats, x))
    return df


def replace_contractDuration(stats, value):
    """
    Methode pour les valeurs de contractDuration
    :param stats:
    :param value:
    :return:
    """
    median = stats['median']
    if isinstance(value, (float, int)) and np.isnan(value):
        return median
    else:
        return value


def clean_contractDuration(df):
    """
    Permet de nettoyer l'attribut contractDuration
    :param df:
    :return:
    """
    stats = {
        'median': df['contractDuration'].median()
    }
    df['cleaned'] = df['contractDuration'].apply(lambda x: replace_contractDuration(stats, x))
    return df


def replace_contractDuration(stats, value):
    """
    Methode pour les valeurs de contractDuration
    :param stats:
    :param value:
    :return:
    """
    median = stats['median']
    if isinstance(value, (float, int)) and np.isnan(value):
        return median
    else:
        return value


def clean_contractDuration(df):
    """
    Permet de nettoyer l'attribut contractDuration
    :param df:
    :return:
    """
    stats = {
        'median': df['contractDuration'].median()
    }
    df['cleaned'] = df['contractDuration'].apply(lambda x: replace_contractDuration(stats, x))
    return df


def replace_publicityDuration(stats, value):
    """
    Methode pour les valeurs de publicityDuration
    :param stats:
    :param value:
    :return:
    """
    median = stats['median']
    if isinstance(value, (float, int)) and np.isnan(value):
        return median
    else:
        return value


def clean_publicityDuration(df):
    """
    Permet de nettoyer l'attribut publicityDuration
    :param df:
    :return:
    """
    stats = {
        'median': df['publicityDuration'].median()
    }
    df['cleaned'] = df['publicityDuration'].apply(lambda x: replace_publicityDuration(stats, x))
    return df


def replace_original_with_cleaned(original, column, cleaned, path):
    """
    Pour remplacer une colonne original par une nettoyée
    :param original:
    :param column:
    :param cleaned:
    :param path:
    :return:
    """
    original[column] = cleaned
    original.to_csv(path, index=False)
    return original


# Analyse Descriptive séparemment
def discretize_values(df, column, bins, labels, include_lowest=True):
    """
    Permet de discrétiser des valeurs
    :param df:
    :param column:
    :param bins:
    :param labels:
    :param include_lowest:
    :return:
    """
    df['category'] = pd.cut(
        df[column],
        bins=bins,
        labels=labels,
        include_lowest=include_lowest
    )
    return df


# Statistiques descriptives
def get_awardDate_info(df):
    df['awardDate'] = pd.to_datetime(df['awardDate'])
    df['year'] = df['awardDate'].dt.year
    df['month'] = df['awardDate'].dt.month
    return df


def awardDate_evolution(df, start, end, saveas):
    data = df[(df['year'] >= start) & (df['year'] <= end)]
    group_by_year_month = data.groupby(['year', 'month']).size()
    group_by_year_month = group_by_year_month.reset_index(name='count')
    group_by_year_month = group_by_year_month.sort_values(by=['year', 'month'])

    # Tracer une courbe pour chaque année
    for year in group_by_year_month['year'].unique():
        subset = group_by_year_month[group_by_year_month['year'] == year]
        plt.plot(subset['month'], subset['count'], marker='', label=int(year))

    # Ajouter des légendes et des titres
    plt.legend(title='Année')
    plt.title("Evolution de l'attributions des lots par mois pour chaque année")
    plt.xlabel('Mois')
    plt.ylabel('Nombre de lots')
    plt.xticks(range(1, 13))
    plt.grid(True)

    folder = os.path.dirname(saveas)
    os.makedirs(folder, exist_ok=True)
    plt.savefig(saveas)


def plot_categorial_categorical(
        data,
        title,
        xlabel,
        ylabel,
        saveas,
        logy=True
):
    data.plot(kind='bar', stacked=False)
    # Adding titles and labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if logy:
        plt.yscale('log')
    folder = os.path.dirname(saveas)
    os.makedirs(folder, exist_ok=True)
    plt.savefig(saveas)


def plot_categorial_numerical(
        data,
        title,
        xlabel,
        ylabel,
        saveas,
        logy=True
):
    sns.violinplot(data=data, x=xlabel, y=ylabel)
    # Adding titles and labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if logy:
        plt.yscale('log')
    folder = os.path.dirname(saveas)
    os.makedirs(folder, exist_ok=True)
    plt.savefig(saveas)


def plot_numerical_numerical(
        data,
        title,
        xlabel,
        ylabel,
        saveas,
        logy=True
):
    sns.scatterplot(data=data, x=xlabel, y=ylabel)
    # Adding titles and labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if logy:
        plt.yscale('log')
    folder = os.path.dirname(saveas)
    os.makedirs(folder, exist_ok=True)
    plt.savefig(saveas)


def get_corr_cat_to_cat(data, cat_column_1, cat_column_2):
    """
    Coefficient de corrélation de cramer entre 2 variables catégorielles
    :param data:
    :param cat_column_1:
    :param cat_column_2:
    :return:
    """
    contingency_table = pd.crosstab(data[cat_column_1], data[cat_column_2])
    chi2_stat, _, _, _ = chi2_contingency(contingency_table)
    n = data.shape[0]
    min_dim = min(contingency_table.shape) - 1
    cramers_v = 0
    if min_dim != 0:
        cramers_v = np.sqrt(chi2_stat / (n * min_dim))
    return cramers_v


def get_corr_cat_to_num(data, cat_column, num_column):
    """
    Permet de calculer la correlation entre une variable catégorielle et une variable numérique
    :param data:
    :param cat_column:
    :param num_column:
    :return:
    """
    grouped_data = {}
    unique_cat = data[cat_column].unique()
    for r in unique_cat:
        grouped_data[r] = data[data[cat_column] == r][num_column].values

    _, p_value = f_oneway(*grouped_data.values())
    p_value = 0 if np.isnan(p_value) else p_value
    return p_value


def get_corr_num_to_mum(data, num_column_1, num_column_2, method='spearman'):
    """
    Calcule la corrélation entre 2 variables numériques: 'pearson', 'kendall', 'spearman'
    :param data:
    :param num_column_1:
    :param num_column_2:
    :param method:
    :return:
    """
    corr = data[num_column_1].corr(data[num_column_2], method=method)
    return corr


def get_all_corr_cat(data, col, num_cols, cat_cols):
    """
    Permet de calculer les corrélations entre une variable catégorielle et les autres
    :param data:
    :param col:
    :param num_cols:
    :param cat_cols:
    :return:
    """
    result_num = []
    num_cols = [c for c in num_cols if c != col]
    for c in num_cols:
        corr = get_corr_cat_to_num(data, cat_column=col, num_column=c)
        result_num.append(corr)

    result_cat = []
    cat_cols = [c for c in cat_cols if c != col]
    for c in cat_cols:
        corr = get_corr_cat_to_cat(data, cat_column_1=col, cat_column_2=c)
        result_cat.append(corr)

    result_cat = pd.DataFrame({col: result_cat}, index=cat_cols)
    result_num = pd.DataFrame({col: result_num}, index=num_cols)
    return result_cat, result_num


def get_all_corr_num(data, col, num_cols, cat_cols):
    """
    Permet de calculer les corrélations entre variable numérique et les autres
    :param data:
    :param col:
    :param num_cols:
    :param cat_cols:
    :return:
    """
    result_num = []
    for c in num_cols:
        result_num.append(get_corr_num_to_mum(data, num_column_1=col, num_column_2=c))

    result_cat = []
    for c in cat_cols:
        result_cat.append(get_corr_cat_to_num(data, num_column=col, cat_column=c))

    result_cat = pd.DataFrame({col: result_cat}, index=cat_cols)
    result_num = pd.DataFrame({col: result_num}, index=num_cols)
    return result_cat, result_num


def get_corr_cat_2_cat_data(df, xcol, ycol):
    """
    Données pour le graphe de corrélation
    :param ycol:
    :param xcol:
    :param df:
    :return:
    """
    return df.groupby([xcol, ycol]).size().unstack(fill_value=0)


def get_corr_cat_2_cat_data_many_y(df, df_cat, xcol, ycol):
    """
    Données pour le graphe de corrélation lorsque les catégories en y sont nombreuses
    :param df_cat:
    :param ycol:
    :param xcol:
    :param df:
    :return:
    """
    df_cat_ = df_cat.rename(columns={'valeur': ycol})
    df_cat_ = df_cat_[[ycol, 'category']]
    merged_df = pd.merge(df, df_cat_, on=ycol, how='left')
    return get_corr_cat_2_cat_data(merged_df, xcol, 'category')


# Questionnement

def get_processor(numeric_features, categorical_features):
    """
    Methode permettant de definir les transformations sur les colonnes
    :param numeric_features: colonnes numériques
    :param categorical_features: colonnes catégorielles
    :return:
    """
    categorical_transformer = Pipeline(steps=[
        ('ohe', OneHotEncoder(handle_unknown='ignore'))
    ])
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])
    transformers = []
    if numeric_features:
        transformers.append(('num', numeric_transformer, numeric_features))

    if categorical_features:
        transformers.append(('cat', categorical_transformer, categorical_features))

    preprocessor = ColumnTransformer(
        transformers=transformers
    )
    return preprocessor


def do_kmeans(data, numeric_columns, categorical_columns, k=2):
    """
    Permet de faire un k-means
    :param data:
    :param numeric_columns:
    :param categorical_columns:
    :param k:
    :return:
    """
    data_ = data.copy()
    preprocessor = get_processor(numeric_columns, categorical_columns)
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('kmeans', KMeans(n_clusters=k, random_state=42))
    ])
    pipeline.fit(data_)
    data['cluster'] = pipeline.predict(data_)
    inertia = pipeline.named_steps['kmeans'].inertia_
    return data, inertia


def get_best_k(values):
    """
    Permet de calculer le meilleur k
    :param values:
    :return:
    """
    diff_inertie = np.diff(values)

    diff_inertie = np.abs(np.diff(diff_inertie))

    best_k = np.argmax(diff_inertie) + 1

    return best_k


def run_multiple_kmeans(data, numeric_columns, categorical_columns, saveas, end, start=2):
    """
    Permet d'exécuter plusieurs fois un k-means
    :param saveas:
    :param data:
    :param numeric_columns:
    :param categorical_columns:
    :param end:
    :param start:
    :return:
    """
    inertia_values = []
    k_range = range(start, end + 1)
    for k in tqdm(range(start, end + 1)):
        _, inertia = do_kmeans(data, numeric_columns, categorical_columns, k)
        inertia_values.append(inertia)

    plt.plot(k_range, inertia_values, marker='o')
    plt.xlabel('Nombre de clusters')
    plt.ylabel('Inertie')
    plt.title(f'Méthode du coude (Elbow method) k = {start}..{end}')
    plt.xticks(k_range)
    plt.grid(True)

    folder = os.path.dirname(saveas)
    os.makedirs(folder, exist_ok=True)
    plt.savefig(saveas)

    return get_best_k(inertia_values) + start


def detect_anomalies(data, numeric_columns, categorical_columns):
    """
    Permet de détecter dans des anomalies dans les clusters
    :param data:
    :param numeric_columns:
    :param categorical_columns:
    :return:
    """
    preprocessor = get_processor(numeric_columns, categorical_columns)
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('isolation_forest', IsolationForest(random_state=42))
    ])
    result = data.copy()
    clusters = result['cluster'].unique()
    for cluster_id in clusters:
        cluster_data = result[result['cluster'] == cluster_id]

        pipeline.fit(cluster_data)

        anomalies = pipeline.predict(cluster_data)

        result.loc[result['cluster'] == cluster_id, 'anomaly'] = anomalies

    result['anomaly'] = result['anomaly'].apply(lambda x: True if x == -1 else False)
    return result


def get_anomaly_cluster(data, clusterId):
    """
    Trouver anomalies pour un cluster spécific
    :param data:
    :param clusterId:
    :return:
    """
    return data[(data['cluster'] == clusterId) & (data['anomaly'])]


def get_cluster_data(data, clusterId):
    """
    Determiner les données d'un cluster
    :param data:
    :param clusterId:
    :return:
    """
    return data[data['cluster'] == clusterId]


def get_anomaly_corr(data, clusterId, num_cols, cat_cols):
    """
    Trouver anomalies pour un cluster spécific
    :param cat_cols:
    :param num_cols:
    :param data:
    :param clusterId:
    :return:
    """
    cluster_data = data[data['cluster'] == clusterId]
    corr_cat, corr_num = get_all_corr_cat(
        data=cluster_data,
        col='anomaly',
        num_cols=num_cols,
        cat_cols=cat_cols
    )
    return corr_cat, corr_num
