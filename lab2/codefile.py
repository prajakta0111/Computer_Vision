from PIL import Image
from PIL import ImageDraw
import numpy as np
from scipy import fftpack
import imageio
from PIL import ImageOps

image1 = Image.open('monk.png').convert("L")
image2 = Image.open('final_lion.jpg').convert("L")

image1,image2 = np.array(image1),np.array(image2)

def resize_image(img1,img2):
    temp_canvas = np.zeros((img2.shape[0],img2.shape[1]))
    a = (image2.shape[0]-image1.shape[0])//2
    b = (image2.shape[1]-image1.shape[1])//2
    temp_canvas[a:a+img1.shape[0],b:b+img1.shape[1]] = img1
    return temp_canvas

new=resize_image(image1,image2)

fft2_1 = fftpack.fftshift(fftpack.fft2(new))
fft2_2 = fftpack.fftshift(fftpack.fft2(image2))

imageio.imsave('fft1.png', (np.log(abs(fft2_1))* 255 /np.amax(np.log(abs(fft2_1)))).astype(np.uint8))
imageio.imsave('fft2.png', (np.log(abs(fft2_2))* 255 /np.amax(np.log(abs(fft2_2)))).astype(np.uint8))

fourier1 = Image.open('fft1.png').convert("L")
fourier2 = Image.open('fft2.png').convert("L")
x,y = fourier1.size
eX , eY = 50 , 50
bbox = ( x/2 - eX / 2 , y/2 - eY / 2 , x /2 + eX / 2 , y /2 + eY / 2 )
low_pass = Image.new( "L" , (fourier1.width , fourier1.height) , color =255)
draw = ImageDraw.Draw( low_pass )
draw.ellipse( bbox , fill =0)
low_pass = np.array(low_pass)
# high_pass = Image.new( "L" , (fourier1.width , fourier1.height) , color =0)
# draw = ImageDraw.Draw( high_pass )
# draw.ellipse( bbox , fill =255)
low_pass = np.array(low_pass)
# high_pass = np.array(high_pass)
fourier1,fourier2 = np.array(fourier1),np.array(fourier2)

def make_hybrid(f1,f2):
    canvas = np.zeros((f1.shape[0],f1.shape[1]),dtype=complex)
    for i in range(0,f1.shape[0]):
        for j in range(0,f1.shape[1]):
            if low_pass[i,j]==0:
                canvas[i,j]+=f1[i,j]
            else:
                canvas[i,j]+=f2[i,j]

    return canvas
        
hybrid_image1 = make_hybrid(fft2_1,fft2_2)
hybrid_image2 = make_hybrid(fft2_2,fft2_1)

ifft1 = abs(fftpack.ifft2(fftpack.ifftshift(hybrid_image1)))
ifft2 = abs(fftpack.ifft2(fftpack.ifftshift(hybrid_image2)))

imageio.imsave('hybrid1.png', ifft1.astype(np.uint8))
imageio.imsave('hybrid2.png', ifft2.astype(np.uint8))