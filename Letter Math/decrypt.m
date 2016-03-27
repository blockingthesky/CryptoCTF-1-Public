readFile=fopen('encrypted','r');
writeFile=fopen('decrypted','w');
line=fgetl(readFile);
decrypted='';
while ischar(line) %while there are still lines to read
    letter=char(line(1)+str2double(line(2:length(line))));
    fprintf(writeFile,'%s',letter);
    line=fgetl(readFile);
end
fclose('all');