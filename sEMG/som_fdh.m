function [sD,sM]=som_fdh(sujetos,task,k_max,electrodo)
    %,map_size)
    close all; 
    label = cell(6*length(task)*length(sujetos),1);

    for a = 1:length(sujetos)
        index_1 = (a-1)*6*length(task) + 1;
        for n = 1:6 
            for m = 1:length(task) 
               label{index_1} = strcat('T',num2str(task(m)));%,'R',num2str(n));
               index_1 = index_1 + 1; 
            end
        end
    end 
     % Por defecto para Experimento 3: 
     segmentos = 25;
     tiempo_seg = 0.25; 
%      electrodo = 12;
%      task = [5,17]; 
   
    % Obtener la tabla con los valores
    [tabla_comparacion] = vector_featuresv2(sujetos,task,electrodo,k_max,segmentos,tiempo_seg);
    
    sujeto_comp = tabla_comparacion';
    %Cargar la data y poner Labels
    sD = som_data_struct(sujeto_comp); 
    sD.labels = label;
    
    % Altos valores atípicos afectan la medida de pesos
    sM = som_make(sD);%,'msize',map_size);
    sM = som_autolabel(sM,sD);
    som_show(sM,'umat','all','empty','Labels','norm','d');
    som_show_add('label',sM,'subplot',2);
%     
%      figure(2)
%     Co=som_unit_coords(sM); U=som_umat(sM); U=U(1:2:size(U,1),1:2:size(U,2));
%     som_grid(sM,'Coord',[Co, U(:)],'Surf',U(:),'Marker','none');
%     view(-80,45), axis tight, title('Distance matrix')


    %  U-maps y labels
%     som_show(sMap,'umat','all','empty','Labels')
%     som_show_add('label',sMap,'Textsize',8,'TextColor','r','Subplot',2)

end

