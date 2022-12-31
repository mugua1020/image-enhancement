close all;clear all;clc;
pic1 = imread("./image/Lenna_gray.png");
pic1 = im2gray(pic1);
pic1_fft = myFFT2(double(pic1));
D0 = 20;
[M, N] = size(pic1);
[U, V] = dftuv(M, N);
D = sqrt(U.^2 + V.^2);
H1 = double(D <= D0);
H2 = double(D > D0);

result1 = pic1_fft.*H1;
result1 = myIFFT2(result1);
result1 = uint8(real(result1));
imwrite(result1, 'result1_low.png');

result1 = pic1_fft.*H2;
result1 = myIFFT2(result1);
result1 = uint8(real(result1));
imwrite(result1, 'result2_low.png');

% imwrite(img,'result.jpg')