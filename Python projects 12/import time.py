import time

username = 'hanaka'
password = 'secretpassword'

username_input = input('Username: ')
password_input = input('Password: ')

if username_input == username and password_input == password:
    print('Access granted')
    print('Please wait')
    time.sleep(5)
    print('Ok... Loading...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print('Ok you have security clearance.')
elif username_input == username and password_input != password:
    print('Password incorrect')
elif username_input != username and password_input == password:
    print('Username incorrect')
else:
    print('You might wanna check both fields...')