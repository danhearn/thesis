# Thesis

## Spectrogram Testing

<img src="/cw_amen05_158_spectrogram_512x512.png">

Some scripts testing out spectrograms at 512*512, which is the same size as the realtime image output from stream diffusion. 

Overall, audio up to 10 seconds sounds very good. As you go over this threshold, the sound is noticably bitty and clippy, starting with the lower frequencies. This is because the frequency bin size is 1 pixel. As the output image size is limited to 512, longer audio clips are squashed, therefore audio information overtime is lost. 

John Belfram's Ten Days of Blue was cut from 1:14 into audio segements ranging from 2 to 30 seconds to test how the audio performed overtime. This song was chosen it is similar in style to the desired output. 


We now have a tool to generate a dataset of 512x512 spectrograms from audio. And have successfully determined that for 512x512 model output, the maximum audio length should be 10 seconds for generation of spectrograms.