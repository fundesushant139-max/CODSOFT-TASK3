import string
import random
lower = string.ascii_uppercase
upper = string.ascii_lowercase
digits=string.digits 
punct = string.punctuation

password_length=int(input("Enter password length:"))
print()
ch=int(input('''Enter complexity of password:
1-for easy
2-for medium
3-for hard
'''))

if ch==1: #easy => upper+lowercase only
    password=[]
    password.extend(list(lower))
    password.extend(list(upper))
    key=random.sample(password,password_length)
    password=''.join(key)
    print(f'Generated password is {password}')

if ch==2: #medium => upper+lowercase+digits letters only 
    password=[]
    password.extend(list(lower))
    password.extend(list(upper))
    password.extend(list(digits))
    key=random.sample(password,password_length)
    password=''.join(key)
    print(f'Generated password is {password}') 

if ch==3: #hard => upper+lowercase letters+digits+punctuation
    password=[]
    password.extend(list(lower))
    password.extend(list(upper))
    password.extend(list(digits))
    password.extend(list(punct))
    key=random.sample(password,password_length)
    password=''.join(key)
    print(f'Generated password is {password}')