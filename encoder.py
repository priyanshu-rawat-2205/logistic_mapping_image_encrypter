import base64

def encode(key:str)->str:
    '''Takes a string and converts to base64 string'''

    key_bytes = key.encode('ascii')
    key_base64 = base64.b64encode(key_bytes).decode('ascii')
    return key_base64


def decode(key:str)->str:
    '''Takes a base64 string and converts to string'''
    key_bytes = key.encode('ascii')
    key_base64 = base64.b64decode(key_bytes).decode('ascii')
    return key_base64