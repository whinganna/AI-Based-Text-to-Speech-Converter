from flask import Flask, request, send_file
from gtts import gTTS
import io

app = Flask(__name__)

@app.route("/tts", methods=["POST"])
def text_to_speech():
    text = request.json["text"]
    tts = gTTS(text)
    
    audio_io = io.BytesIO()
    tts.write_to_fp(audio_io)
    audio_io.seek(0)
    
    return send_file(audio_io, mimetype="audio/mp3")

if __name__ == "__main__":
    app.run(debug=True)
