# 512x512 Spectrogram Reconstruction Experimentation

## Spectrogram Generation

**10 seconds of John Belfram's 10 Days of Blue** 

![chunk_10_seconds_spectrogram_512x512](https://github.com/user-attachments/assets/9c05fb1a-07e5-4e22-929f-99d881030dee)

## Stable Diffusion Fine Tune 
A finetune test using the dreambooth method. Dataset is five 512x512 spectrograms of 10 audio chunks of the same song as above. Trained using diffusers acceleration with 400 iterations (only a few mins on 4090 if I remember correctly)

![image_0](https://github.com/user-attachments/assets/d50f3abf-1ccc-49cb-95f5-97f8f87e3c77)

Pretty good considering such quick finetuning.

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

**Finetuned model spectrogram output using the librosa code**

https://github.com/user-attachments/assets/10c04417-212f-40fa-82fc-a51f07f5a8d2

It's a start I guess! :D 







