import os

# Find valid subdirectories
valid = []
for folder in [x[0] for x in os.walk('.')]:
    if folder.count('/') == 1 and folder.count('.') == 1:
        valid.append(folder[2:])
with open("block-ignore") as i:
    for subdir in i:
        if subdir.replace('\n', '') in valid:
            valid.remove(subdir.replace('\n', ''))

# Output the <head>
print "<html><head><title>", "Harry Beadle", "</title>"
print "<link rel=\"stylesheet\" href=\"block-theme/style.css\"></head><body>"

# Get the global aliases
global_aliases = ["%link%"]
global_aliases_dict = {
    "%link%": "echo DIR_ERROR"
}
with open("block-global") as g:
    for line in g:
        global_aliases.append(line.split(":")[0])
        global_aliases_dict[line.split(":")[0]] = line.split(":")[1]

# Output the header.html
with open("block-theme/header.html") as header_file:
    header = header_file.read()
    for a in global_aliases:
        if a in header:
            header = header.replace(a, os.popen(global_aliases_dict[a]).read())
    print header

block = open('block-theme/block.html', 'r').read()
tmpblock = block
for f in valid:
    aliases = global_aliases
    aliases_dict = global_aliases_dict
    aliases_dict["%link%"] = "echo " + f
    print "<div>"
    try:
        with open(f+"/block-local") as local:
            for line in local:
                aliases.append(line.split(":")[0])
                aliases_dict[line.split(":")[0]] = line.split(":")[1]
    except:
        os.system("touch \"" + f + "/block-local\"")
    for a in aliases:
        if a in tmpblock:
            tmpblock = tmpblock.replace(a, os.popen(aliases_dict[a]).read())
    print tmpblock
    print "</div>"
    tmpblock = block

with open("block-theme/footer.html") as footer_file:
    footer = footer_file.read()
    for a in global_aliases:
        if a in footer:
            footer = footer.replace(a, os.popen(global_aliases_dict[a]).read())
    print footer
