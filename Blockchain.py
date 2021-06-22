from Block import Block

class Blockchain:

    def __init__(self):
        self.chain=[Block.genesis()]

    
    def addBlock(self,data):
        block = Block.mineBlock(self.chain[len(self.chain)-1],data)
        self.chain.append(block)
        return block
    
    def isValidChain(self,chain):
        if str(chain[0])!= str(Block.genesis()):
            return False
        for i in range(1,len(chain)):
            block = chain[i]
            lastBlock = chain[i-1]
            
            if block.lastHash != lastBlock.hash  or block.hash != Block.blockHash(block) :
                return False
        
        return True
    
    def replaceChain(self,newChain):
        if len(newChain) < len(self.chain):
            print("Received chain is not longer than the current chain. ")
            return
        elif not self.isValidChain(newChain):
            print("The Received chain is not valid. ")
            return
        print("Replacing blockchain with the new chain...")
        self.chain = newChain
        
    
