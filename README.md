# Time‑Series
Repositorio de análisis de series temporales en Python

## 📌 Descripción
Este proyecto contiene scripts en Python para generar, procesar y analizar series temporales. Actualmente incluye dos módulos principales:

- `ar1_process.py`: generación y análisis de procesos autoregresivos de orden 1 (AR(1)).
- `whitenoise.py`: generación/gestión de ruido blanco, para uso en el contexto de series temporales.

## 🧰 Estructura del repositorio
time‑series/
│
├── ar1_process.py 
├── whitenoise.py 
└── README.md 


## ⚙️ Requisitos
- Python 3.x
- Dependencias estándar de Python (ej: `numpy`, `scipy`, `matplotlib`)  

> Asegurese de tener instaladas las dependencias antes de ejecutar los scripts.

## 📊 ¿Qué puedes hacer con este repositorio? 
- Generar datos simulados de series temporales (AR(1), ruido blanco).
- Estudiar propiedades estadísticas de series temporales: autocorrelación, estacionariedad, etc.
- Extender los scripts para modelos más complejos (AR(p), MA, ARMA, ARIMA…).
- Usarlo como base para tareas de forecasting o modelado de series temporales reales.

## 🧪 Buenas prácticas
- Modifica los parámetros del modelo (coeficiente φ en AR(1), tamaño de la muestra, varianza del ruido) para observar su efecto.
- Visualiza la serie y su autocorrelograma para entender la estructura temporal.
- Comprueba estacionariedad (por ejemplo usando test de Dickey‑Fuller).
- Guarda resultados o figuras si planeas hacer comparaciones o un reporte de análisis.

## Autor: Juan Pablo Estrada Lucero
