#!/usr/bin/env python3

import os
import csv
import pdfplumber

region = ""
for path, currentDirectory, files in os.walk("./voter_data/" + region):
    for file in files:
        pdf_file = os.path.join(path, file)
        csv_dir = 'csv/' + region + '/'
        csv_file = csv_dir + file + '.csv'

        if not os.path.exists(csv_dir):
            os.makedirs(csv_dir)

        with pdfplumber.open(pdf_file) as pdf:
            pages = len(pdf.pages)
            for i in  range(pages):
                page = pdf.pages[i]
                table_data = page.extract_table()

                if table_data is not None:
                    with open(csv_file, 'a') as f:
                        write = csv.writer(f)
                        #write.writerow(fields)
                        write.writerows(table_data)
   
        pdf.close()
    
