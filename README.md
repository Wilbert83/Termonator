# 🌡️ Termonator — Simulador de Curva de Calentamiento H₂O

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Activo-brightgreen)
![Termodinámica](https://img.shields.io/badge/Área-Termodinámica-orange)

Simula la curva de calentamiento del agua en una parrilla eléctrica,
calculando temperatura y masa líquida segundo a segundo hasta la
evaporación completa.

Desarrollado como proyecto de **Termodinámica - 1437** (Gpo:9 Sem:2023-2).

---

## Características

- Calcula T_sat a partir de la presión con la ecuación **IAPWS-IF97 Región 4**
- Modela h_fg en función de T_sat
- Genera gráficas **T(t)** y **m(t)** con matplotlib
- Validación de entradas y manejo de errores

---

## Modelo físico

El simulador cubre dos fases:

**1. Calentamiento sensible** — mientras T < T_sat, la temperatura sube linealmente:

```
T(t) = T₀ + (P · t) / (m · cp)       cp = 4186 J/(kg·°C)
```

**2. Cambio de fase** — una vez que T = T_sat, la energía se usa en evaporar agua:

```
Δm(t) = (P · t) / h_fg
```

La entalpía de vaporización se aproxima con:

```
h_fg [kJ/kg] = 2256.4 · [(1 - T_sat[K]/647.096) / (1 - 0.57665623)]^0.375
```

La temperatura de saturación se obtiene de la ecuación **IAPWS-IF97** (10 constantes), válida para presiones entre 0.000611 y 22.064 MPa.

---

## Uso

```bash
pip install -r requirements.txt
python termonator.py
```

---

## Parámetros de entrada

| Parámetro | Unidad | Descripción |
|---|---|---|
| Temperatura inicial | °C | Estado inicial del agua |
| Masa | kg | Masa de agua en el recipiente |
| Tiempo | s | Duración de la simulación |
| Potencia | W | Potencia de la parrilla |
| Presión | MPa | Presión atmosférica del sistema |

---

## Ejemplo de ejecución

Parámetros: T₀ = 25 °C · m = 1 kg · t = 2400 s · P = 2000 W · p = 0.101325 MPa

```
  Temperatura de saturación : 99.9743 °C
  Entalpía de vaporización  : 2256.4854 kJ/kg

    t [s]      T [°C]      m [kg]
  -----------------------------------
        0      25.000      1.0000
       50      48.889      1.0000
      100      72.778      1.0000
      150      96.667      1.0000
      ...
      156      99.534      1.0000   ← inicio de ebullición
      157      99.974      0.9991
      158      99.974      0.9982
      ...
     1283      99.974      0.0011
     1284      99.974      0.0002
     1285   — vapor —           —   ← evaporación completa
```

---

## Autores

Miguel Nahuatlato · Alex Girón · Sarah
