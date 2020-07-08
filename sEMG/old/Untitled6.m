clc; clear all; close all; 
load('tabla_comparacion_T5_T17.mat'); 
dummy = [tabla_comparacion_T5_T17{1},tabla_comparacion_T5_T17{2},tabla_comparacion_T5_T17{3},...
         tabla_comparacion_T5_T17{4},tabla_comparacion_T5_T17{5},tabla_comparacion_T5_T17{6}];
sujeto1_tablacomp = dummy';
label = {'T5';'T17';'T5'; 'T17'; 'T5';'T17';'T5';'T17';'T5';'T17';'T5';'T17';
         'T5';'T17';'T5'; 'T17'; 'T5';'T17';'T5';'T17';'T5';'T17';'T5';'T17';
         'T5';'T17';'T5'; 'T17'; 'T5';'T17';'T5';'T17';'T5';'T17';'T5';'T17';
         'T5';'T17';'T5'; 'T17'; 'T5';'T17';'T5';'T17';'T5';'T17';'T5';'T17';
         'T5';'T17';'T5'; 'T17'; 'T5';'T17';'T5';'T17';'T5';'T17';'T5';'T17';
         'T5';'T17';'T5'; 'T17'; 'T5';'T17';'T5';'T17';'T5';'T17';'T5';'T17'};

%Cargar la data y poner Labels
sD = som_data_struct(sujeto1_tablacomp); 
sD.labels = label;

% Normalizar la data
% Altos valores atípicos afectan la medida de pesos
% sD = som_normalize(sD,'var');
sM = som_make(sD,'msize',[7,7]);
sM = som_autolabel(sM,sD);
som_show(sM,'umat','all','empty','Labels','norm','d');
som_show_add('label',sM,'subplot',2);

%  U-maps y labels
%% 
som_show(sM,'umat','all','empty','Labels')
som_show_add('label',sM,'Textsize',8,'TextColor','r','Subplot',2)


%% Para mostrar el mapa en 3D
% subplot(2,2,2)
 Co=som_unit_coords(sM); U=som_umat(sM); U=U(1:2:size(U,1),1:2:size(U,2));
som_grid(sM,'Coord',[Co, U(:)],'Surf',U(:),'Marker','none');
 view(-80,45), axis tight, title('Distance matrix')

%% Más mapas por jugar 


% subplot(2,2,3) % Grillas que cambian con el tamaño para separar
% som_cplane(sM,'none',1-Um(:)/max(Um(:)))
% title('D-matrix (marker size)')

% Similariaad por color 
% subplot(2,2,4)
C = som_colorcode(Pm);  % Pm is the PC-projection calculated earlier
som_cplane(sM,C)
drawnow;
title('Similarity coloring')

%% Trayectoria

Dtraj = [linspace(9,2,20); linspace(0,2,20); linspace(0,2,20)]';
T = som_bmus(sM,Dtraj);

som_show(sM,'comp',[1 1]);
som_show_add('traj',T,'Markercolor','r','TrajColor','r','subplot',1);
som_show_add('comet',T,'MarkerColor','r','subplot',2);
