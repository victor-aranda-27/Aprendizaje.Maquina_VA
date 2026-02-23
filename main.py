import values as vl
import coef_recta as ct
import coef_corr as cr
import error_estandar as st
import predcc as pr
import values as vl

a, b = ct.calcular_coeficientes(vl.nomina_x, vl.ventas_y)
r, r2 = cr.calcular_metricas_ajuste(vl.nomina_x, vl.ventas_y)
error = st.calcular_error_estandar(vl.nomina_x, vl.ventas_y, a, b)
# Ejemplo de predicción
valor_prueba = 6
prediccion = pr.predecir_valor(valor_prueba, a, b)
    
# --- Mostrar Resultados ---
print(f"Ecuación de la recta: Y = {a:.3f} + {b:.3f}x")
print(f"Coeficiente de Correlación (r): {r:.4f}")
print(f"Coeficiente de Determinación (R²): {r2:.4f}")
print(f"Error Estándar de Estimación: {error:.4f}")
print("-" * 35)
print(f"Predicción para nómina de {valor_prueba}: {prediccion:.3f}")

