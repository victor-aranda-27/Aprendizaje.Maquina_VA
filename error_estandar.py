import numpy as np

def calcular_error_estandar(x, y, a, b):
    n = len(x)
    y_predichos = a + b * x
    suma_residuos_cuadrado = np.sum((y - y_predichos)**2)
    s_yx = np.sqrt(suma_residuos_cuadrado / (n - 2))
    return s_yx