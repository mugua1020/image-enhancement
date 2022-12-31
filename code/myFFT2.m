function [ mfft2 ] = myFFT2( data )
    h = size(data, 1);
    w = size(data, 2);
    mfft2 = data;

    if power(2, log2(h)) ~= h || power(2, log2(w)) ~= w
        disp('myFFT2 exit: h and w must be the power of 2!')
    else
        for i = 1 : h
            mfft2(i, :) = fft(mfft2(i, :));
        end

        for j = 1 : w
            mfft2(:, j) = fft(mfft2(:, j));
        end
    end
end

