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
		call(['git','mv',os.path.join(dirpath, file),os.path.join(dirpath, name + ext.lower())])
		print(ext)
		if ext == ".jpg" or ext == ".png":
			os.rename(os.path.join(dirpath, file), os.path.join(dirpath, name + ext.upper()))
