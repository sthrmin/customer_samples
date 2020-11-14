from random import *

def generate_customer_sample():
	f = open('CUSTOMER_SAMPLE.CSV','w')
	f.write('"CUSTOMER_CODE"\n')

	total = 0

	i = 100020
	while(True):
		
		index = (int)( random() * 100)
		customer_code = "CUST0" + "%08d" %i
		i = i + index
		total = total + 1

		f.write('"%s"\n' %(customer_code))
		
		if total >= 1000:
			break

def generate_customer_csv():
	f = open('CUSTOMER.CSV','w')
	f.write('"CUSTOMER_CODE","FIRSTNAME","LASTNAME"\n')

	names_data=open('names.txt').read()	
	names=names_data.split("\n")

	for i in range(10000,500000):
		customer_code = "CUST0" + "%08d" %i

		fn = (int)(random() * len(names))
		l = (int)(random() * len(names))
		first_name = names[fn]
		last_name = names[l]
		f.write('"%s","%s","%s"\n' %(customer_code,first_name,last_name))

def generate_invoice_csv():
	f = open('INVOICE.CSV','w')
	f.write('"CUSTOMER_CODE","INVOICE_CODE","AMOUNT","DATE"\n')

	cust = {}

	invoice_num = 1
	for i in range(10000,500000):
		j = (int)(random() * i)
		customer_code = "CUST0" + "%08d" %j
		am = (int)(random() * 1000)

		invoice_code = "INV00" + "%03d" %invoice_num
		invoice_num = invoice_num + 1

		f.write('"%s","%s","%d","01-01-2020"\n' %(customer_code,invoice_code,am))

def generate_invoice_item_csv():
	f = open('INVOICE_ITEM.CSV','w')
	f.write('"INVOICE_CODE","ITEM_CODE","AMOUNT","QUANTITY"\n')

	invoice_num = 1
	for i in range(1,400000):
		j = (int)(random() * i)
		customer_code = "CUST0" + "%08d" %j
		rnd = (int)(random() * 5)

		for r in range(1,rnd):
			invoice_code = "INV00" + "%03d" %invoice_num
			am = (int)(random() * 1000)
			f.write('"%s","RANDOM_STR","%d","10"\n' %(invoice_code,am))

		invoice_num = invoice_num + 1

generate_customer_csv()
generate_invoice_csv()
generate_invoice_item_csv()
generate_customer_sample()
