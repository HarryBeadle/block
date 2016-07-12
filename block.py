#!/env/python

# Block
# A static Website generator

# Harry Beadle 2016 
# www.harrybeadle.co.uk

import os
import glob
from time import time

###################
### UI Elements ###
###################

okay = "[OKY]"
warn = "[WRN]"
err  = "[ERR]"
st_time = time()

########################
### Define functions ###
########################

def html_comment(string):
	return "<!-- " + string + " -->"

def alias_replace(content, alias_dict):
	# Replaces tags with aliases from alias_dict in content
	for A in alias_dict:
		if A in content:
			replacement = os.popen(alias_dict[A]).read()
			if replacement[-1] == "\n":
				replacement = replacement[0:-1]
			content = content.replace(A, replacement)
	return content

def tab_in(content, index):
	# Adds (index) number of tabs to each line of a string
	content = content.split("\n")
	result = []
	for line in content:
		result.append(index * "\t" + line)
	return "\n".join(result)

###########################
### Get associated data ###
###########################

# Get the global aliases
global_dict = {
	"%link%": "echo DIR_ERROR",
}
with open("block-global") as block_global:
	for line in block_global:
		tag, command = line.split(":", 1)
		global_dict[tag] = command

print okay, "Imported block-global"

# Get a list of valid subdirectories
valid_directories = []
subdirectories = [x[0] for x in os.walk('.')]
for folder in subdirectories:
	if folder.count("/") == 1 and folder.count(".") == 1:
		valid_directories.append(folder[2:])
with open("block-ignore") as ignored_directories:
	for directory in ignored_directories:
		directory = directory.replace("\n", "")
		if directory in valid_directories:
			valid_directories.remove(directory)

print okay, "Got valid subdirectories"

# Get a list of block link (.bl) files
block_links = glob.glob('*.bl')
print okay, "Got block link files"

################################
### Output the HTML document ###
################################

print okay, "Genorating index.html"

index = open("index.html", "w")

# Start the HTML document
index.write("""<html>
\t<head>""")

# Output head.html
with open("block-theme/head.html") as head_file:
	index.write(tab_in(alias_replace(head_file.read(), global_dict), 2))

# Finish the <head> and start the <body>
index.write("""\t</head>\n\t<body>""")

# Output header.html
with open("block-theme/header.html") as header_file:
	index.write(tab_in(alias_replace(header_file.read(), global_dict), 2))

# Output the blocks
with open("block-theme/block.html") as b:
	block = b.read()
	for directory in valid_directories:
		local_dict = {
			"%link%": "echo " + directory
		}
		index.write("\t\t<div>")
		try:
			with open(directory + "/block-local") as local:
				for line in local:
					tag, command = line.split(":", 1)
					local_dict[tag] = command
			index.write(tab_in(alias_replace(block, local_dict), 3))
		except IOError:
			print err, "No block-local found for " + directory + "."
		index.write("\t\t</div>")
	for block_link in block_links:
		local_dict = {}
		index.write("\t\t<div>")
		with open(block_link) as bl:
			for line in bl:
				tag, command = line.split(":", 1)
				local_dict[tag] = command
			index.write(tab_in(alias_replace(block, local_dict), 3))
		index.write("\t\t</div>")

# Output footer.html
with open("block-theme/footer.html") as footer_file:
	index.write(tab_in(alias_replace(footer_file.read(), global_dict), 2))

# Finsh the HTML document
index.write("""\t</body>\n\t</html>""")

index.close()

print okay, "index.html genorated in", str(time() - st_time) + "s"