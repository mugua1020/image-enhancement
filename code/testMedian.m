close all;clear all;clc;
I=imread('./image/Lenna_gray_sp.png');
img=im2gray(I);%转换为灰度像素
result = medfilt2(img,[3,3]);
my = myMedianFilter(img, 3);
subplot(1,2,1);imshow(result,[]);title('result');
subplot(1,2,2);imshow(my,[]);title('my');