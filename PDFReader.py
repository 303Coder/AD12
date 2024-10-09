import os

#Install pdfplumber on new computers
#os.system('pip install pdfplumber[full]')
 
import pdfplumber

# Replace '' with the path to your PDF
pdf_path = 'C:\\Users\\BTEC_Cyber_10\\Desktop\\Python VS\\.venv\\Inventory.pdf'

ASIN_list = []
Amount_list = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()

        for table in tables:
            for row in table[2:]:   #Start iterating from the third row (index 2)
                if row:
                    first_column = row[0]
                    last_column = row[-1]
                    ASIN_list.append(first_column)
                    Amount_list.append(last_column)

print(ASIN_list)
print(Amount_list)
