from connection import Connection
from datetime import date

query = '''
    select * from test limit 2;
'''

res = Connection().execute(query)

# print(res[0][1])

'''
returns array of tuples, with each tuple representing a row
'''

import hmac, base64
secret = 'secret'.encode('utf-8')
args = 'args'.encode('utf-8')
h = hmac.new(secret, args).hexdigest()
h = base64.urlsafe_b64encode(bytes(h, 'utf-8'))