grupo_1 = {};
grupo_2 = {};
grupo_3 = {};
for n = 1:80 
    for m = 1:9
        if( out_net_1(m,n) == 1)
            if ( m == 1)
                 %disp('Primer grupo')
                 %disp(tags{n})
                grupo_1 = [grupo_1, tags{n}];
            elseif( m == 7)
                %disp('Segundo grupo')
                grupo_2 = [grupo_2, tags{n}];
%             elseif (m == 3)
%                 grupo_3 = [grupo_3,tags{n}];
            end
        end
    end
end

%% Plots
% Uncomment these lines to enable various plots.
% figure, plotsomtop(net)
% figure, plotsomnc(net)
% figure, plotsomnd(net)
% figure, plotsomplanes(net)
figure, plotsomhits(test1_nn,in_test1_3nn)
figure, plotsomhits(test2_nn,in_test2_4nn)
figure, plotsomhits(test3_nn,in_test3_5nn)
% figure, plotsompos(net,x)

