clc; clear all; close all; 
[sD,sM]=som_fdh([38],[5,17],10,12);
[c, p, err, ind] = kmeans_clusters(sM);
[color,b,kmeans]=som_kmeanscolor(sM,8);
figure(2)
som_show(sM,'color',color,'color',{color(:,:,b),'Mejor clúster para la tarea'});
 

%% 
% [C,sM,sD] = clustering_som(sujetos,tareas,k_max,electrodo)
[C,sM,sD,positions,indexs_db] = clustering_som([3],[5,17],10,12);
% Colorear la grilla
map = sM.topol.msize; 
num_map = map(1)*map(2);
color_map = ones(num_map,3);
for n = 1:length(C)
    color = 0.5 + (1-0.5).*rand(1,3);
    for m = 1:size(C{n},1)
        pos = C{n}(m,:);
        color_map(pos(1) + (pos(2)-1)*map(1),:)= color;  
    end
end
%
% Escoger el label de mayor representación en las tareas 5 y 17 
C_labels = cell(1,length(C)); 
for n = 1:length(C)
    counter_T5 = 0;
    counter_T17 = 0;
    for m = 1:size(C{n},1)
        for l = 1:size(sM.labels,2)
            pos = C{n}(m,:);
            if sM.labels{pos(1) + (pos(2)-1)*map(1),l} == "T5"
                counter_T5 = counter_T5+1;
            elseif sM.labels{pos(1) + (pos(2)-1)*map(1),l} == "T17"
                counter_T17 = counter_T17+1;
            end
        end
    end
    
    if counter_T5>counter_T17
        C_labels{n} = 'T5';
    elseif counter_T5<counter_T17
        C_labels{n} = 'T17';
    else
        C_labels{n} = 'none';
    end
end

%
figure(1)
som_show(sM,'umat','all','empty','Labels','norm','d');
som_show_add('label',sM,'subplot',2);
figure(2)
som_cplane(sM.topol.lattice,sM.topol.msize,color_map);
title("Cluster")
figure(3)
plot(indexs_db);
%% 
valores = [];
for n = 1:size(positions,1)
    pos = positions(n,:);
end

valores = [valores;NaN*ones(map(1)*map(2) - length(valores),1)];
[t,r]=db_index(sM,valores);