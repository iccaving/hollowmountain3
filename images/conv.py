import os

def count(text):
	count = 0
	for letter in text:
		if letter == ".":
			count = count + 1
	return count

for dirpath, dirs, files in os.walk(os.getcwd()):
	for file in files:
		num = count(file)
		if num > 1:
			os.rename(os.path.join(dirpath, file), os.path.join(dirpath, file.replace('.','_',num - 1 )))

for dirpath, dirs, files in os.walk(os.getcwd()):
	for file in files:
		os.rename(os.path.join(dirpath, file), os.path.join(dirpath, file.replace(')','_').replace('(','_').replace("'",'_')))
