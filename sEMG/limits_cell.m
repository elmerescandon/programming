function [index_cluster] = limits_cell(map,C,cluster_evaluar)
    % Input: 
    % Cell array que contiene n vectores con posición (cell-array)
    % Tamaño del mapa (vector)
    % Cluster general
    % Output: 
    % Vecinos que rodean al vector grupo (matriz de vectores)
    dummy =[]; 
    C_eval = C{cluster_evaluar};
    for n = 1:size(C_eval,1)
        pos = C_eval(n,:);
        [lims] = limits(pos,map);
        dummy =[dummy;lims];
    end
    final_limits = unique(dummy,'rows'); 
%     disp(final_limits);
    
    index_cluster = [];
    % Si el cluster evlauado no correponde al que se desea
    % Y por lo menos existe un vecino, entonces se escoge
    for m = 1:length(C)
        
        if m~=cluster_evaluar
            if ~isempty(find(ismember(C{m},final_limits,'rows')))
                %disp(find(ismember(C{m},final_limits,'rows')))
                index_cluster = [index_cluster,m];
            end 
        end
    end
       
end