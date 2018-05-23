import subprocess
import shlex


#subprocess.call(shlex.split("touch templist.txt"))
subprocess.call(shlex.split("find . -name '*.pdf' -exec echo {} \;"))

old_list, new_list =[],[]
commands = []

with open('templist.txt', 'r') as infile:
 	for line in infile:
 		old_list.append(line[2:-1])
 		new_list.append(line[2:-5]+'_cmyk.tiff')


print(old_list)
print(new_list)

for i,j in zip(old_list,new_list):
	subprocess.call(shlex.split('convert {!s} -verbose -density 300 -evaluate Pow 1.1 {!s}'.format(i,j)))

