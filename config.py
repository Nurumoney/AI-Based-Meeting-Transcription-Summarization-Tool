import pyaudio

# Audio recording configuration
CHUNK = 1024                       # Number of audio frames per buffer
FORMAT = pyaudio.paInt16           # 16-bit resolution
CHANNELS = 1                       # Mono recording
RATE = 44100                       # Sampling rate in Hz
WAVE_OUTPUT_FILENAME = "output.wav"  # Output WAV file name
