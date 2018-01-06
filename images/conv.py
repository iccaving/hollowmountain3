import os
from subprocess import call

def count(text):
	count = 0
	for letter in text:
		if letter == ".":
			count = count + 1
	return count

for dirpath, dirs, files in os.walk(os.getcwd()):
	for file in files:
		name, ext = os.path.splitext(file)
		call(['git','mv','--force',os.path.join(dirpath, file),os.path.join(dirpath, file.lower())])
		#os.rename(os.path.join(dirpath, file), os.path.join(dirpath, file.lower()))
