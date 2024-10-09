import os

#Install pdfplumber on new computers
#os.system('pip install pdfplumber[full]')
 
import pdfplumber

# Replace '' with the path to your PDF
pdf_path = 'C:\\Users\\BTEC_Cyber_10\\Desktop\\Python VS\\.venv\\Inventory.pdf'

first_column_list = []
last_column_list = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()

        for table in tables:
            # Start iterating from the third row (index 2)
            for row in table[2:]:
                if row:
                    first_column = row[0]
                    last_column = row[-1]
                    first_column_list.append(first_column)
                    last_column_list.append(last_column)

print(first_column_list)
print(last_column_list)
