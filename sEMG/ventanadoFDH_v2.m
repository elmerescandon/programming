%% Overlapping y Segmentación 
function [ventanas]=ventanadoFDH_v2(x,n_seg,t_w,k_max)
    % Función que retorna la dimensión fractal de Hicuhi
    % Inputs: 
       % K_max(int) = Segmento variables de Higuchi
       % x(int 1D array) = Señal
       % n_seg (int) = Número de segmentos deseados
       % t_w = Tiempo del segmento   

    % Segmentación 
    freq = 2000; %(Hz)
    % Las tareas 5 y 17 en promedio duran eso
    pseudo_n_seg = n_seg +1; 
    ventanas = zeros(1,n_seg);
    
    % Tiempo 
    t_x = length(x)/freq; % Señal
    t_o = t_w - t_x/(pseudo_n_seg+1); % Overlapping Dinámico
    
    for i = 1:(pseudo_n_seg-1)
        n = floor(((i-1)*(t_w-t_o))*freq) + 1 ;
        m = n + floor(t_w*freq) - 1;
        if i == (pseudo_n_seg-1) 
            dummy = x(n:end);
        else 
            dummy = x(n:m);
        end
        ventanas(i) = Higuchi_FD(dummy,k_max);
    end
end
