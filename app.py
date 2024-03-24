from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    audio_file = request.files['audioFile']
    text_input = request.form['textInput']
    
    # Save audio file if uploaded
    if audio_file:
        audio_file.save(audio_file.filename)
    
    # Execute run.py
    subprocess.run(['python', 'run.py', text_input])
    
    return 'Processing complete'

if __name__ == '__main__':
    app.run(debug=True)
