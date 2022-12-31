function H = myLPFilter(type, M, N, D0, n)
%   lowpass filter.
%   H = LPFILTER(TYPE, M, N, D0, n) creates the transfer function of
%   a lowpass filter, H, of the specified TYPE and size (M-by-N). To
%   view the filter as an image or mesh plot, it should be centered
%   using H = fftshift(H). 

% Use function dftuv to set up the meshgrid arrays needed for
% computing the required distances. 
[U, V] = dftuv(M, N);

% Compute the distances D(U, V).
D = sqrt(U.^2 + V.^2);

% Begin filter computations.
switch type
case 'ideal'                            %理想低通滤波器
   H = double(D <= D0);
case 'btw'                              %巴特沃兹低通滤波器
   if nargin == 4
      n = 1;    
   end
   H = 1./(1 + (D./D0).^(2*n));
case 'gaussian'                         %高斯低通滤波器
   H = exp(-(D.^2)./(2*(D0^2)));
otherwise
   error('Unknown filter type.')
end
