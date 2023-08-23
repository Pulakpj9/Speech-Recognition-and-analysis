# import required libraries
import sounddevice as sd
# from scipy.io.wavfile import write
import wavio as wv

def recordMic():

    # Sampling frequency
    freq = 44100

    # Recording duration
    duration = 5

    # Start recorder with the given values
    # of duration and sample frequency
    print("recording.....")
    recording = sd.rec(int(duration * freq),
                    samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()

    print("recorded!!")
    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    # write("recorded_output.wav", freq, recording)
    
    # Convert the NumPy array to audio file
    wv.write("recorded_output.wav", recording, freq, sampwidth=2)
    return "recorded_output.wav"

    # FRAMES_PER_BUFFER = 3200
    # FORMAT = pyaudio.paInt16
    # CHANNELS = 1
    # RATE = 16000

    # p = pyaudio.PyAudio()

    # stream = p.open(
    #     format=FORMAT,
    #     channels=CHANNELS,
    #     rate = RATE,
    #     input=True,
    #     frames_per_buffer=FRAMES_PER_BUFFER
    # )

    # print("start recording..")

    # seconds = 5
    # frames = []
    # for i in range(0,int(RATE/FRAMES_PER_BUFFER*seconds)):
    #     data = stream.read(FRAMES_PER_BUFFER)
    #     frames.append(data)

    # stream.stop_stream()
    # stream.close()
    # p.terminate()

    # obj = wave.open("recorded_output.wav","wb")
    # obj.setnchannels(CHANNELS)
    # obj.setsampwidth(p.get_sample_size(FORMAT))
    # obj.setframerate(RATE)
    # obj.writeframes(b"".join(frames))
    # obj.close()
    # return "recorded_output.wav"