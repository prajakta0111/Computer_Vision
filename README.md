# Computer Vision
## Lab 1
In this lab, we had to perform different convolutions on the input image from scratch. We performed the 3D convolutions using the following kernels and their respective outputs can be seen below:

### Original image:
![Original](https://github.com/prajakta0111/Computer_Vision/blob/master/lab1/original.jpg)
### Identity:
![Identity](https://github.com/prajakta0111/Computer_Vision/blob/master/lab1/Identity.jpg)
### Box BLur:
![Blurry](https://github.com/prajakta0111/Computer_Vision/blob/master/lab1/Blurry.jpg)
### Horizontal Derivative:
![Horizontal](https://github.com/prajakta0111/Computer_Vision/blob/master/lab1/Horizontal.jpg)
### Gaussian:
![Gaussian](https://github.com/prajakta0111/Computer_Vision/blob/master/lab1/Gaussian.jpg)
### Sharpening:
![Sharpening](https://github.com/prajakta0111/Computer_Vision/blob/master/lab1/Sharpening.jpg)
### Derivative of Gaussian
![Gaussian_derivative](https://github.com/prajakta0111/Computer_Vision/blob/master/lab1/Gaussian_derivate.jpg)

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

## Lab 3
In this lab we implement corner detection using Harris detector. The intermediate results are as shown below:
### Input image:
![Input](https://github.com/prajakta0111/Computer_Vision/blob/master/lab3/input.jpg)
### Derivative in x direction (Ix)
![Input](https://github.com/prajakta0111/Computer_Vision/blob/master/lab3/Ix.png)
### Derivative in y direction (Iy)
![Input](https://github.com/prajakta0111/Computer_Vision/blob/master/lab3/Iy.png)
### Ixy (Ix * Iy)
![Input](https://github.com/prajakta0111/Computer_Vision/blob/master/lab3/Ixy.png)
### Ix2 (Ix * Ix)
![Input](https://github.com/prajakta0111/Computer_Vision/blob/master/lab3/Ix2.png)
### Iy2 (Iy * Iy).
![Input](https://github.com/prajakta0111/Computer_Vision/blob/master/lab3/Iy2.png)
### Output (Corners marked with red crosses)
![Input](https://github.com/prajakta0111/Computer_Vision/blob/master/lab3/output.png)

## Lab 4

In this lab, we have a bunch of 3D points corresponding to a runway. We cast this on a 2D surface and simulate flight takeoff.
We can tune various parameters to make the plane twist, tilt, 360 rotations or show the rear view.
The way this is done is, by casting the 3D points to a 4D homogeneous surface and converting it back while plotting the points for the take-off simulation.
The transformation matrix is obtained from the equation below:

![Input](https://github.com/prajakta0111/Computer_Vision/blob/master/lab3/formula.png)

Checkout the [movie.mp4](https://github.com/prajakta0111/Computer_Vision/blob/master/lab4/movie.mp4) file to view the takeoff.

![Input](https://github.com/prajakta0111/Computer_Vision/blob/master/lab3/plane.png)
