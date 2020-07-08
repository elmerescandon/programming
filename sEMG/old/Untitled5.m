clc; clear all; close all; 
x = linspace(0,1,3326);
freq = 2000;
t_w = 0.25;
n_seg = 25; 

ps_seg = n_seg + 3;
ventanas = zeros(1,n_seg);

t_x_pts = length(x); 
t_w_pts = t_w*freq;
t_o_pts = floor(t_w_pts - t_x_pts/(ps_seg+1));

t_o = t_o_pts/freq;
t_w = t_w_pts/freq;


for i = 1:(ps_seg-3)
    n = floor(((i-1)*(t_w-t_o))*freq) + 1 ;
    m = n + floor(t_w*freq) - 1;
    if i == (ps_seg-1) 
        dummy = x(n:end);
    else 
        dummy = x(n:m);
    end
    ventanas(i) = mean(dummy);  %Higuchi_FD(dummy,k_max);
end

%% 

sujetos = [2,3,8,14,15,16,17,19,21,22,25,27,30,33,40];
sujeto2 = [1,4,6,7,11,12,18,20,23,26,32,31,37,38,39];