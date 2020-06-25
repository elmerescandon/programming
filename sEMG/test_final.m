%% Obtención de valores de comparación Higuchi
% sujetos = [2,3,8,14,15,16,17,19,21,22,25,27,30,33,40];
% task = [5,17]
% electrodo = 12
% k_max = 6
% segmentos = 25
% tiempo_seg = 0.25

% tabla_comp = vector_features(sujetos,tareas,electrodo,k_max,segmentos,tiempo_seg);
 
%% Clasificación mediante SOM 
clc; clear all; close all; 
load('tabla_comparacion_T5_T17.mat');


sample = tabla_comparacion_T5_T17{5};