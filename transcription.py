import whisper

def audio_a_texto(ruta):
    model = whisper.load_model("base")
    result = model.transcribe(ruta)

    print(result["text"])