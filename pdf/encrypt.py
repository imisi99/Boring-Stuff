import os
import PyPDF2

pdf_files = []

for file_name in os.listdir('.'):
    if file_name.endswith('.pdf'):
        obj = PyPDF2.PdfReader(open(file_name, 'rb'))
        if not obj.is_encrypted:
            pdf_files.append(file_name)

pdf_files.sort(key=str.lower)

for file in pdf_files:
    open_file = open(file, 'rb')
    reader = PyPDF2.PdfReader(open_file)
    writer = PyPDF2.PdfWriter()

    for page in range(len(reader.pages)):
        page_content = reader.pages[page]
        writer.add_page(page_content)

    password = input(f'Enter a password to use encrypt the file {file}: ')
    writer.encrypt(password)

    print(f'Encrypting file {file}')
    save_file = open(f'encrypted_{file}', 'wb')
    writer.write(save_file)
    save_file.close()
