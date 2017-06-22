#open the file - read all of the lines
attempts_file ='attempts.txt'
#use strip to strip out spaces and trim the lines

data = [line.strip()for line in open(attempts_file,'r')]
print len(data)

attempts_output = open('attempts.csv','w')
attempts_output.write('Course Student Number,email\n')
for item in data:
	entry = {}
	columns =  item.split(' ')
	#print len(columns)
	#print columns[23]
	line = columns[23].split('?')[1].strip('",')
	#print line
	values = line.split('&')
	#print values[0],
	#print values[2],
	#print values[3]
	attempts_output.write('%s,%s,%s\n' %(values[0].split('=')[1],values[3].split('='),values[2].split('=')[1]))
	
attempts_output.close()
	