# customer_samples

Submitted Files:
----------------

1. process_customers.py: 

This is my submission. The code expects all the input files in the current directory. The filenames are expected exactly as specified in the specification doc. 

The output files are suffixed with _SUBSET.CSV, namely
CUSTOMER_SUBSET.CSV
INVOICE_SUBSET.CSV
INVOICE_ITEM_SUBSET.CSV

To run:

	python process_customers.py


2. generate_data.py

This is a script I used to generate sufficient entries in input files to test. Running this script creates a large enough sample for testing.

To run:
	python generate_data.py


Approach:
---------

The approach tried to keep the processing time low and at the O(n) complexity. I used python for the quick coding. Using C would have given more control on the hashing efficiency etc. 

The code seems to run quite fast. Using a test sample of the order as mentioned in the specifications, it completed in 3-5 seconds on my mac (Intel(R) Core(TM) i5-4288U CPU @ 2.60GHz)


