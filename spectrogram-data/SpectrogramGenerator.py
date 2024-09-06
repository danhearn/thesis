import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

class SpectrogramGenerator:
    def __init__(self, input_audio_file, output_image_path, output_audio_file_path,
                 output_spectrogram=True, output_audio_file=False, 
                 n_fft=1024, hop_length=512):
        self.audio_file = input_audio_file
        self.y, self.sr = librosa.load(self.audio_file, sr=None)
        self.output_spectrogram = output_spectrogram
        self.output_audio_file = output_audio_file
        self.n_fft = n_fft
        self.hop_length = int(len(self.y) / hop_length)
        self.output_image_path = output_image_path
        self.output_audio_file_path = output_audio_file_path

    def save_spectrogram(self, S_db_resized):
        # Create a figure without any axes or titles
        fig, ax = plt.subplots(figsize=(5.12, 5.12))
        ax.axis('off')  # Turn off axes
        librosa.display.specshow(S_db_resized, sr=self.sr, hop_length=self.hop_length, x_axis=None, y_axis=None, cmap='inferno')
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Remove padding

        # Save the spectrogram image without any additional chart elements
        output_image_path = f'{self.output_image_path}_spectrogram_512x512.png'
        plt.savefig(output_image_path, bbox_inches='tight', pad_inches=0, dpi=100)
        plt.close()

    def save_audio_file(self, D):
        y_reconstructed = librosa.istft(D, hop_length=self.hop_length)

        sf.write(f"{self.output_audio_file_path}.wav", y_reconstructed, self.sr)
    
    def generate_spectrogram(self):
        # Generate the spectrogram
        D = librosa.stft(self.y, n_fft=self.n_fft, hop_length=self.hop_length)
        S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
        # Resize the spectrogram to 512x512 if needed (padding or cropping)
        S_db_resized = librosa.util.fix_length(S_db, size=512, axis=1)

        assert S_db_resized.shape == (513, 512), f"Spectrogram shape is {S_db_resized.shape}, expected (513, 512)"

        if self.output_spectrogram:
            # Save the spectrogram to a file
            self.save_spectrogram(S_db_resized)

        if self.output_audio_file:
            # Save the audio file
            self.save_audio_file(D)



        
    

        
