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
hall_of_fame.write('\\begin{tcolorbox}\n'+'\\begin{fullwidth} \n'+'\\chapter{Hall of Fame} \n')
hall_of_fame.write('\n Here follows a non-exhaustive list of the members involved in the exploration of \\passage{Tolminski Migovec} during the last five expeditions. Please forgive any omissions \n')
hall_of_fame.write('\n \\begin{multicols}{2} \n')
for i in range(len(your_list)):
	if i !=0:
		hall_of_fame.write('%s %s \n \n'% (your_list[i][1],your_list[i][0]))
		
hall_of_fame.write('\\end{multicols} \n \\end{fullwidth} \n \\end{tcolorbox} \n')
hall_of_fame.close()
