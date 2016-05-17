import os

curfile = "mordor.zip"
newfile = ""
prevfile = ""
counter = 0
fileindex = 13

while newfile != "flag.txt":
	contents = os.popen("unzip -l " + curfile).read().split()
	newfile = contents[fileindex]
	os.popen("unzip -p " + curfile + " > " + str(counter)+".zip")
	prevfile = curfile
	curfile = str(counter)+".zip"
	os.popen("rm " + prevfile)
	counter += 1

print open(curfile, "r").read()
