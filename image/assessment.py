import cv2
from skimage.metrics import structural_similarity as ssim
import numpy as np
import math

class StructureSimComp(object):
    def __init__(self,w=512,h=512,win_size =7):
        self.h = h
        self.w = w
        self.rsz = 0
        self.C1 = 6.5025
        self.C2 = 58.5225
        self.filterSize = win_size
        #if filterX = 0 then opencv inner use : filterX = 0.3*((filterSize-1)*0.5 - 1) + 0.8
        self.filterX = 0
    def run(self, imgx, imgy):
        # https://docs.opencv.org/2.4/doc/tutorials/highgui/video-input-psnr-ssim/video-input-psnr-ssim.html
        # https://blog.csdn.net/chaipp0607/article/details/70158835
        imgx = cv2.resize(imgx, (self.w, self.h), interpolation=self.rsz)
        imgy = cv2.resize(imgy, (self.w, self.h), interpolation=self.rsz)
        # imgx sqr
        X_2 = cv2.multiply(imgx, imgx, dtype=cv2.CV_32F)
        # imgy sqr
        Y_2 = cv2.multiply(imgy, imgy, dtype=cv2.CV_32F)
        # imgx_imgy
        X_Y = cv2.multiply(imgx, imgy, dtype=cv2.CV_32F)
        mu1 = cv2.GaussianBlur(imgx, (self.filterSize, self.filterSize), self.filterX)#GaussianBlur()函数用高斯滤波器（GaussianFilter）对图像进行平滑处理。
        mu2 = cv2.GaussianBlur(imgy, (self.filterSize, self.filterSize), self.filterX)
        # mul1 sqr
        mu1_2 = cv2.multiply(mu1, mu1, dtype=cv2.CV_32F)
        # mul2 sqr
        mu2_2 = cv2.multiply(mu2, mu2, dtype=cv2.CV_32F)
        # mul1 mul2
        mu1_mu2 = cv2.multiply(mu1, mu2, dtype=cv2.CV_32F)
        sigma1_2 = cv2.GaussianBlur(X_2, (self.filterSize, self.filterSize), self.filterX)
        sigma2_2 = cv2.GaussianBlur(Y_2, (self.filterSize, self.filterSize), self.filterX)
        sigma12 = cv2.GaussianBlur(X_Y, (self.filterSize, self.filterSize), self.filterX)
        sigma1_2 -= mu1_2
        sigma2_2 -= mu2_2
        sigma12 -= mu1_mu2
        t1 = 2 * mu1_mu2 + self.C1
        t2 = 2 * sigma12 + self.C2
        t3 = cv2.multiply(t1, t2, dtype=cv2.CV_32F)

        t1 = mu1_2 + mu2_2 + self.C1
        t2 = sigma1_2 + sigma2_2 + self.C2
        t1 = cv2.multiply(t1, t2, dtype=cv2.CV_32F)
        resMap = cv2.divide(t3,t1,dtype=cv2.CV_32F)
        r = cv2.mean(resMap)
        res = abs((r[0] + r[1] + r[2])/3.0)
        return res


def MSE(img1,img2):
    mse = np.mean( (img1 - img2) ** 2 )
    return mse


def PSNR(img1, img2):
    mse = np.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def print_result(Image1_path, Image2_path):
    image1 = cv2.imread(Image1_path)
    image2 = cv2.imread(Image2_path)
    SSIM = StructureSimComp()
    result = SSIM.run(image1, image2)
    print("the SSIM of this two picture is {}%".format(result*100))
    print("the MSE of this two picture is {}".format(MSE(image1, image2)))
    print("the PSNR of this two picture is {}%".format(PSNR(image1, image2)))


if __name__ == "__main__":
    Image1_path = ["Cat_gray.jpg"]
    Image2_path = ["Cat_gray_cycle.jpg"]
    for i in range(1):
        print_result(Image1_path[i], Image2_path[i])
    
