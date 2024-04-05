import os
import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors


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
    if np.isnan(value):
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
    if np.isnan(value):
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
    if np.isnan(value):
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
