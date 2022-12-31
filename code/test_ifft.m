pic1 = imread("./image/Lenna_gray.png");
pic1 = im2gray(pic1);
pic1_fft = myFFT2(double(pic1));
myFc = myFFTshift(pic1_fft);
myS2 = log(1+abs(myFc));

result = fft2(double(pic1));
Fc = fftshift(result);
S2 = log(1+abs(Fc));

myRF = myIFFTshift(myFc);
mypic = uint8(myIFFT2(myRF));

RF = ifftshift(Fc);
pic = uint8(ifft2(RF));

subplot(2,2,1);imshow(real(myFc),[]);title('myS2');
subplot(2,2,2);imshow(real(Fc),[]);title('S2');
subplot(2,2,3);imshow(mypic, []);title('mypic');
subplot(2,2,4);imshow(pic, []);title('pic');
% pic1_fft_amp = abs(pic1_fft);
% pic1_fft_amp_log = log(1 + pic1_fft_amp);
% imshow(log(1+abs(result)));