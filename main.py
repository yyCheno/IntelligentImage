import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft2,fftshift
from PIL import Image

def my_rotate(im):
    #原始图像
    #画图
    plt.imshow(im,cmap='gray')
    plt.savefig("figure/original.png")
    plt.close()
    #
    im_fft2 = fft2(im)
    im_fftshift = fftshift(abs(im_fft2))
    plt.imshow(im_fftshift,cmap='gray')
    plt.savefig("figure/original_spectrum.png")
    plt.close()


    im_image = Image.fromarray(im)
    im_90 = im_image.rotate(45)
    im_90_bak = im_image.rotate(45)
    if im_90_bak.mode == "F" or im_90_bak.mode == "P":
        im_90_bak = im_90_bak.convert('RGB')
    im_90_bak.save("figure/90.png")
    im_90 = np.asarray(im_90)
    im_90_fft2 = fft2(im_90)
    im_90_fftshift = fftshift(abs(im_90_fft2))
    plt.imshow(im_90_fftshift,cmap='gray')
    plt.savefig("figure/90_spectrum.png")
    plt.close()

im = np.zeros((256,256))
im[80:180,80:180] = 255
my_rotate(im=im)