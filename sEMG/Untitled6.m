clc; clear all; close all; 
load('tabla_comparacion_T5_T17.mat'); 

dummy = [];
for a = 1:length(tabla_comparacion_T5_T17)
    dummy = [dummy,tabla_comparacion_T5_T17{a}];
end

dummy = dummy';
%% 
clc; clear all; close all; 
load('tabla_comparacion_T5_T17.mat'); 

dummy = tabla_comparacion_T5_T17{4};

dummy = dummy';