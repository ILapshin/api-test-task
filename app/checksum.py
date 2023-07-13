import hashlib

def get_checksum(bytes_data):
    return hashlib.md5(bytes_data).hexdigest()