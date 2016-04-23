# CryptoCTF
This is where your problems go. They exist in two places in the repository: `/problems` and `/ymlproblems`.

## /problems ##
The `/problems` directory is the information that will be published after the CTF; and should include the following information:

- flag.txt
- statement.txt (shorter ciphertext can be in a `<code>` tag within the statement)
- writeup.txt

Optionally:

- generation file
- solution code
- additional necessary files (pictures, longer flags, etc.)


## /ymlproblems
The `/ymlproblems` directory is one which will be crawled by a tool on the website and which will be used to populate the list of problems. Each subfolder here (which should be named in the same fashion as the corresponding folder in `/problems` should contain the following items:

### problem.yml ###

Fill the file with data like what is given in this example. Your description can be multiline, but the only parsed linebreaks will be `<br />`. After the statement is finished, you must follow it with a linebreak delimited list of item links like `<a href="|myfile.extension|">myfile.extension</a>`. **Don't forget the pipes around the filename!** Also, the hint is optional (but recommended). All of the problems currently have a point value of 100; this will be changed soon. Here is the example:

	- name: Yellow Submarine
	- author: Jacob Magnuson
	- category: Classic
	- description: >
		THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG.<br />
	    <a href="|yellow_submarine.txt|">yellow_submarine.txt</a>
	- hint: Don't ignore the problem statement. Or do, and just google instead.
	- points: 100
	- flag: "flag{just_used_quipqiup_anyway}"

### static.yml ###

This file contains a list of all extra files associated with your problem. For the example above, it would contain one line:
	
	- yellow_submarine.txt

If your problem doesn't have any external files, omit this file.

### extra files ###

Place all associated files in the same folder, ensuring they have the same names as the ones given above.

If you have any questions, check out the other problems in the directory as examples.