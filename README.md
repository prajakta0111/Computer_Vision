# Computer Vision

## Lab 2

The aim of this Lab assignment was to make a Hybrid Image from two different images in Fourier space. The input images I chose are:

![Monkey](https://github.com/prajakta0111/Computer_Vision/blob/master/lab2/monk.png)

![Lion](https://github.com/prajakta0111/Computer_Vision/blob/master/lab2/final_lion.jpg)

The first step is to convert the images in grayscale. And further, perform FFT on them. The images below are their repective FFTs.

![Monkey1](https://github.com/prajakta0111/Computer_Vision/blob/master/lab2/fft1.png)

![Lion1](https://github.com/prajakta0111/Computer_Vision/blob/master/lab2/fft2.png)

After obtaining these FFTs, I created a low pass where only pixels included in a 50 pixel radius will be chosen from one image, and for high pass filter, the pixels not belonging to the circle area from the second image will be chosen. Together they will form a new Hybrid image which is the task at hand. After performing this once, I swapped the swapped the images to be sent to the low pass and high pass filter as a result of which we get another Hybrid image.

Although, these images are still in FFT form, hence we perform Inverse FFT on them. The produced Hybrid Images can be seen below.


![Hybrid1](https://github.com/prajakta0111/Computer_Vision/blob/master/lab2/hybrid1.png)

![Hybrid2](https://github.com/prajakta0111/Computer_Vision/blob/master/lab2/hybrid2.png)
