# Clasificación de imágenes: Botellas de Plástico / Vidrio

Este proyecto tiene como objetivo clasificar imágenes de botellas como de plástico o de vidrio utilizando algoritmos de aprendizaje automático. Se ha creado un dataset artificial para entrenar el modelo.

## Dataset

A continuación se muestra una imagen del dataset artificial utilizado para entrenar el modelo:

<p align="center">
  <img src="https://i.postimg.cc/rsKxywrB/dataset-artificial.png" alt="Dataset">
</p>

El dataset contiene imágenes de botellas de plástico y vidrio en diferentes ángulos y posiciones. Se han agregado efectos de iluminación y ruido para aumentar la variabilidad de las imágenes y mejorar el rendimiento del modelo.

Se seleccionaron imágenes random de internet para hacer una pequeña demostración de la predicción del modelo:

<p align="center">
  <img src="https://i.postimg.cc/PJXdsSCJ/data-test.png" alt="Data Test">
</p>

**Los resultados:**

A continuación se muestran los resultados de la clasificación de las imágenes de prueba:

<p align="center">
  <img src="https://i.postimg.cc/90LCWy9p/resultados.png" alt="Resultados">
</p>

## Preparación de imágenes

Se define `entrenamiento_datagen` para preparar las imágenes de entrenamiento con las siguientes transformaciones:
- Escalar los valores de los píxeles entre 0 y 1 (`rescale=1./255`).
- Inclinar las imágenes (`shear_range=0.2`).
- Hacer zoom a algunas imágenes (`zoom_range=0.2`).
- Invertir algunas imágenes horizontalmente (`horizontal_flip=True`).

Por otro lado, se define `test_datagen` para preparar los datos de validación solo escalando los valores de los píxeles entre 0 y 1.

Luego se definen los generadores de entrenamiento (`entrenamiento_generador`), validación (`validacion_generador`) y todas las imágenes (`all_data`) utilizando las funciones `flow_from_directory` que cargan las imágenes de los respectivos directorios y las preparan utilizando los generadores definidos anteriormente.

## Entrenamiento y evaluación del modelo

Se define una lista `funAct` que contiene diferentes funciones de activación para ser utilizadas en las capas de la red neuronal convolucional.

Se crea un ciclo que recorre las funciones de activación de la lista `funAct` y para cada una se define un modelo de red neuronal convolucional `cnn`, que se entrena utilizando los datos de `entrenamiento_generador` y `validacion_generador`. El modelo se compila con la función de pérdida 'categorical_crossentropy', el optimizador 'adam' y la métrica 'accuracy'.

Al final de cada iteración, se guarda en una lista `Resumen` los resultados de la función de activación utilizada, la mejor precisión de validación (`val_accuracy`), la menor pérdida de validación (`val_loss`) y la época en que se obtuvieron dichos resultados.

Luego se define un segundo modelo `cnn2` con una función de activación 'relu' y se entrena utilizando el generador `all_data` para aprovechar todos los datos para el entrenamiento final. El modelo
