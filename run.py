import whisper
import gemini_summarize

model = whisper.load_model("base")
audio_file = input("")
result = model.transcribe(audio_file)
transcription = result["text"]

print(gemini_summarize.get_summary(transcription))