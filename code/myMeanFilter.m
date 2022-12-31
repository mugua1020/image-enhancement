function [out] = myMeanFilter(img, K_size)
    [h, w] = size(img);

    % 零填充
    pad = mod(K_size, 2);
    out = zeros(h+2*pad, w+2*pad);
    out(pad+1:pad+h, pad+1:pad+w) = double(img);

    % 均值滤波核
    K = ones(K_size, K_size);
    K = K/sum(K, 'all');

    % 开始卷积
    tmp = out;
    for y = 1:h
        for x = 1:w
            out(pad+y, pad+x) = sum(K.*tmp(y:y+K_size-1, x:x+K_size-1), 'all');
        end
    end
    
    out = uint8(out(pad+1:pad+h, pad+1:pad+w));