close all;clear all;clc;
I=imread('./image/Lenna_gray_gaussian.png');
img=im2gray(I);%转换为灰度像素
result = imgaussfilt(img,1.3, FilterSize=3);
my = myGaussianFilter(img, 1.3, 3);
subplot(1,2,1);imshow(result,[]);title('result');
subplot(1,2,2);imshow(my,[]);title('my');
