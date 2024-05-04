import whisper

model = whisper.load_model("base")
result = model.transcribe("/home/gresuto/Descargas/Primer Video Legítimo (enhanced y mejorado 2).mp3")

print(result["text"])