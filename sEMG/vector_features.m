function [tabla_comparacion] = vector_features(sujetos,task,electrodo,k_max,segmentos,tiempo_seg)
    % Obtención de segmentos para Clasificación
    % Sujetos: 
    % K_max = 6/8
    % Sujetos: 2,3,8,14,15,16,17,19,21,22,25,27,30,33,40
    % Electrodo = 12 (Triceps)
    % Taks = vector de tareas a comparar

    % Ejemplos:
    % k_max = 6
    % task = [5,17]
    % sujetos = [2,3,8,14,15,16,17,19,21,22,25,27,30,33,40];
    % Segmentos = 25
    % tiempo_seg = 0.25
    tabla_comparacion = cell(1,length(sujetos));

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
        % disp("Sujeto " + int2str(uint8(sujetos(n))));
        % Evaluar los valores
        for m = 2:7
            % Concatenar todas las repeticiones
            for p = 1:length(task)
                %disp(size(ventanadoFDH_v2(temp{task(p),m}(:,12),25,0.25,k_max)'))
                tabla_comparacion{n} = [tabla_comparacion{n},...
                            ventanadoFDH_v2(temp{task(p),m}(:,electrodo),segmentos,tiempo_seg,k_max)'];
            end  
        end
    end
end

