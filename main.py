password = open('password.txt')
read = password.read()
input_password = input("Enter the password: ")
if read == input_password:
    print("Access granted")
else:
    print("Intruder alert")