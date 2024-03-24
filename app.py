from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Handle the form submission
    text_input = request.form['textInput']
    audio_file = request.files['audioFile']
    
    # Save the audio file
    audio_file.save(audio_file.filename)
    
    # Call the run.py script with appropriate arguments
    output = subprocess.check_output(['python', 'run.py', audio_file.filename, text_input])
    
    return render_template('index.html', output=output.decode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True)
