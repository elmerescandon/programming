
% Neuronas de mayor peso
   % 1 : 21 - 22 
   % 2 : 20 - 19 - 15
grupo_1 = {};
grupo_2 = {};
   
for n = 1:80 
    for m = 1:9
        if( out_net_1(m,n) == 1)
            if ( m == 21 || m == 22 || m ==16)
                disp('Primer grupo')
                disp(tags{n})
                grupo_1 = [grupo_1, tags{n}];
            elseif( m == 7)
                disp('Segundo grupo')
                grupo_2 = [grupo_2, tags{n}];
            end
        end
    end
end