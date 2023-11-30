# Proyecto de Transcripción y Respuesta por Voz Taller UNI 
Este proyecto consiste en un script en Python que utiliza la biblioteca SpeechRecognition para transcribir voz a texto, GPT-4 All para generar respuestas basadas en texto, y Whisper para transcribir el contenido de archivos de audio. Además, se emplea pyttsx3 para convertir el texto generado por GPT-4 All en voz.

## Requisitos
Asegúrate de tener instaladas las siguientes bibliotecas de Python:

```bash

conda create -n gpt4alltaller

conda activate gpt4alltaller

conda list

conda install python=3.11

conda install -c anaconda pip

python -m pip install gpt4all==1.0.5

python -m pip install openai-whisper

python -m pip install SpeechRecognition

python -m pip install playsound

python -m pip install PyAudio==0.2.13

python -m pip install soundfile
```

En powershell:
```bash

Set-ExecutionPolicy Unrestricted
```

Instalar choco:

```bash
choco install ffmpeg
```

Instalar librerias faltantes:

```bash

python -m pip install pyttsx3

python -m pip install tiktoken

conda info --envs

```
Ahora continuar ejecutando:+

* Ejecutar python whispertest.py

* Ejecutar python tiktokentest.py

 

Además, instala Anaconda y Visual C++ Build Tools. Crea una carpeta en C:\TallerIA para organizar el proyecto.

## Configuración
Antes de ejecutar el script, asegúrate de tener los modelos necesarios en las rutas correctas:

El modelo de GPT-4 All debe ubicarse en
```bash
 "C:\Users\nickq\AppData\Roaming\nomic.ai\ggml-model-gpt4all-falcon-q4_0.bin".
```


El modelo base de Whisper debe estar en 
```bash
"C:\Users\nickq\.cache\whisper\base.pt".
"C:\Users\nickq\.cache\whisper\tiny.pt".

```

Ejecuta los siguientes comandos en powershell para descargar archivos esenciales:

```powershell
Invoke-WebRequest -Uri "https://openaipublic.blob.core.windows.net/gpt-2/encodings/main/encoder.json" -OutFile "encoder.json"
Invoke-WebRequest -Uri "https://openaipublic.blob.core.windows.net/gpt-2/encodings/main/vocab.bpe" -OutFile "vocab.bpe"
```

Edita el archivo
```bash
 C:\Users\nickq\.conda\envs\gpt4alltaller\Lib\site-packages\tiktoken_ext\openai_public.py 
```
con la sección que comienza con mergeable_ranks de la siguiente manera:

```python
mergeable_ranks = data_gym_to_mergeable_bpe_ranks(
        vocab_bpe_file=r"C:\Users\nickq\.cache\whisper\vocab.bpe",
        encoder_json_file=r"C:\Users\nickq\.cache\whisper\encoder.json",
    )
```

Ejecuta choco install ffmpeg en PowerShell para instalar FFmpeg.


Buscamos
```bash

C:\Users\nickq\.conda\envs\gpt4alltaller\Lib\site-packages\tiktoken_ext\openai_public.py
```

Abrimos y editamos:
```python

 mergeable_ranks = data_gym_to_mergeable_bpe_ranks(
        vocab_bpe_file=r"C:\Users\nickq\.cache\whisper\vocab.bpe",
        encoder_json_file=r"C:\Users\nickq\.cache\whisper\encoder.json",
    )
```

## Uso
Ejecuta el script y sigue las instrucciones por voz:

* Inicia el programa diciendo 'start' para comenzar la transcripción.
* Habla para proporcionar la entrada de voz.
* Cuando desees detener la transcripción y salir, di 'stop'.
## Personalización
* Ajusta la longitud máxima de tokens generados por GPT-4 All modificando el parámetro max_tokens=200 en la función model.generate.
* Cambia la voz de salida modificando la línea engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0') en la función text_to_speech.
## Notas Importantes
* Asegúrate de tener un micrófono funcional conectado al dispositivo.
* El programa utiliza la API de reconocimiento de voz de Google, por lo que se requiere conexión a internet para su funcionamiento.
* ¡Disfruta del proyecto y explora las posibilidades de interacción por voz!.

# GPT4ALL + PDF
## Version para alimentarse de PDF
En el archivo main-pdf.py entrarás una versión que te permite alimentar a GPT con un pdf. En el ejemplo se hará una consulta a GPT, se realizará la búsqueda por similitud en el espacio vectorial creado por los embeddings para encontrar el documento más relevante en relación con la pregunta y luego traera la respuesta.

## Requisitos

Instalar https://visualstudio.microsoft.com/es/visual-cpp-build-tools/


```bash
python -m pip install langchain==0.0.173 
python -m pip install chromadb==0.3.23
python -m pip install pypdf==3.8.1 
python -m pip install pygpt4all==1.1.0 
python -m pip install sentence_transformers
 ```
