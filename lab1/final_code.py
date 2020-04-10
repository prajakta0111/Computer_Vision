from PIL import Image
import numpy as np
import copy
orig = Image.open("original.jpg")
iden=np.array([[0,0,0],[0,1,0],[0,0,0]])
blur=np.array([[1,1,1],[1,1,1],[1,1,1]])/9
horiz=np.array([[0,0,0],[-1,0,1],[0,0,0]], dtype=np.float64)
gaus=np.array([[0.003,0.013,0.022,0.013,0.003],[0.013,0.059,0.097,0.059,0.013],[0.022,0.097,0.159,0.097,0.022],[0.013,0.059,0.097,0.059,0.013],[0.003,0.013,0.022,0.013,0.003]])

alpha = 0.92
e = np.zeros((5,5))
e[2,2]=1
e = (1+alpha) * e
e = e - gaus
def display_image(x,n):
    x = Image.fromarray(x)
    x.save(n)

def filter3(image, filterm):
    pix = np.array(image)
    canvas = np.zeros(pix.shape)
    for i in range(pix.shape[2]):
        for h in range(pix.shape[0]-2):
            for w in range(pix.shape[1]-2):

                inter = pix[h:h+3,w:w+3,i]*filterm
                canvas[h+1][w+1][i] = np.sum(inter)

    canvas=np.clip(canvas,0,255)
    return canvas

def filter5(image, filterm):
    pix = np.array(image)
    canvas = np.zeros(pix.shape)
    for i in range(pix.shape[2]):
        for h in range(pix.shape[0]-4):
            for w in range(pix.shape[1]-4):
                inter = pix[h:h+5,w:w+5,i]*filterm
                canvas[h+1][w+1][i] = np.sum(inter)
    canvas=np.clip(canvas,0,255)
    return canvas

ident = filter3(orig, iden)
display_image(ident.astype('uint8'),"Identity.jpg")
blurry = filter3(orig, blur)
display_image(blurry.astype('uint8'),"Blurry.jpg")
hor = filter3(orig, horiz)
display_image(hor.astype('uint8'),"Horizontal.jpg")
gauss=filter5(orig,gaus)
display_image(gauss.astype('uint8'),"Gaussian.jpg")
deriv=filter5(hor,gaus)
display_image(deriv.astype('uint8'),"Gaussian_derivate.jpg")
sharp=filter5(orig,e)
display_image(sharp.astype('uint8'),"Sharpening.jpg")