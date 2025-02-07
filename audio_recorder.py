import pyaudio
import wave
import threading
import time
from config import CHUNK, FORMAT, CHANNELS, RATE, WAVE_OUTPUT_FILENAME

# Global flags and objects for recording
is_recording = False
audio_frames = []
p = pyaudio.PyAudio()


def record_audio():
    """
    Continuously records audio from the microphone until 'is_recording' is set to False.
    """
    global audio_frames, is_recording
    try:
        # Open the audio stream for recording
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        audio_frames = []  # Clear previous audio frames

        while is_recording:
            # Read data from the audio stream and append it to the audio_frames list.
            data = stream.read(CHUNK, exception_on_overflow=False)
            audio_frames.append(data)
    except Exception as e:
        print(f"Error during recording: {e}")
    finally:
        # Close the stream properly after recording stops
        stream.stop_stream()
        stream.close()


def start_recording():
    """
    Sets the recording flag and starts a new thread for audio recording.
    """
    global is_recording
    if is_recording:
        print("Recording is already in progress!")
        return
    is_recording = True
    threading.Thread(target=record_audio, daemon=True).start()
    print("Recording started...")


def stop_recording():
    """
    Stops the recording and saves the captured audio frames to a WAV file.
    """
    global is_recording, audio_frames
    if not is_recording:
        print("Recording is not in progress!")
        return
    is_recording = False  # Signal the recording thread to stop
    time.sleep(0.5)  # Allow some time for the thread to finish

    try:
        # Write the audio frames to a WAV file
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(audio_frames))
        wf.close()
        print(f"Recording stopped and saved as {WAVE_OUTPUT_FILENAME}")
    except Exception as e:
        print(f"Error saving the recording: {e}")


def terminate_audio():
    """
    Terminates the PyAudio instance to release system resources.
    """
    p.terminate()
