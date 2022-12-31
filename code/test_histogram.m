close all;clear all;clc;
I=imread('./image/Lenna_gray_gaussian.png');
img=im2gray(I);%转换为灰度像素
array = myGrayHistogram(img);
[m,n] = size(img);
sum=n*m;
p=array/sum;%统计频率
figure;
bar(array),title('灰度像素图');
figure,bar(p),title('归—化');

