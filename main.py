import os
import speech_recognition as sr
from gpt4all import GPT4All
import whisper
import time
import threading
import pyttsx3

model = GPT4All("C:\\Users\\nickq\\AppData\\Roaming\\nomic.ai\\ggml-model-gpt4all-falcon-q4_0.bin",allow_download=False)

r = sr.Recognizer()
base_model_path = 'C:\\Users\\nickq\\.cache\\whisper\\base.pt'
base_model = whisper.load_model(base_model_path)

listening_for_input = False
current_state = "idle"  # States: "idle", "transcribing"

def onStart(name):
    print('Starting to speak:', name)

def onEnd(name, completed):
    if completed:
        print('Speech completed successfully:', name)
    else:
        print('Speech interrupted:', name)

def log(message):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"[{current_time}] {message}")

def process_question(prompt_text):
    try:
        log(f'User question: {prompt_text}')
        if len(prompt_text.strip()) == 0:
            log("Empty question. Please speak again.")
        else:
            output = model.generate(prompt_text, max_tokens=200)
            log(f'GPT4All response: {output}')
            text_to_speech(output)
    except Exception as e:
        log(f"Error processing question: {e}")

def text_to_speech(text):
    engine = pyttsx3.init()
    #print('lista de voces')
    #for voice in engine.getProperty('voices'):
    #    print(voice)
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    engine.connect('started-utterance', onStart)
    engine.connect('finished-utterance', onEnd)
    engine.say(text)
    engine.runAndWait()

def start_transcription():
    global listening_for_input
    while listening_for_input and current_state == "transcribing":
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=2)
                log("Say something...")
                audio = r.listen(source, timeout=None)
                with open("transcription.wav", "wb") as f:
                    f.write(audio.get_wav_data())
                result = base_model.transcribe('transcription.wav')
                transcription = result['text']
                log(f"Transcription: {transcription}")
                process_question(transcription)
        except sr.UnknownValueError:
            log("Sorry, I didn't catch that. Could you please repeat?")
        except sr.RequestError as e:
            log(f"Speech recognition request failed; {e}")

def main():
    global listening_for_input
    global current_state

    log("Listening for voice input. Say 'start' to begin transcription and 'stop' to stop and exit.")
    
    while True:
        with sr.Microphone() as source:
            try:
                audio = r.listen(source, timeout=None)
                command = r.recognize_google(audio).lower()

                if "start" in command and current_state == "idle":
                    listening_for_input = True
                    current_state = "transcribing"
                    transcription_thread = threading.Thread(target=start_transcription)
                    transcription_thread.start()
                    log("Transcription started. Say something or 'stop' to end and exit.")
                elif "stop" in command and current_state == "transcribing":
                    listening_for_input = False
                    transcription_thread.join()
                    current_state = "idle"
                    log("Transcription stopped. Exiting the program.")
                    break
            except sr.UnknownValueError:
                pass  # Ignore if no speech is recognized
            except sr.RequestError as e:
                log(f"Speech recognition request failed; {e}")

if __name__ == '__main__':
    main()
