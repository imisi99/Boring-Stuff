import os
import PyPDF2

pdf_files = []
writer = PyPDF2.PdfWriter()
for file_name in os.listdir('.'):
    if file_name.endswith('.pdf'):
        pdf_files.append(file_name)

pdf_files.sort(key=str.lower)

for file in pdf_files:
    open_file = open(file, 'rb')
    reader = PyPDF2.PdfReader(open_file)

    for page in range(len(reader.pages)):
        page_content = reader.pages[page]
        writer.add_page(page_content)

    writer.encrypt('Bankai')
    save_file = open(f'encrypted_{file}', 'wb')
    writer.write(save_file)
    save_file.close()
