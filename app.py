import speech_recognition as sr
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "VatsalParsaniya"


@app.route('/')
def index():
    flash(" Welcome to Vatsal's site")
    return render_template('index.html')



@app.route('/audio', methods=['POST'])
def audio():
    r = sr.Recognizer()
    with open('upload/audio.wav', 'wb') as f:
        f.write(request.data)

    with sr.AudioFile('upload/audio.wav') as source:
        audio_data = r.record(source)

        try:
            text = r.recognize_google(audio_data, language='ar-SA')
            print(text)
            return_text = text
        except:
            return_text= "لم يتم تنبؤ أي كلمة"

    return str(return_text)


if __name__ == "__main__":
    app.run(debug=True)
