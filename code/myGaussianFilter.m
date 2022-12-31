function [out] = myGaussianFilter(img, sigma, K_size)
    [h, w] = size(img);

    % 零填充
    pad = mod(K_size, 2);
    out = zeros(h+2*pad, w+2*pad);
    out(pad+1:pad+h, pad+1:pad+w) = double(img);

    % 定义滤波核
    K = zeros(K_size, K_size);
    for x = 1-pad:K_size-pad
        for y = 1-pad:K_size-pad
            K(y+pad, x+pad) = exp(-((x-1)^2 + (y-1)^2)/(2*(sigma^2)));
        end
    end
    K = K/(sigma*sqrt(2*pi));
    K = K/sum(K, 'all');

    % 开始卷积
    tmp = out;
    for y = 1:h
        for x = 1:w
            out(pad+y, pad+x) = sum(K.*tmp(y:y+K_size-1, x:x+K_size-1), 'all');
        end
    end
    
    out = uint8(out(pad+1:pad+h, pad+1:pad+w));


