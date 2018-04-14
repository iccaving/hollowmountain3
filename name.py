import csv

from operator import itemgetter

with open('hall_of_fame.csv', 'rU') as f:
  reader = csv.reader(f)
  your_list = list(reader)

for i in range(len(your_list)):
	new_line=your_list[i]
	for h in range(len(new_line)):
		if new_line[h] == 'y':
			new_line[h] = your_list[0][h]
	your_list[i] = new_line 
headings=your_list[0]
print headings

del your_list[0]
your_list.sort()
your_list.insert(0,headings)
print your_list


hall_of_fame = open('hall-of-fame.tex','w')
hall_of_fame.write('\\section{Hall of Fame} \n')
hall_of_fame.write('\n')


for i in range(len(your_list)):
	k=0
	if i != 0:
		hall_of_fame.write('%s %s: \\textsl{'% (your_list[i][1],your_list[i][0]))
		k=0
		for h in range(2,len(your_list[i])):	
			if your_list[i][h] != 'n':			
				k+=1
				if k != len(your_list[i]) - your_list[i].count('n') - 2:
					hall_of_fame.write('%s, ' % (your_list[i][h]))
				else:
					hall_of_fame.write('%s }\n' % (your_list[i][h]))
					hall_of_fame.write('\\newline\n')

hall_of_fame.close()