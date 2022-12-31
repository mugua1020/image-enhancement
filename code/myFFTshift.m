function [ after ] = myFFTshift( before )
    h = size(before, 1);
    w = size(before, 2);

    after = before;

    if power(2, log2(h)) ~= h || power(2, log2(w)) ~= w
        disp('FFTshift exit: h and w must be the power of 2!')
    else
        hh = h / 2;
        hw = w / 2;
        after(1 : hh, 1 : hw) = before(hh + 1 : h, hw + 1 : w);
        after(1 : hh, hw + 1 : w) = before(hh + 1 : h, 1 : hw);
        after(hh + 1 : h, 1 : hw) = before(1 : hh, hw + 1 : w);
        after(hh + 1 : h, hw + 1 : w) = before(1 : hh, 1 : hw);
    end
end