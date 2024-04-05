import os
import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors


# EXPLORATION
def load_data(path):
    """
    Function permettant de charger les données
    :param path:
    :return:
    """
    return pd.read_csv(path, sep=',')


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


def plot_proportion(data, xcol, ycol, title, xtitle, ytitle, saveas, logy=True):
    """
    Permet de representer les proportions de catégories de données
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
    plt.xticks(rotation=0)
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
