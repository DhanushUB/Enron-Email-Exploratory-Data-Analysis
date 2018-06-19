import sys
import re

from datetime import datetime

regex1 = r'(\b(?=\w*[@\.])[\w\-\.@]+\b)' # get email addresses which contains single @ and a .
regex2 = r'(<.*>)' # get everything between the brackets
regex3 = r'\"(.*)\"'

# to extract the values from the unstructured dataset through a patterns using regex
def get_first_found(pattern,x):
	found = re.search(pattern,x)
	if found:
		return found.group(0)
	else: return re.sub(r'\"','',x)
# to get the first name first and last name last, this will convert the names like [kelly,naomi] to naomi kelly 
def func(x):
	cont = lambda x: x.split(',')
	last_name = (x)[1].strip() + " " + cont(x)[0].strip() if ',' in x else x
	return re.sub(r"\"|\'",'', last_name)

# mapper output is sorted in ascending order by key.
date = None
subject = None
body = ''
id_count = 1
key = None
sender_1 = None 
sender_2 = None
origin = None
recievers = []
previous_line = 0
previous_line2 = 0

# column headers
# ("sender", 'receiver', 'date', 'subject', 'body')

for line in sys.stdin:
	line = line.strip().lower()

	#to get details of message-id
	if "message-id: " in line:
		previous_line = 1
		foundes =  re.search(r'<(.*)>', line)
		if foundes:
			newkey = foundes.group()
			newkey = re.sub(r'<|>',"",newkey)
	# to get details of date
	if "date: " in line and "," in line and previous_line > 0:
		date = re.sub(r"date: ", "", line).strip()
		date = re.search(r"([a-z]{3}, [0-9]{2} [a-z]{3} [0-9]{4}.*:[0-9]{2})", date)
		if date:
			date = datetime.strptime(date.group(), "%a, %d %b %Y %H:%M:%S")
		else:
			date = None
	# to get details of date
	if "subject: " in line and previous_line > 0:
		subject = re.sub("subject: ", "", line).strip()
	# to get details of sender
	if "x-from:" in line:
	    sender = re.split(r'x-from:', line)[1].strip()
	    sender_2 = get_first_found(regex1,  sender)
	    sender_2 = re.sub(regex2,'', sender_2)
	    if len(sender_2) == 1: sender_2 = None
	    
	    sender = re.sub(regex1 + '|'+ regex2,'',sender)
	    sender_1 = get_first_found(regex3 ,  sender)
	    if '@' not in sender_1: sender_1 = re.sub(r'\.|\"','',sender_1)
	    
	if "x-origin:" in line:
	    origin = re.split(r'x-origin:', line)[1].strip()
		
	# to get details of receiver
	if "x-to:" in line:
		recievers = re.sub("x-to:", "", line).strip()
		recievers = [x.strip().split('<')[0] for x in re.split(r'>,', recievers)]
		if len(recievers) > 15: continue
		else: recievers = list(map(func, recievers))



	if 'x-filename: ' in line:
		previous_line2 = 1


	if not key:
		key = newkey

	if key != newkey and date is not None and sender_1 is not None and len(recievers)>0:
		print '%s\t%s\t%s\t%s\t%s' % (str(date), sender_1, ",".join(recievers), subject, id_count)
		
		date = None
		subject = None
		body = ''
		id_count += 1
		key = newkey
		sender = None		
		recievers = []
	
		previous_line = 0
		previous_line2 

if key != None and date is not None and sender_1 is not None and len(recievers)>0:
	print '%s\t%s\t%s\t%s\t%s' % (str(date), sender_1, ",".join(recievers), subject, id_count)