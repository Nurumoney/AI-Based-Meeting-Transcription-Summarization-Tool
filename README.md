# AI-Based Meeting Transcription & Summarization Tool

It is a Python-based desktop application designed to automate the process of documenting meetings. It integrates live audio capture, AI-driven speech-to-text conversion, and advanced text summarization into one seamless workflow. Below is an outline of how the project works, the technology used, and how to deploy it on your system.

---

https://github.com/Vaskar71/AI-Based-Meeting-Transcription-and-Summarization-Desktop-App/blob/main/Text%20summarize.png?raw=true

## How It Works 

1. **Audio Recording:**  
   - **Process:** The application uses PyAudio to capture live audio from your system’s microphone. Audio is continuously read in small chunks and stored temporarily.  
   - **Output:** Once the recording is stopped, the collected audio data is saved as a WAV file using Python’s standard `wave` module.

2. **Speech Transcription:**  
   - **Process:** The saved audio file is processed by the SpeechRecognition library. Leveraging Google’s Speech Recognition API, the application converts the speech in the WAV file into a complete text transcript.  
   - **Output:** The result is a detailed transcript of the entire audio recording.

3. **Text Summarization:**  
   - **Process:** The complete transcript is then passed to a text summarization engine powered by Hugging Face’s Transformers. The summarization model condenses the transcript into a brief summary that captures the key points of the meeting.  
   - **Output:** A concise summary is generated, providing an overview of the main discussion points.

4. **Graphical User Interface (GUI):**  
   - **Framework:** The entire workflow is controlled through a user-friendly desktop interface built with Tkinter.  
   - **Functionality:**  
     - **Start Recording:** Begins capturing live audio.  
     - **Stop Recording:** Ends the audio capture and saves the recorded data.  
     - **Transcribe & Summarize:** Initiates the process of converting audio to text and generating a summary.  
     - **Display:** The full transcript and its summary are shown in a scrollable text area for easy review.

---

## Tech Stack

- **Programming Language:** Python  
- **Audio Processing:**  
  - **PyAudio:** For live audio capture.  
  - **wave:** For writing audio data to a file.
- **Speech Recognition:**  
  - **SpeechRecognition:** Utilizes Google’s Speech Recognition API to convert audio to text.
- **Natural Language Processing:**  
  - **Hugging Face Transformers:** Provides the summarization capabilities.
- **User Interface:**  
  - **Tkinter:** Creates the desktop GUI.
- **Concurrency:**  
  - **threading:** Ensures audio recording runs concurrently without freezing the GUI.

---

## How to Use the Application

1. **Installation:**
   - **Clone the Repository:**  
     Clone the project repository from GitHub to your local system.
   - **Set Up Environment:**  
     Create and activate a Python virtual environment (optional but recommended).
   - **Install Dependencies:**  
     Install all required dependencies using the provided `requirements.txt` file.

2. **Running the Application:**
   - **Launch:**  
     Run the main script (e.g., `python main.py`) to start the desktop application.
   - **Workflow:**  
     - Click **Start Recording** to capture live audio from your microphone.
     - Click **Stop Recording** to finish the capture and save the audio file.
     - Click **Transcribe & Summarize** to process the audio—first converting it to text and then generating a summary.
   - **Output:**  
     The application displays both the full transcript and the summarized version within the GUI.

