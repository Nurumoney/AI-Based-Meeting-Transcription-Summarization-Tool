# Meeting Transcription & Summarization Tool
**An AI-Powered Desktop Application to Record, Transcribe, and Summarize Meetings**

## Description
This project is a desktop application designed to streamline meeting documentation. It records live audio from your microphone, transcribes the speech into text, and then summarizes the content using advanced NLP models. The primary components are:
- **Audio Recording:** Captures audio via PyAudio.
- **Speech Transcription:** Converts the audio file to text using Google’s Speech Recognition API.
- **Text Summarization:** Uses Hugging Face Transformers to create a concise summary.
- **Graphical User Interface:** Provides an intuitive control panel built with Tkinter.

## Table of Contents
- [Installation/Getting Started](#installationgetting-started)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Features](#features)
- [Configuration/Customization](#configurationcustomization)
- [Contributing Guidelines](#contributing-guidelines)
- [License](#license)
- [Contact/Support](#contactsupport)
- [Credits/Acknowledgments](#creditsacknowledgments)
- [Screenshots](#screenshots)

## Installation/Getting Started

### Prerequisites
- Python 3.x (version 3.7+ recommended)
- pip (Python package installer)

### Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/MeetingTranscriptionApp.git
   cd MeetingTranscriptionApp
   ```

2. **Set Up a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python main.py
   ```

## Usage
Upon running the application, you will see a window with three primary buttons:
- **Start Recording:** Begins capturing live audio.
- **Stop Recording:** Ends the capture and saves the audio to `output.wav`.
- **Transcribe & Summarize:** Processes the saved audio—first transcribing the speech into text, then summarizing it. The full transcript and summary are displayed in the output text area.

## Technical Details

### Project Structure
- **config.py:**  
  Stores configuration parameters (e.g., audio buffer size, format, channels, sample rate, and output filename).

- **audio_recorder.py:**  
  - Uses PyAudio to open an input stream with the parameters from `config.py`.
  - Continuously reads audio data in chunks and stores them in a list.
  - Upon stopping, it writes the audio frames to `output.wav` using Python’s `wave` module.

- **transcriber.py:**  
  - Loads the recorded WAV file and uses the SpeechRecognition library to transcribe audio to text.
  - Passes the transcription to a Hugging Face Transformers summarization pipeline to produce a concise summary.

- **main.py:**  
  - Implements a Tkinter-based GUI.
  - Integrates recording, transcription, and summarization functions.
  - Displays the output (full transcript and summary) in a scrollable text area.

### How It Works
1. **Recording:**
   - The `start_recording()` function sets a flag and spawns a new thread that calls `record_audio()`.
   - `record_audio()` reads audio in real time from the microphone using PyAudio and stores the data.
   - When `stop_recording()` is called, the audio frames are written to `output.wav`.

2. **Transcription:**
   - The `transcribe_audio()` function uses SpeechRecognition’s `recognize_google()` method to convert the audio in `output.wav` into text.

3. **Summarization:**
   - The `summarize_text()` function initializes a summarization pipeline from Hugging Face Transformers.
   - It processes the transcribed text to generate a summary, taking into account parameters like minimum and maximum lengths.

4. **GUI Operation:**
   - Tkinter buttons are linked to these functions, ensuring that users can control the entire workflow via the graphical interface.

## Features
- **Real-Time Audio Recording:** Captures live audio using your system’s microphone.
- **Accurate Speech-to-Text:** Utilizes Google’s Speech Recognition API for transcription.
- **Automated Summarization:** Leverages a pre-trained NLP model to create concise summaries.
- **User-Friendly Interface:** Built with Tkinter for ease of use.
- **Modular Codebase:** Organized into distinct modules for configuration, recording, transcription, and GUI management.

## Configuration/Customization
- **Audio Parameters:** Adjust the recording settings (CHUNK size, FORMAT, CHANNELS, RATE, and output filename) in `config.py`.
- **Summarization Settings:** Modify summarization parameters (e.g., `max_length`, `min_length`) in `transcriber.py` to fine-tune the summary.
- **Model Selection:** Change the summarization model by altering the pipeline initialization in `transcriber.py`.

## Contributing Guidelines
Contributions are welcome! To contribute:
1. **Fork** the repository.
2. **Create a New Branch** for your feature or bug fix.
3. **Commit** your changes with clear, descriptive messages.
4. **Open a Pull Request** detailing your improvements.

## Contact/Support
For questions, suggestions, or issues:
- **GitHub Issues:** Open an issue in the repository.
- **Email:** [your-email@example.com](vaskarb.cs.20@nitj.ac.in)

## Credits/Acknowledgments
- **PyAudio:** For handling live audio recording.
- **SpeechRecognition:** For converting audio to text.
- **Transformers (Hugging Face):** For providing the summarization model.
- **Tkinter:** For the desktop GUI.
- Thanks to all the open-source contributors whose work made this project possible.

## Screenshots
![Screenshot 1](path/to/screenshot1.png)
![Screenshot 2](path/to/screenshot2.png)
```
