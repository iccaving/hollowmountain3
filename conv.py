import os
from subprocess import call
import fileinput
import re
import shutil

def count(text):
	count = 0
	for letter in text:
		if letter == ".":
			count = count + 1
	return count


def matchcase(m):
	return m.group().lower()

for dirpath, dirs, files in os.walk(os.getcwd()):
	for file in files:
		print(file)
		filename = file
		with open(os.path.join(dirpath, file + "temp"), "w+") as wfile:
			with open(os.path.join(dirpath, file)) as file:
    				for line in file:
        				result = re.sub(r"images\/(.*)}", matchcase, line)
					if result is not None:
						wfile.write(result)
					else:
						wfile.write(line)
		shutil.move(os.path.join(dirpath, filename + "temp"), os.path.join(dirpath, filename))
