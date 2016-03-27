xcoords=[];
ycoords=[];
for y=1:46
    for x=1:167
        if pic(y,x,1)~=255
            xcoords=[xcoords x];
            ycoords=[ycoords 46-y];
        end
    end
end
plot(xcoords,ycoords,'*');
file=fopen('message.txt','w');
for x=1:length(xcoords)
    fprintf(file,'%g,%g\n',xcoords(x),ycoords(x));
end
fclose('all');