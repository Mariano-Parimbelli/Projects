from flask import Flask, request, render_template, session
from flask_session import Session
from flask import jsonify as json_response
from flask import request, jsonify

app = Flask(__name__)

# Configuración de Flask-Session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


def descargar_audio(url):
    from pytube import YouTube
    # Crear una instancia de la clase YouTube
    yt = YouTube(url)

    # Obtener la mejor corriente de audio disponible (en este caso, MP4)
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Descargar el audio en formato MP3
    audio_stream.download(filename='audio.mp3')

    print("Audio descargado exitosamente en formato MP3.")

#descargar_audio("https://www.youtube.com/watch?v=aMm2KyuB32g")


def dividir_audio():

    from pydub import AudioSegment

    # Nombre del archivo de audio original
    input_audio = "audio.mp3"

    # Cargar el archivo de audio
    audio = AudioSegment.from_file(input_audio)

    # Duración total del archivo de audio en milisegundos
    total_duration = len(audio)

    # Duración de cada parte (en milisegundos)
    part_duration = total_duration // 3

    # Dividir el archivo en tres partes iguales
    for i in range(3):
        start_time = i * part_duration
        end_time = (i + 1) * part_duration
        
        # Extraer la parte correspondiente del audio
        audio_part = audio[start_time:end_time]
        
        # Guardar la parte en un nuevo archivo
        output_file = f"audio_part_{i + 1}.mp3"  # Puedes cambiar la extensión a mp4 si lo deseas
        audio_part.export(output_file, format="mp3")

    print("El audio se ha dividido en tres partes iguales.")


def transcribe():

    import concurrent.futures

    import whisper

    # Lista de archivos de audio
    audio_files = ["audio_part_1.mp3", "audio_part_2.mp3", "audio_part_3.mp3"]

    # Número de subprocesos
    num_threads = 3

    # Función para transcribir un archivo de audio
    def transcribe(audio_file):
        model = whisper.load_model("base")
        result = model.transcribe(audio_file)
        if result:
            return result["text"]
        else:
            return None

    # Crear un grupo de subprocesos
    executor = concurrent.futures.ThreadPoolExecutor(num_threads)

    # Transcribir los archivos de audio en paralelo
    futures = []
    for audio_file in audio_files:
        futures.append(executor.submit(transcribe, audio_file))

    # Obtener los resultados de la transcripción
    results = [future.result() for future in futures]

    # Concatenar los textos transcritos
    text = " ".join(results)
    print("listo")
    return text






def summarize(text):
    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
    import torch
    from googletrans import Translator

    # Crear un objeto Translator
    translator = Translator()

    # Traducir el texto al inglés
    text = translator.translate(text, src='es', dest='en').text
    
    model_str = "facebook/bart-large-cnn"
    tokenizer = AutoTokenizer.from_pretrained(model_str)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_str)

    print("Resumiendo...")

    # Establecer el dispositivo en CPU
    device = "cpu"
    model.to(device)

    # Tokenizar el texto
    input_ids = tokenizer(text, return_tensors="pt").input_ids

    # Convertir los input_ids a tipo Long
    input_ids = input_ids.to(dtype=torch.long)

    # Generar la salida con una longitud máxima y mínima más corta
    output_ids = model.generate(input_ids, max_length=450, min_length=20)

    # Decodificar y mostrar el resultado
    decoded_output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    # Traducir el resumen de vuelta al español
    decoded_output = translator.translate(decoded_output, src='en', dest='es').text
    
    print("¡Listo!")
    return decoded_output


@app.route('/')
def home():  
    return render_template('index.html')


@app.route('/load-video', methods=['POST'])
def load_video():
    try:
        data = request.get_json()
        youtube_link = data['youtube_link']
        
        print(youtube_link)
        descargar_audio(youtube_link)
        dividir_audio()
        
        transcribed_text = transcribe()  # Obtener el texto transcrito
        
        # Almacenar el texto transcrito en la sesión
        session['transcribed_text'] = transcribed_text
        
        # Enviar una respuesta JSON con la información necesaria para la redirección
        response_data = {
            "redirect_event": True
        }
        
        return json_response(response_data)  # Utiliza el nuevo nombre de la variable
    except Exception as e:
        return json_response({"error": str(e)}), 400


@app.route('/index2.html')  # Agrega una ruta para index2.html
def index2():
    text = session.get('transcribed_text', '')
    return render_template('index2.html', text=text)


@app.route('/summarize', methods=['POST'])
def summarize_text():
    try:
        data = request.get_json()
        text = data['text']
        
        # Llama a la función summarize con el texto proporcionado
        summary = summarize(text)
        
        # Devuelve el resumen como JSON
        response_data = {
            "summary": summary
        }
        
        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=False)