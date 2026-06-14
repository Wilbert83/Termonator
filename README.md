# 🌡️ Termonator — Simulador de Curva de Calentamiento H₂O

Simula la curva de calentamiento del agua en una parrilla eléctrica,
calculando temperatura y masa líquida segundo a segundo hasta la
evaporación completa.

Desarrollado como proyecto de **Termodinámica** (1437).

## Características
- Calcula T_sat a partir de la presión con la ecuación IAPWS-IF97
- Modela h_fg en función de T_sat
- Genera gráficas T(t) y m(t) con matplotlib
- Validación de entradas y manejo de errores

## Uso
```bash
pip install -r requirements.txt
python termonator.py
```

## Parámetros de entrada
| Parámetro | Unidad | Descripción |
|---|---|---|
| Temperatura inicial | °C | Estado inicial del agua |
| Masa | kg | Masa de agua en el recipiente |
| Tiempo | s | Duración de la simulación |
| Potencia | W | Potencia de la parrilla |
| Presión | MPa | Presión atmosférica del sistema |

## Autores
Miguel Nahuatlato · Alex Girón · Sarah