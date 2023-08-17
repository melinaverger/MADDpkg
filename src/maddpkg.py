import numpy as np
import pandas as pd


def separate_sets(X, y, sf):
    """Separates X and y according to a specific binary sensitive feature.

    Parameters
    ----------
    X : pd.DataFrame
        The feature set
    y : pd.DataFrame
        The labels of the feature set X
    sf : str
        The name of the sensitive feature

    Returns
    -------
    four-tuple of pd.DataFrame
        The tuple of (X_sf0, X_sf1, y_sf0, y_sf1)
    """
    X_sf0 = X[X[sf] == 0]
    X_sf1 = X[X[sf] == 1]
    y_sf0 = y.loc[X_sf0.index]
    y_sf1 = y.loc[X_sf1.index]
    return (X_sf0, X_sf1, y_sf0, y_sf1)


def normalized_density_vector(pred_proba, e):
    """Computes the density vector.
    
    Parameters
    ----------
    pred_proba : np.ndarray of shape (n, 1)
        The predicted probabilities of positive predictions from a model
    e : float
        The probability sampling parameter
    
    Returns
    -------
    np.ndarray
        The density vector
    """
    if not (0 < e < 1):
        raise Exception("The value of argument e should be between 0 and 1 excluded.")
    elif abs(e) < 10**(-5):
        # cannot guarantee the results due to numerical approximation
        raise Exception("The value of argument e is too small.")
    
    nb_decimals = (lambda e : len(np.format_float_positional(e).split(".")[1]))(e)
    nb_components = (lambda e : int(1 // e) + 2)(e)

    PP_rounded = np.around(pred_proba, decimals=nb_decimals)

    density_vector = np.zeros(nb_components)
    proba_values = np.linspace(0, 1, nb_components)

    for i in range(len(proba_values)):
        compar = proba_values[i]
        count = 0
        for x in PP_rounded:
            if abs(x - compar) <= e/10:
                count = count + 1
        density_vector[i] = count
    
    normalized_density_vec = density_vector / np.sum(density_vector)

    return normalized_density_vec


def MADD():
    # call separate_sets and normalized_density_vector
    pass
