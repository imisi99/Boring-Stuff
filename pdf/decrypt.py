import PyPDF2
import os
from PyPDF2.errors import FileNotDecryptedError

encrypted_files = []

for file_name in os.listdir('.'):
    if file_name.endswith('.pdf'):
        obj = PyPDF2.PdfReader(open(file_name, 'rb'))
        if obj.is_encrypted:
            encrypted_files.append(file_name)

encrypted_files.sort(key=str.lower)

for file in encrypted_files:
    file_obj = PyPDF2.PdfReader(open(file, 'rb'))
    writer = PyPDF2.PdfWriter()

    password = input(f'enter password for the file {file}: ')
    file_obj.decrypt(password)

    try:
        for pages in range(len(file_obj.pages)):
            file_page = file_obj.pages[pages]
            writer.add_page(file_page)

        save_file = open(f'decrypted_{file}', 'wb')
        writer.write(save_file)
        save_file.close()

    except FileNotDecryptedError as e:
        print(f'An error occurred on {file} due to {e} ')
