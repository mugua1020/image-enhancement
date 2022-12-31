function [counts] = myGrayHistogram(image)
    %默认对灰度图像，并且为256深度
    counts = zeros(1,256);
    [m,n]=size(image);
    for i=1:m
        for j=1:n
            counts(image(i,j)+1) = counts(image(i,j)+1)+1;
        end
    end
    