# Thesis

## Spectrogram Testing

<img src="cw_amen06_158_spectrogram_512x512.png">

Some scripts testing out spectrograms at 512*512, which is the same size as the realtime image output from stream diffusion. 

Overall, audio less than 10 seconds sounds very good. As you get towards 20 seconds, the sound is noticably bitty/steppy. This is because the frequency bin size is 1 pixel. As the output image size is limited to 512, longer audio clips are squashed, therefore audio information overtime is lost. 

**Original Audio**

<audio controls>
  <source src="cw_amen05_158.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

**Reconstructed Audio**

<audio controls>
  <source src="cw_amen05_158_reconstructed.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

Anyway, we now have a tool to generate a dataset of 512x512 spectrograms from audio.