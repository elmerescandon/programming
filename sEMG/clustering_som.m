function [C,sM,sD,positions,indexs_db] = clustering_som(sujetos,tareas,k_max,electrodo)
    % Ejemplo: [sD,sM]=som_fdh([30,3,5],[5,17],10,12);
    [sD,sM]=som_fdh(sujetos,tareas,k_max,electrodo);
    hits = sM.labels;
    map = sM.topol.msize;
    indexs_db = [];
    % subplot(1,2,1)
    % som_cplane('hexa',[10 15],'none')
    % title('Hexagonal SOM grid')

    neuron_grid = reshape(hits,[map(1),map(2),size(hits,2)]);
    weights_grid = reshape(sM.codebook,[map(1),map(2),size(sM.codebook,2)]); 

    % Consideraciones: 
        % Usar simple linkage 
        % Considerar solo los nodos adyacentes
        % Escoger el menor index de David

    % Paso 1: Reorganizar las neuronas como el mapa
    neuron_grid = reshape(hits,[map(1),map(2),size(hits,2)]);

    % Paso 2: Verificar qué neuronas las que se evaluarán
    positions = [];
    for n = 1:map(1)
        for m = 1:map(2)
            if ~(isempty(neuron_grid{n,m}))
                pos = [n,m];
                positions = [positions;pos];
            end
        end 
    end
    
    % Paso 3: Clusterizar según simple-linkage
        % Todos los clusters son singleton
    C = cell(1,length(positions));
    for n = 1:length(positions)
        C{n} = positions(n,:);
    end
    min_dist = inf;
    num_vecino = 0;
    cluster_evaluar = 1;
    cluster_cont = 0;
    indexdb_cont = 0;
    while (length(C) > 1) 
        % Iniciar búsqueda con el primer clúster
        if cluster_evaluar > length(C)
            cluster_evaluar = 1;
        end
        while cluster_evaluar <= length(C)
            % Encontrar los vecinos e indicarlos por el index
            index_cluster = limits_cell(map,C,cluster_evaluar);
            % Si no hay más vecinos, acabar algoritmo
            if isempty(index_cluster)
                cluster_evaluar = cluster_evaluar+1;
                cluster_cont = cluster_cont + 1;
                break;
            else
                cluster_cont = 0;
            end
            % Para cada clúster, escoger el vecino de menor distancia mediante 
            % single linkage
            min_dist = Inf;
            for n = 1:length(index_cluster)
               dist = single_linkage(C{cluster_evaluar},C{index_cluster(n)},weights_grid);
               if dist <= min_dist 
                   num_vecino = n;
                   min_dist = dist;
               end
            end

            % Unión entre clústers del menor y el escogido 
            index_closest  = index_cluster(num_vecino);
            cluster_closest = C{index_closest};
            
            % Parámetro Davies-Bouldin en caso sea más de 2 clústers 
%             [index_flag,index_db] = db_index_v2(C{cluster_evaluar},cluster_closest,weights_grid);
%             indexs_db = [indexs_db;index_db];
            
%             if ~index_flag
%                 cluster_evaluar = cluster_evaluar + 1;
%                 indexdb_cont = indexdb_cont + 1;
%                 break;
%             else 
%                 indexdb_cont = 0;
%             end
            
            
            C{cluster_evaluar} = [C{cluster_evaluar};cluster_closest];

            if index_closest == length(C)
                C = {C{1:end-1}};
            else 
                C = {C{1:index_closest-1},C{index_closest+1:end}};  
            end
            cluster_evaluar = cluster_evaluar + 1; 
        end   
        if length(C) == cluster_cont %|| length(C) == indexdb_cont
            break;
        end
    end
end