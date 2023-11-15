# import required libraries
import sounddevice as sd
# from scipy.io.wavfile import write
import wavio as wv

def recordMic():

    # Sampling frequency
    freq = 44100

    # Recording duration
    duration = 5

    print("recording.....")
    recording = sd.rec(int(duration * freq),
                    samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()

    print("recorded!!")

    wv.write("recorded_output.wav", recording, freq, sampwidth=2)

    return "recorded_output.wav"