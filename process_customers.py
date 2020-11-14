import csv
import sys

def read_customer_samples(filename):
	client_dict = {}
	try:
		with open(filename, 'r') as csvfile:	
			handle = csv.DictReader(csvfile)
			for row in handle:
				client_dict[row['CUSTOMER_CODE']] = 1
	except IOError:
		print "Error reading customer samples file - %s. Please place all data files in the current directory." %filename
		sys.exit(1)
	except Exception:
		print "Unexpected error:", sys.exc_info()[0]
		sys.exit(1)

	return client_dict

def create_customer_subset(filename, newfilename, client_dict):
	
	try:
		fhandle = open(filename,'r')
	except IOError:
		print "Error reading customer file - %s. Please place all data files in the current directory." %filename
		sys.exit(1)
	except Exception:
		print "Unexpected error:", sys.exc_info()[0]
		sys.exit(1)
	
	try:
		header_line = fhandle.readline()
		header = header_line.split(',')

		#Verify the header format
		if header[0].lstrip('"').rstrip('"') != 'CUSTOMER_CODE':
			print "File Header not in specified format."
			sys.exit(-1)
	except Exception:
		print "Unexpected error:", sys.exc_info()[0]
		sys.exit(1)
	
	#Write the header 
	try:
		whandle = open(newfilename,'w')
	except IOError:
		print "Error creating subset file."
		sys.exit(1)

	whandle.write(header_line)

	try:
		#Process the lines
		while(True):
			line = fhandle.readline()
			if len(line) == 0:
				break
			client_code = line.split(',')[0].lstrip('"').rstrip('"')
			if client_code in client_dict and client_dict[client_code] == 1:
				whandle.write(line)
	except Exception:
		print "Unexpected error:", sys.exc_info()[0]
		sys.exit(1)

def create_invoice_subset(filename, newfilename, client_dict):

	invoice_dict = {}
	try:
		fhandle = open(filename,'r')
	except IOError:
		print "Error reading customer invoice file - %s. Please place all data files (.CSV) in the current directory" %filename
		sys.exit(1)
	except Exception:
		print "Unexpected error:", sys.exc_info()[0]
		sys.exit(1)

	header_line = fhandle.readline()
	header = header_line.split(',')

	#Verify the header format
	if header[0].lstrip('"').rstrip('"') != 'CUSTOMER_CODE' or header[1].lstrip('"').rstrip('"') != 'INVOICE_CODE':
		print "File Header not in specified format."
		sys.exit(-1)
	
	try:
		whandle = open(newfilename,'w')
	except IOError:
		print "Error creating subset file."
		sys.exit(1)

	#Write the header 
	whandle.write(header_line)

	#Process the lines
	try:
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
	
	except Exception:
		print "Unexpected error:", sys.exc_info()[0]
		sys.exit(1)

	return invoice_dict

def create_invoice_items_subset(filename, newfilename, invoice_dict):

	try:
		fhandle = open(filename,'r')
	except IOError:
		print "Error reading customer invoice items file - %s. Please place all data files (.CSV) in the current directory" %filename
		sys.exit(1)
	except Exception:
		print "Unexpected error:", sys.exc_info()[0]
		sys.exit(1)

	header_line = fhandle.readline()
	header = header_line.split(',')

	#Verify the header format
	if header[0].lstrip('"').rstrip('"') != 'INVOICE_CODE' or header[1].lstrip('"').rstrip('"') != 'ITEM_CODE':
		print "File Header not in specified format."
		sys.exit(-1)
	
	try:
		whandle = open(newfilename,'w')
	except IOError:
		print "Error creating subset file."
		sys.exit(1)

	#Write the header 
	whandle.write(header_line)

	try:
		#Process the lines
		while(True):
			line = fhandle.readline()
			if len(line) == 0:
				break
			fields = line.split(',')
			invoice_code = fields[0].lstrip('"').rstrip('"')
			if invoice_code in invoice_dict and invoice_dict[invoice_code] == 1:
				whandle.write(line)
	except Exception:
		print "Unexpected error:", sys.exc_info()[0]
		sys.exit(1)

if __name__ == "__main__":
	print "Reading Customer Samples.."
	cdict = read_customer_samples('CUSTOMER_SAMPLE.CSV')

	print "Creating Customer File from samples"
	create_customer_subset('CUSTOMER.CSV', 'CUSTOMER_SUBSET.CSV', cdict)

	print "Creating Customer Invoice File from samples"
	idict = create_invoice_subset('INVOICE.CSV', 'INVOICE_SUBSET.CSV', cdict)

	print "Creating Customer Invoice Item files from samples"
	create_invoice_items_subset('INVOICE_ITEM.CSV', 'INVOICE_ITEM_SUBSET.CSV', idict)
