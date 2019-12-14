from hashlib import sha256

"""

block_chain_2.py 写法2
python实现的区块链思想
备注：python实现的区块链思想
Version: 1.0
Author: LC
DateTime: 2019年12月14日23:47:02
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""


class Block:

    def __init__(self, index, timestamp, data, previousHash=""):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculateHash()

    def calculateHash(self):
        plainData = str(self.index) + str(self.timestamp) + str(self.data)
        return sha256(plainData.encode('utf-8')).hexdigest()

    def __str__(self):
        return str(self.__dict__)


class BlockChain:

    def __init__(self):
        self.chain = [self.createGenesisBlock()]

    def createGenesisBlock(self):
        return Block(0, "01/01/2018", "genesis block", "0")

    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()
        self.chain.append(newBlock)

    def __str__(self):
        return str(self.__dict__)

    def chainIsValid(self):
        for index in range(1, len(self.chain)):
            currentBlock = self.chain[index]
            previousBlock = self.chain[index - 1]
            if (currentBlock.hash != currentBlock.calculateHash()):
                return False
            if previousBlock.hash != currentBlock.previousHash:
                return False
        return True


myCoin = BlockChain()
myCoin.addBlock(Block(1, "02/01/2018", "{amount:4}"))
myCoin.addBlock(Block(2, "03/01/2018", "{amount:5}"))

# print block info
print("print block info ####:")
for block in myCoin.chain:
    print(block)
# check blockchain is valid
print("before tamper block,blockchain is valid ###")
print(myCoin.chainIsValid())
# tamper the blockinfo
myCoin.chain[1].data = "{amount:1002}"
print("after tamper block,blockchain is valid ###")
print(myCoin.chainIsValid())

# print block info ####:
# {'index': 0, 'timestamp': '01/01/2018', 'data': 'genesis block', 'previousHash': '0', 'hash': 'd8d21e5ba33780d5eb77d09d3b407ceb8ade4e5545ef951de1997b209d91e264'}
# {'index': 1, 'timestamp': '02/01/2018', 'data': '{amount:4}', 'previousHash': 'd8d21e5ba33780d5eb77d09d3b407ceb8ade4e5545ef951de1997b209d91e264', 'hash': '15426e32db30f4b26aa719ba5e573f372f41e27e4728eb9e9ab0bea8eae63a9d'}
# {'index': 2, 'timestamp': '03/01/2018', 'data': '{amount:5}', 'previousHash': '15426e32db30f4b26aa719ba5e573f372f41e27e4728eb9e9ab0bea8eae63a9d', 'hash': '75119e897f21c769acee6e32abcefc5e88e250a1f35cc95946379436050ac2f0'}
# before tamper block,blockchain is valid ###
# True
# after tamper block,blockchain is valid ###
# False
