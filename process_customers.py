import csv
import sys

def read_customer_samples(filename):
	client_dict = {}
	with open(filename, 'r') as csvfile:	
		#handle = csv.reader(csvfile, delimiter=',', quotechar='"')
		handle = csv.DictReader(csvfile)
		for row in handle:
			#print row['CUSTOMER_CODE']
			client_dict[row['CUSTOMER_CODE']] = 1

	return client_dict

def create_customer_subset(filename, newfilename, client_dict):
	
	fhandle = open(filename,'r')
	header_line = fhandle.readline()
	header = header_line.split(',')

	#Verify the header format
	if header[0].lstrip('"').rstrip('"') != 'CUSTOMER_CODE':
		print "File Header not in specified format."
		sys.exit(-1)
	
	#Write the header 
	whandle = open(newfilename,'w')
	whandle.write(header_line)

	#Process the lines
	while(True):
		line = fhandle.readline()
		if len(line) == 0:
			break
		client_code = line.split(',')[0].lstrip('"').rstrip('"')
		if client_code in client_dict and client_dict[client_code] == 1:
			whandle.write(line)

def create_invoice_subset(filename, newfilename, client_dict):

	invoice_dict = {}
	fhandle = open(filename,'r')
	header_line = fhandle.readline()
	header = header_line.split(',')

	#Verify the header format
	if header[0].lstrip('"').rstrip('"') != 'CUSTOMER_CODE' or header[1].lstrip('"').rstrip('"') != 'INVOICE_CODE':
		print "File Header not in specified format."
		sys.exit(-1)
	
	#Write the header 
	whandle = open(newfilename,'w')
	whandle.write(header_line)

	#Process the lines
	while(True):
		line = fhandle.readline()
		if len(line) == 0:
			break
		fields = line.split(',')
		client_code = fields[0].lstrip('"').rstrip('"')
		invoice_code = fields[1].lstrip('"').rstrip('"')
		if client_code in client_dict and client_dict[client_code] == 1:
			whandle.write(line)
			invoice_dict[invoice_code] = 1

	return invoice_dict

def create_invoice_items_subset(filename, newfilename, invoice_dict):

	fhandle = open(filename,'r')
	header_line = fhandle.readline()
	header = header_line.split(',')

	#Verify the header format
	if header[0].lstrip('"').rstrip('"') != 'INVOICE_CODE' or header[1].lstrip('"').rstrip('"') != 'ITEM_CODE':
		print "File Header not in specified format."
		sys.exit(-1)
	
	#Write the header 
	whandle = open(newfilename,'w')
	whandle.write(header_line)

	#Process the lines
	while(True):
		line = fhandle.readline()
		if len(line) == 0:
			break
		fields = line.split(',')
		invoice_code = fields[0].lstrip('"').rstrip('"')
		if invoice_code in invoice_dict and invoice_dict[invoice_code] == 1:
			whandle.write(line)


cdict = read_customer_samples('CUSTOMER_SAMPLE.CSV')
create_customer_subset('CUSTOMER.CSV', 'CUSTOMER_SUBSET.CSV', cdict)
idict = create_invoice_subset('INVOICE.CSV', 'INVOICE_SUBSET.CSV', cdict)
create_invoice_items_subset('INVOICE_ITEM.CSV', 'INVOICE_ITEM_SUBSET.CSV', idict)
