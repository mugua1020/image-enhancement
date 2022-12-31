close all;clear all;clc;

M =128;
N =128;
D0 = 20;
n = 3;
H1 = myLPFilter('ideal', M, N, D0, n);
H2 = myLPFilter('btw', M, N, D0, n);
H3 = myLPFilter('gaussian', M, N, D0, n);

surf(myFFTshift(H3));
