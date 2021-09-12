## Password Manager ##
# Requirements #
# Store the master password
# Ask user to enter master password
# After user enters master password correctly, they have 4 options
# View all passwords
# Add a password
# Close the password manager
from cryptography.fernet import Fernet

'''
def write_key():
	key = Fernet.generate_key()
	with open("key.key", "wb") as key_file:
		key_file.write(key)'''

def load_key():
	file = open("key.key", "rb")
	key = file.read()
	file.close()
	return key

def view_passwords():
	with open("passwords.txt", "r") as f:
		for line in f.readlines():
			data = line.rstrip()
			user, password = data.split("|")
			print("Username: " + user + ", " + "Password: " + 
			fer.decrypt(password.encode()).decode())
def add_password():
	username = input("Username: ")
	password = input("Password: ")
	
	with open("passwords.txt", "a") as f:
		f.write(username + "|" + fer.encrypt(password.encode()).decode()
		 + "\n")

master_pass = 'p'
key = load_key()
fer = Fernet(key)
master_username = input("Please enter your username: ")
user_master_pass = input("Please enter the master password: ")

if user_master_pass == master_pass:
	print("******************************************")
	print("********** O P E N  S E S A M E **********")
	print("******************************************")
	print("Welcome to the vault, " + master_username)
	mode_select = int(input("[1] View all passwords" + "\n" +
						"[2] Add a password"+ "\n" +
						"[3] Close program"+ "\n" +
						"Please select an option: "))
	if mode_select == 1:
		view_passwords()
	elif mode_select == 2:
		add_password()
	elif mode_select == 3:
		print("Have a nice day.")
		quit()
else:
	print("That password is incorrect.")


