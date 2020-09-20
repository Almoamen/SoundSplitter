import pyaudio
import wave


def play_wav_file(filename):
    """
    Play a .wav file
    :param filename: The name of the .wav audio file we're trying to play
    """
    try:
        wf = wave.open(filename)
    except FileNotFoundError:
        print("The file " + filename + " could not be found.")
        return
    p = pyaudio.PyAudio()
    chunk = 1024
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(chunk)
    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)

def main():
    play_wav_file('FOB_Dead_On_Arrival.wav')


if __name__ == "__main__":
    main()