import numpy as np


def calcular_metricas_ajuste(x, y):
    n = len(x)
    sum_x, sum_y = np.sum(x), np.sum(y)
    sum_x2, sum_y2 = np.sum(x**2), np.sum(y**2)
    sum_xy = np.sum(x * y)
    
    # Coeficiente de Correlación (r)
    num_r = (n * sum_xy) - (sum_x * sum_y)
    den_r = np.sqrt(((n * sum_x2) - (sum_x**2)) * ((n * sum_y2) - (sum_y**2)))
    r = num_r / den_r
    
    # Coeficiente de Determinación (R²)
    r2 = r**2
    
    return r, r2