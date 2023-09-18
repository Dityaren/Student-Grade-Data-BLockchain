import datetime as _dt
import hashlib

class Block:
    def __init__(self, previous_hash, data):
        self.data = data
        self.previous_hash = previous_hash
        string = "".join(data) + previous_hash
        self.block_hash = hashlib.sha256((string).encode()).hexdigest()
