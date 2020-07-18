function [index_flag,index_db] = db_index_v2(C1,C2,weights_grid)
    index_db = 0;
    if (size(C1,1) ~= 1 && size(C2,1)~=1) 
        dist1 = []; 
        for n = 1:size(C1,1)
            temp = C1(n,:);
            pesos = squeeze(weights_grid(temp(1),temp(2),:));
            dist1 =[dist1,pesos];
        end
        
        centroid1 = sum(dist1')'/size(dist1,2);
        sumsc_1 = 0;

        for m = 1:size(dist1,2)
           sumsc_1 = sumsc_1 + norm(centroid1-dist1(:,m)); 
        end

        Sc_1v2 = sumsc_1/size(dist1,2);
        dist2 = [];

        for n = 1:size(C2,1)
            temp = C2(n,:);
            pesos = squeeze(weights_grid(temp(1),temp(2),:));
            dist2=[dist2,pesos];
        end

        centroid2 = sum(dist2')'/size(dist2,2);
        sumsc_2 = 0;

        for m = 1:size(dist2,2)
           sumsc_2 = sumsc_2 + norm(centroid2-dist2(:,m)); 
        end

        Sc_2v2 = sumsc_2/size(dist2,2);
        index_db = ((Sc_1v2+Sc_2v2)/(norm(centroid1-centroid2)))/2;

        disp(index_db);
        if index_db >=1
            index_flag = true;
        else
            index_flag = false;
        end
        
    else
        index_flag = true;  
   end

end