function [out] = NotchFilter(img, Fq)
    [h,w] = size(img);
    out = zeros(h, w);

    for i = 1:h
        for j = 1:w
            out(i,j) = img(i,j) - Fq*(sin(Fq*(i-1)) + sin(Fq*(j-1)));
        end
    end
    