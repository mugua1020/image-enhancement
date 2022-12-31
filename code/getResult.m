close all;clear all;clc;
pic1 = imread("./Lenna_gray_cycle_sp.png");
pic1 = im2gray(pic1);

K_size =3;
result1 = myMeanFilter(pic1, K_size);
imwrite(result1, 'result_mean.png');

result2 = myMedianFilter(pic1, K_size);
imwrite(result2, 'result_median.png');

sigma = 1.3;
result3 = myGaussianFilter(pic1, sigma, K_size);
imwrite(result3, 'result_gauss.png');

pic1_fft = myFFT2(double(pic1));
[M, N] = size(pic1);
D0 = M/5;
H =  myLPFilter('gaussian', M, N, D0, 0);
result4 = pic1_fft.*H;
result4 = myIFFT2(result4);
result4 = uint8(real(result4));
imwrite(result4, 'result_LF.png');

result5 = NotchFilter(pic1, 10);
result5 = myMedianFilter(result5, K_size);
imwrite(uint8(result5), 'result_Notch.png');
