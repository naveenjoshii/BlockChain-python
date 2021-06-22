import time
import hashlib
DIFFICULTY = 4
MINE_RATE = 30000
class Block:
    def __init__(self,timestamp,lastHash,hash,data,nonce,difficulty=DIFFICULTY):
        self.timestamp = timestamp
        self.lastHash = lastHash
        self.hash = hash
        self.data = data
        self.nonce = nonce
        self.difficulty = difficulty 
    
    def to_string(self):
        return "timestamp: " + str(self.timestamp) + "\nlastHash : " + str(self.lastHash[:10]) + "\nHash: " + str(self.hash[:10]) + "\nNonce: " + str(self.nonce) + "\nDifficulty: " + str(self.difficulty) +"\nData: " + str(self.data)   +"\n--------------"
    
    @staticmethod
    def genesis():
        timestamp = str(int(time.time() * 1000))
        return Block(timestamp,'------','f1r57-h45h',[],0,DIFFICULTY) 

    
    @staticmethod
    def mineBlock(lastBlock,data): 
        timestamp = ""
        hash = ""
        lastHash = lastBlock.hash
        difficulty = lastBlock.difficulty
        nonce = 0
        while True:
            nonce+=1
            timestamp = str(int(time.time() * 1000))
            difficulty = Block.adjustDifficulty(lastBlock,timestamp)
            hash = Block.hash(timestamp,lastHash,data,nonce,difficulty)
            if (hash[:difficulty]) == '0'* difficulty:
                break
        return Block(timestamp,lastHash,hash,data,nonce,difficulty)

    @staticmethod
    def hash(timestamp,lastHash,data,nonce,difficulty):
        h = hashlib.sha256()
        h.update(
        str(timestamp).encode('utf-8') +
        str(lastHash).encode('utf-8') +
        str(data).encode('utf-8')+
        str(nonce).encode('utf-8')+
        str(difficulty).encode('utf-8')
        )
        return str(h.hexdigest())
    
    @staticmethod
    def blockHash(block):
        timestamp = block.timestamp
        lastHash = block.lastHash
        data = block.data 
        nonce = block.nonce
        difficulty = block.difficulty
        return Block.hash(timestamp,lastHash,data,nonce,difficulty)
    
    @staticmethod
    def adjustDifficulty(lastBlock,currentTime):
        difficulty = lastBlock.difficulty
        tt = int(lastBlock.timestamp)+MINE_RATE 
        if tt > int(currentTime):
            difficulty = difficulty+1
        else:
            difficulty = difficulty-1
        return difficulty
