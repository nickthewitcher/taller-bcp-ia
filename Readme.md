

conda init powershell

Instalar GPT4All:

https://gpt4all.io/index.html

Instalar anaconda:

https://www.anaconda.com/download/

Crear una carpeta en 

C:\TallerIA

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

En powershell:
Set-ExecutionPolicy Unrestricted

choco install ffmpeg

python -m pip install pyttsx3

python -m pip install tiktoken

conda info --envs

Ejecutar python whispertest.py

Ejecutar python tiktokentest.py


Buscamos 
C:\\Users\\nickq\\.cache\\whisper\\tiny.pt
C:\\Users\\nickq\\.cache\\whisper\\base.pt

Ejecutamos

Invoke-WebRequest -Uri "https://openaipublic.blob.core.windows.net/gpt-2/encodings/main/encoder.json" -OutFile "encoder.json"

Invoke-WebRequest -Uri "https://openaipublic.blob.core.windows.net/gpt-2/encodings/main/vocab.bpe" -OutFile "vocab.bpe"

Buscamos
C:\Users\nickq\.conda\envs\gpt4alltaller\Lib\site-packages\tiktoken_ext\openai_public.py

Abrimos y editamos:
import os
        vocab_bpe_file="C:\\Users\\nickq\\.cache\\whisper\\vocab.bpe",
        encoder_json_file="C:\\Users\\nickq\\.cache\\whisper\\encoder.json",


python -m pip install keyboard

