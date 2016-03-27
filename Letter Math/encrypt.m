function [ ] = encrypt( message )
file=fopen('encrypted','w');
for x=1:length(message)
    n=randi([-40,40]);
    while(message(x)+n)>126 || (message(x)+n)<32
        n=randi([-40,40]);
    end
    fprintf(file,'%s%+g\n',char(message(x)+n),-n);
end
fclose('all');
end
