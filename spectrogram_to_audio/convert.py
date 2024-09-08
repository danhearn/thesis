# Code from riffusion 

import numpy as np
import pydub
from PIL import Image

from riffusion.spectrogram_converter import SpectrogramConverter
from riffusion.spectrogram_params import SpectrogramParams
from riffusion.util import image_util


class SpectrogramImageConverter:
    """
    Convert between spectrogram images and audio segments.

    This is a wrapper around SpectrogramConverter that additionally converts from spectrograms
    to images and back. The real audio processing lives in SpectrogramConverter.
    """

    def __init__(self, params: SpectrogramParams, device: str = "cuda"):
        self.p = params
        self.device = device
        self.converter = SpectrogramConverter(params=params, device=device)


    def audio_from_spectrogram_image(
        self,
        image: Image.Image,
        apply_filters: bool = True,
        max_value: float = 30e6,
    ) -> pydub.AudioSegment:
        """
        Reconstruct an audio segment from a spectrogram image.

        Args:
            image: Spectrogram image (in pillow format)
            apply_filters: Apply post-processing to improve the reconstructed audio
            max_value: Scaled max amplitude of the spectrogram. Shouldn't matter.
        """
        spectrogram = image_util.spectrogram_from_image(
            image,
            max_value=max_value,
            power=self.p.power_for_image,
            stereo=self.p.stereo,
        )

        segment = self.converter.audio_from_spectrogram(
            spectrogram,
            apply_filters=apply_filters,
        )

        return segment
    
    
image = Image.open("/Users/danh/Documents/GitHub/thesis/spectrogram_to_audio/cw_amen05_158_spectrogram_512x512.png")
    
params = SpectrogramParams(
    stereo=False,
    sample_rate=44100,
    step_size_ms=10,
    window_duration_ms=100,
    padded_duration_ms=400,
    num_frequencies=512,
    min_frequency=0,
    max_frequency=10000,
    mel_scale_norm=None,
    mel_scale_type="htk",
    max_mel_iters=200,
    num_griffin_lim_iters=32,
    power_for_image=0.25,
)
    
img_converter = SpectrogramImageConverter(params=params, device="cpu")

img_converter.audio_from_spectrogram_image(image)