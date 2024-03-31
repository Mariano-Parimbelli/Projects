# Transcripción y Resumen de Videos de YouTube

Este proyecto consiste en una plataforma web desarrollada con Flask que permite transcribir y resumir videos de YouTube utilizando modelos de lenguaje generativo como LLM Bart y Whisper de OpenAI.

## Descripción del Proyecto

El proyecto se centra en la transcripción y resumen de videos de YouTube utilizando modelos de lenguaje generativo. Se emplean tecnologías de inteligencia artificial para convertir el audio en texto y generar un resumen del contenido.

## Funcionalidades Principales

- Incluye la transcripción automática del audio de videos de YouTube utilizando el modelo LLM Bart de OpenAI.
- Proporciona la capacidad de generar un resumen del contenido del video utilizando el modelo Whisper de OpenAI.

## Tecnologías Utilizadas

- Flask como framework web en Python.
- Bibliotecas como pytube para descargar videos de YouTube, pydub para manipular archivos de audio, Whisper de OpenAI para la transcripción de voz y transformers para el resumen de texto.
- Se hace uso de la API de Google Translate para la traducción de texto.

## Resultados

Los resultados incluyen transcripciones precisas de los videos de YouTube, así como resúmenes concisos que capturan los puntos clave del contenido. La plataforma es capaz de manejar una variedad de temas y acentos de audio.

## Repositorio

El código fuente de este proyecto está disponible en [GitHub](https://github.com/mariano4659/Projects/tree/main/Youtube%20video%20transcribe%20and%20summarize).


A continuación se muestran algunas capturas de pantalla del proyecto:

![Load]([transcription.png](https://raw.githubusercontent.com/mariano4659/Projects/main/Youtube%20video%20transcribe%20and%20summarize/Captura%20de%20pantalla%202024-03-31%20122818.png))
*Figura 1: Transcripción automática del audio de un video de YouTube.*

![Resumen](summary.png)
*Figura 2: Generación de un resumen del contenido del video.*
