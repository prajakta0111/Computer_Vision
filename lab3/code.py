from PIL import Image
from PIL import ImageDraw
import numpy as np
import imageio
import copy

def check_range(x): return np.min(x), np.max(x)

def display_np(x):
    """
    Display a numpy array as an image
    """
    result = Image.fromarray(x.astype('uint8'))
    result.show()

def normalize(output):
    base = np.min(output)
    roof = np.max(output)
    diff = roof - base
    scale = diff/255
    output = output - base
    output = output / scale
    return output
    
image1 = Image.open("input.jpg").convert('L')
image_arr = np.array(image1)

#this function code is referrenced from the first group assignment
def conv1d(image, kernel):
    """
    Performs 1d convolution on an image
    """
    
    im = copy.deepcopy(image.flatten())
    k = copy.deepcopy(kernel.flatten())

    size = len(k)
    to_remove = len(k) - 1
    
    output = np.full((im.shape), 255)
    for i in range(len(im) - to_remove):
        output[i] = np.sum(k * im[i:i+size])
    
#     print(check_range(output))
    output = normalize(output)
#     print(check_range(output))

    output = output.reshape(image.shape[0],image.shape[1])
    return output

#this function code is referrenced from the first group assignment
def conv2d(image, kernel):
    """
    Applies 2d convolution on a 2d image. Also works with rectangular kernels
    """

    # number of rows and columns of the kernel
    r = kernel.shape[0]
    c = kernel.shape[1]

    # initialize a canvas for the output with 255s. We will fill values in this
    output = np.full(image.shape, 255)
    for i in range(image.shape[0] - r - 1):
        for j in range(image.shape[1] - c - 1):
            output[i][j] = np.sum(kernel * image[i:i+r, j:j+c])
    output = normalize(output)
    return output

kernel2d = np.array([[1,1,1],[1,1,1],[1,1,1]])
kernel1= np.array([-1,1])
# kernel1.shape


Ix = conv1d(image_arr,kernel1)
Iy = np.transpose(conv1d(np.transpose(image_arr),kernel1))

Ix2 = normalize(Ix*Ix)
Ixy = normalize(Ix*Iy)
Iy2=normalize(Iy*Iy)
imageio.imsave('Ix.png',Ix)
imageio.imsave('Iy.png',Iy)
imageio.imsave('Ix2.png',Ix2)
imageio.imsave('Ixy.png',Ixy)
imageio.imsave('Iy2.png',Iy2)

Aw = conv2d(Ix2,kernel2d)
Bw = conv2d(Ixy,kernel2d)
Cw = conv2d(Iy2,kernel2d)


T = 6
im = Image.open( "input.jpg")
draw = ImageDraw.Draw(im)
for x in range(image1.size[0]):
    for y in range(image1.size[1]):
        e_values , e_vectors = np.linalg.eig(np.array([[Aw[y][x],Bw[y][x]],[Bw[y][x],Cw[y][x]]]))
        
        if (np.min(e_values) > T):
            draw.line(((x-5,y),(x+5,y)),fill = (255,0,0))
            draw.line(((x, y-5),(x,y+5)),fill= (255,0,0))
imageio.imsave('output.png',im)
