function [lims] = limits(pos,map)
    % En caso la grilla fuese impar (filas)
    lims_par =[  pos(1)-1,pos(2);... 
                pos(1)-1,pos(2)+1;...
                  pos(1),pos(2)+1;...
                  pos(1)+1,pos(2)+1;...
                  pos(1)+1,pos(2);...
               pos(1),pos(2)-1];
           
    % En caso la grilla es par
    lims_impar =[ pos(1)-1, pos(2)-1;... 
                  pos(1)-1,pos(2);...
                  pos(1),pos(2)+1;...
                  pos(1)+1,pos(2);...
                pos(1)+1,pos(2)-1;...
                 pos(1),pos(2)-1];
    if (mod(pos(1),2) == 0 )
        lims_r = lims_par; 
    else
        lims_r = lims_impar;
    end
     lims = [];
    for n= 1:length(lims_r)
        if (0<lims_r(n,1) && lims_r(n,1)<=map(1) && 0<lims_r(n,2) && lims_r(n,2)<=map(2))
            lims = [lims;lims_r(n,:)];
        end
    end