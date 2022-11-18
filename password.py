from encodings import utf_8
import bcrypt
from db import setData
password = "adminamazon@1848"
password = password.encode('utf-8')
# password = b"adminamazon@1848"
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

setData("Credentials", {'username': 'bhargav',
        'password': str(hashed)})
