f = imread('./image/try.png');
f = im2gray(f);
F = fft2(f);%傅里叶变换,逆变换为 f=ifft2(F),取实部为 f=real(ifft2(F))

S = abs(F);%傅里叶频谱

Fc = fftshift(F);%将变换的原点移动到频率矩阵的中心,反变换为 F=ifftshift(Fc),
%频率矩阵中心点位于[floor(M/2)+1,floor(N/2)+1]
S2 = log(1+abs(Fc)); %对数变换

subplot(2,2,1);imshow(f);title('简单图像');
subplot(2,2,2);imshow(S,[ ]);title('傅里叶频谱');
subplot(2,2,3);imshow(abs(Fc),[ ]);title('居中的频谱');
subplot(2,2,4);imshow(S2,[ ]);title('对数变换后视觉增强的图像');
