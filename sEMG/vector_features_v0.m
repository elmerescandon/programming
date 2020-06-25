%% Obtención de segmentos para Clasificación
% Sujetos: 
% K_max = 6/8
% Sujetos: 2,3,8,14,15,16,17,19,21,22,25,27,30,33,40
% Electrodo = 12 (Triceps)

clc; clear all; close all; 
load(fullfile('C:','Users','raul_','programming',...
    'Analysis of sEMG signals with Multifractal Characteristics',...
    'Sujetos','S3_EJ_AB'));

sujetos = [2,3,8,14,15,16,17,19,21,22,25,27,30,33,40];
electrodo = 12; 
task = [5,17]; 

tabla_comparacion_T5_T17 = cell(1,length(sujetos));

% Cada celda está compuesta por los segmentos de la tarea de un sujeto 
% Estos segmentos están en el siguiente orden 
% T5R1,T17R1 / T5R2,T17R2 / T5R3,T17R3 / T5R4,T17R4 / T5R5,T17R5 /
% T5R6,T17R6

for n = 1:length(sujetos)
    
    % Inicializar la variable 
    str_var = strcat('S',int2str(sujetos(n)),'_EJ_AB');
    str_load = strcat(str_var,'.mat');
    load(fullfile('C:','Users','raul_','programming',...
    'Analysis of sEMG signals with Multifractal Characteristics',...
    'Sujetos',str_load));

    funct = strcat('temp=',str_var,';');
    eval(funct);
    disp("Sujeto " + int2str(uint8(sujetos(n))));
    % Evaluar los valores
    for m = 2:7
        % Agarrar Tarea 5 y 17  / S3_EJ_AB{2,2}(:,12)
        % ventanadoFDH_v2(x,n_seg,t_w,k_max)
        
        % Concatenar todas las reps
        for p = 1:2 
            disp(size(ventanadoFDH_v2(temp{task(p),m}(:,12),25,0.25,6)'))
            tabla_comparacion_T5_T17{n} = [tabla_comparacion_T5_T17{n},...
                        ventanadoFDH_v2(temp{task(p),m}(:,12),25,0.25,6)'];
        end  
    end
end