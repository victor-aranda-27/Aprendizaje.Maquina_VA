import numpy as np

def calcular_coeficientes(x, y):
    n = len(x)
    x_media, y_media = np.mean(x), np.mean(y)
    
    # Pendiente (b)
    numerador_b = np.sum(x * y) - (n * x_media * y_media)
    denominador_b = np.sum(x**2) - (n * (x_media**2))
    b = numerador_b / denominador_b
    
    # Intercepto (a)
    a = y_media - (b * x_media)
    
    return a, b
