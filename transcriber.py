import speech_recognition as sr
from transformers import pipeline

def transcribe_audio(filename):
    """
    Converts a WAV audio file into text using SpeechRecognition and Google's API.
    """
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(filename) as source:
            audio_data = recognizer.record(source)
        # Transcribe the audio using Google's API (requires an internet connection)
        text = recognizer.recognize_google(audio_data)
        print("Transcription completed.")
        return text
    except sr.RequestError:
        error_message = "Could not request results from the speech recognition service."
        print(error_message)
        return error_message
    except sr.UnknownValueError:
        error_message = "Audio was unclear. No transcription available."
        print(error_message)
        return error_message
    except Exception as e:
        error_message = f"An error occurred during transcription: {e}"
        print(error_message)
        return error_message

def summarize_text(text):
    """
    Summarizes the provided text using a pre-trained transformer model.
    """
    try:
        summarizer = pipeline("summarization")
        # Ensure the text is long enough for summarization
        if len(text.split()) < 30:
            return "The transcription is too short for summarization."
        summary_output = summarizer(text, max_length=130, min_length=30, do_sample=False)
        summary = summary_output[0]['summary_text']
        print("Summarization completed.")
        return summary
    except Exception as e:
        error_message = f"An error occurred during summarization: {e}"
        print(error_message)
        return error_message
