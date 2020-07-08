function [dist] = single_linkage(C1,C2,weights_grid)
    dist = inf; 
%     disp(C1)
%     disp(C2)
    for n = 1:size(C1,1)
        for m = 1:size(C2,1)
            % Distancia de punto m de Clúster 1
            temp1 = C1(n,:); 
            dist1 = squeeze(weights_grid(temp1(1),temp1(2),:));
            % Distancia de punto n de Clúster 2
            temp2 = C2(m,:);
            dist2 = squeeze(weights_grid(temp2(1),temp2(2),:));
            dist_diff = vecnorm(dist1 - dist2); 
            if dist_diff < dist
                dist = dist_diff;
            end
        end 
    end   
end