# # import wave
# # import numpy as np
# # import matplotlib.pyplot as plt

# # def audioPlot(audioUrl):
# #     wav_obj = wave.open(audioUrl, 'r')

# #     sample_freq = wav_obj.getframerate()
# #     print(sample_freq)

# #     n_samples = wav_obj.getnframes()
# #     print(n_samples)

# #     n_channels = wav_obj.getnchannels()
# #     print(n_channels)

# #     t_audio = n_samples/sample_freq
# #     print(t_audio, "seconds")

# #     # Read only one channel of the audio file
# #     signal_wave = wav_obj.readframes(n_samples * n_channels)
# #     signal_array = np.frombuffer(signal_wave, dtype=np.int16)[::n_channels]
# #     print(signal_array.shape)

# #     times = np.linspace(0, n_samples/sample_freq, num=n_samples)

# #     plt.figure(figsize=(15, 5))
# #     plt.plot(times, signal_array)
# #     plt.title('Audio')
# #     plt.ylabel('Signal Value')
# #     plt.xlabel('Time (s)')
# #     plt.xlim(0, t_audio)
# #     plt.show()

# #     plt.figure(figsize=(15, 5))
# #     plt.specgram(signal_array, Fs=sample_freq, vmin=-20, vmax=50)
# #     plt.title('Left Channel')
# #     plt.ylabel('Frequency (Hz)')
# #     plt.xlabel('Time (s)')
# #     plt.xlim(0, t_audio)
# #     plt.colorbar()
# #     plt.show()


# import wave
# import numpy as np
# import matplotlib.pyplot as plt

# def audioPlot(audioUrl):
#     wav_obj = wave.open(audioUrl, 'r')

#     sample_freq = wav_obj.getframerate()
#     print(sample_freq)

#     n_samples = wav_obj.getnframes()
#     print(n_samples)

#     n_channels = wav_obj.getnchannels()
#     print(n_channels)

#     t_audio = n_samples/sample_freq
#     print(t_audio, "seconds")

#     # Read only one channel of the audio file
#     signal_wave = wav_obj.readframes(n_samples * n_channels)
#     signal_array = np.frombuffer(signal_wave, dtype=np.int16)[::n_channels]
#     print(signal_array.shape)

#     times = np.linspace(0, n_samples/sample_freq, num=n_samples)

#     fig, ax = plt.subplots(figsize=(15, 5))
#     ax.plot(times, signal_array)
#     ax.set_title('Audio')
#     ax.set_ylabel('Signal Value')
#     ax.set_xlabel('Time (s)')
#     ax.set_xlim(0, t_audio)

#     fig2, ax2 = plt.subplots(figsize=(15, 5))
#     spec = ax2.specgram(signal_array, Fs=sample_freq, vmin=-20, vmax=50)
#     ax2.set_title('Left Channel')
#     ax2.set_ylabel('Frequency (Hz)')
#     ax2.set_xlabel('Time (s)')
#     ax2.set_xlim(0, t_audio)
#     fig2.colorbar(spec)

#     print(fig,fig2)

#     return fig, fig2
