import os

for folder, subfolder, file in os.walk('./quiz'):
    for i in file:
        if os.path.getsize(os.path.join(os.path.abspath('.') + f'.\\quiz\\{i}')) < 130:
            os.remove(os.path.join(os.path.abspath('.') + f'.\\quiz\\{i}'))
            print('File below 130 bytes have been deleted')
