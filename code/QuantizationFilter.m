fs = 44100; %采样频率，这里按照音频来处理
fpass = 4000;  %通带边界频率
wp = 2*pi*fpass/fs;  % 待设计的模拟滤波器的边界频率
fstop = 16000; 
ws = 2*pi*fstop/fs;
pr = 0.01;  %通带纹波
sr = 80;    %阻带纹波
[N,wn]=buttord(wp,ws,pr,sr,'s');   % 滤波器的阶数、截止频率
[b,a]=butter(N,wn,'s');            % 传递函数
[bz,az]=bilinear(b,a,0.5);         % 利用双线性变换实现频率响应S域到Z域的变换

qpath2 = quantizer('fixed','round','saturate',[16,8]); % 共16位保留12位小数(二进制),精度2^(-20)
b_quan = quantize(qpath2,bz);
a_quan = quantize(qpath2,az);

subplot(1,2,1);
[h,w]=freqz(bz,az);
title('未量化的IIR低通滤波器');
plot(w*fs/(2*pi),abs(h));

subplot(1,2,2);
[h_q,w_q]=freqz(b_quan,a_quan);
title('量化后IIR低通滤波器');
plot(w_q*fs/(2*pi),abs(h_q));