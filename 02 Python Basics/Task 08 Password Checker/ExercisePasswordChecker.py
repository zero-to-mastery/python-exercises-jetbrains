# Password Checker Exercise
# Hide the password with asterisks

username = input('Enter your username:\t')
password = input('Enter you password:\t')

# Hide the password by creating a string of asterisks
secret_password = len(password) * '*'

print(f'Hey {username}, your password {secret_password} is {len(password)} letters long.')
