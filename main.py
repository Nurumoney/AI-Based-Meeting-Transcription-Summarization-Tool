import tkinter as tk
from tkinter import scrolledtext
import audio_recorder
import transcriber

# ----------------------- GUI Setup -----------------------
app = tk.Tk()
app.title("Meeting Transcription & Summarization Tool")
app.geometry("700x500")  # Set the window size

# Start Recording Button
start_button = tk.Button(app, text="Start Recording", width=20, command=audio_recorder.start_recording)
start_button.pack(pady=10)

# Stop Recording Button
stop_button = tk.Button(app, text="Stop Recording", width=20, command=audio_recorder.stop_recording)
stop_button.pack(pady=10)

def process_audio():
    """
    Transcribes the saved audio file and then summarizes the transcription.
    The results are displayed in the output text area.
    """
    output_text.delete(1.0, tk.END)  # Clear previous output
    output_text.insert(tk.END, "Transcribing audio...\n")
    app.update()  # Refresh GUI

    # Transcription step
    transcript = transcriber.transcribe_audio("output.wav")
    output_text.insert(tk.END, f"\nFull Transcript:\n{transcript}\n")
    output_text.insert(tk.END, "\nSummarizing transcript...\n")
    app.update()

    # Summarization step
    summary = transcriber.summarize_text(transcript)
    output_text.insert(tk.END, f"\nSummary:\n{summary}\n")

# Transcribe & Summarize Button
process_button = tk.Button(app, text="Transcribe & Summarize", width=20, command=process_audio)
process_button.pack(pady=10)

# ScrolledText widget to display transcription and summary
output_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=80, height=20)
output_text.pack(pady=10)

# Instruction Label for guidance
instruction_label = tk.Label(app, text="Click 'Start Recording' to begin, 'Stop Recording' to end, then 'Transcribe & Summarize'.")
instruction_label.pack(pady=5)

# ----------------------- Main Loop & Cleanup -----------------------
def on_closing():
    """
    Cleans up resources before closing the application.
    """
    # Ensure any active recording is stopped
    audio_recorder.is_recording = False
    audio_recorder.terminate_audio()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()
