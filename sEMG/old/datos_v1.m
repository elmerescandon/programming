%% Obtener igual valor de segmentos
% Se modificará la señal de mayor tiempo
clc; clear all; close all; 
load(fullfile('C:','Users','raul_','programming',...
    'Analysis of sEMG signals with Multifractal Characteristics',...
    'Sujetos','S3_EJ_AB'));

% Características de la señal
freq = 2000; %(Hz)
n = 25; % Las tareas 5 y 17 en promedio duran eso
t_w = 0.25; % Tiempo de segmentación 

for a = 2:7
    x = S3_EJ_AB{5,a}(:,1); % Cargar señal
    t_x = length(x)/freq; % Tiempo de señal
    
    t_o = t_w - t_x/n; % Tiempo de Overlapping 
    disp("Tiempo de overlapping: " + num2str(t_o))
    
    num_win = t_x/(t_w-t_o); % Segmentación de ventanas
    disp("Num. ventanas: " + num2str(num_win))
    
end

%% Segmentación - Modificarla para que todas tengan 25 segmentos
% Exclusivo para las tareas 5 y 17 
clc; clear all; close all; 
load(fullfile('C:','Users','raul_','programming',...
    'Analysis of sEMG signals with Multifractal Characteristics',...
    'Sujetos','S3_EJ_AB'));
% Segmentación 
freq = 2000; %(Hz)
n_seg = 26; % Las tareas 5 y 17 en promedio duran eso
t_w = 0.25; % Tiempo de segmentación 
ventanas = zeros(1,25);

x = S3_EJ_AB{5,2}(:,1); % Cargar señal
t_x = length(x)/freq; % Tiempo de señal
t_o = t_w - t_x/(n_seg+1); % Tiempo de Overlapping 

num_win = t_x/(t_w-t_o) - 1;

for i = 1:(n_seg-1)
    n = floor(((i-1)*(t_w-t_o))*freq) + 1 ;
    m = n + floor(t_w*freq) - 1;
    dummy = x(n:m);
    ventanas(i) = mean(dummy);
end


