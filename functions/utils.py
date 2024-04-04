import pandas as pd


def load_data(path):
    """
    Méthode permettant de charger les données
    :param path:
    :return:
    """
    return pd.read_csv(path, sep=',')
