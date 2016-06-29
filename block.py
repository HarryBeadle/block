#!/env/python

# Block
# A static Website generator

# Harry Beadle 2016 
# www.harrybeadle.co.uk

import os

########################
### Define functions ###
########################

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
		tag, command = line.split(":")
		global_dict[tag] = command

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

################################
### Output the HTML document ###
################################

# Start the HTML document
print """<html>
\t<head>"""

# Output head.html
with open("block-theme/head.html") as head_file:
	print tab_in(alias_replace(head_file.read(), global_dict), 2)

# Finish the <head> and start the <body>
print """\t</head>
	<body>"""

# Output header.html
with open("block-theme/header.html") as header_file:
	print tab_in(alias_replace(header_file.read(), global_dict), 2)

# Output the blocks
with open("block-theme/block.html") as b:
	block = b.read()
	for directory in valid_directories:
		local_dict = {
			"%link%": "echo " + directory
		}
		print "\t\t<div>"
		try:
			with open(directory + "/block-local") as local:
				for line in local:
					tag, command = line.split(":")
					local_dict[tag] = command
			print tab_in(alias_replace(block, local_dict), 3)
		except IOError:
			print "\t\t\tNo block-local found for " + directory + "."
		print "\t\t</div>"

# Output footer.html
with open("block-theme/footer.html") as footer_file:
	print tab_in(alias_replace(footer_file.read(), global_dict), 2)

# Finsh the HTML document
print """\t</body>
</html>"""


