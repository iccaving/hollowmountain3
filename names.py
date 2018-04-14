import sys

person = raw_input("Enter the person's name: ")

if str(person) in open('hall-of-fame.tex').read():
	if 'Wilson' in str(person):
		print('Careful with Wilsons. Amend manually')
	else:	
		print("This name is already in the database. Amend manually.")
else: 
	year = []
	i=0
	icheck=True
	while icheck != False:
		new_input= raw_input("Enter an expedition year or enter 'stop': ")
		try:
			exped_year= int(new_input)
		except:
			exped_year= new_input

		if type(exped_year) == str:
			icheck = False
		else:
			i =+ 1
			year.append(exped_year)
		
	print(person,year)

	new_line=str(person)+""": \\textsl{"""

	for j in range(len(year)):
		new_line += str(year[j])
		if j < len(year)-1:
			new_line += ', '

	new_line +='.}\n'
	print('This is what you\' ve written in the .tex file:')
	print new_line

	hall_of_fame = open("hall-of-fame.tex","a")
	hall_of_fame.write(new_line)
	hall_of_fame.close()