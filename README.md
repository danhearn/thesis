# 512x512 Spectrogram Reconstruction Experimentation

## Spectrogram Generation

C:\Users\danhearn\Documents\GitHub\thesis\spectrogram-data\spectrograms\chunk_10_seconds_spectrogram_512x512.jpeg

## Audio reconstruction

### Reconstructed with phase information

**Up to 10 seconds audio is indistinguishable from the original**

https://github.com/user-attachments/assets/b8e4ae3f-16b1-490f-8630-10653a3a80bf

**Above 10 seconds audio quality gets progressively worse, starting with the low-end.**

https://github.com/user-attachments/assets/6aa12c05-5c79-4558-bf52-5f5b56a88246

### Reconstructed without phase information

**Using librosa, converting to Mel then reconstructing with Griffin-Lim**

https://github.com/user-attachments/assets/cded1591-5fd4-4377-a9da-02e7f2d19478

**Using Riffusion's conversion pipeline that wraps torchaudio, again converting to Mel then reconstructing with Griffin-Lim. Very hard to find any similarity with original audio.**

https://github.com/user-attachments/assets/2aa04f51-5fb8-4af7-aeb8-5c8b61827e30





