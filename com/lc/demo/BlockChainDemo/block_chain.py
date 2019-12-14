import hashlib

"""

block_chain.py 写法1
python实现的区块链思想
备注：python实现的区块链思想
Version: 1.0
Author: LC
DateTime: 2019年12月14日23:45:53
UpdateTime:
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
LC博客url: http://oneplusone.vip/index.html
一加壹.SNS LC - 又一个SNS社区: http://sns.oneplusone.vip
赞助一加壹博客最Top-LC万能收款码支持-支付宝、微信、QQ
http://lc.oneplusone.vip/donateMeByLC.html

"""


# sha256 哈希值算法
def sha256(data_need_sha):
    sha256 = hashlib.sha256()
    sha256.update(data_need_sha.encode('utf-8'))
    return sha256.hexdigest()


# 区块
class Block:
    def __init__(self, data, previousHash):
        self.data = data
        self.previousHash = previousHash
        self.hash = self.ComputeHash

    # Python内置的@property装饰器就是负责把一个方法变成属性调用的
    @property
    def ComputeHash(self):
        return str(sha256(self.data))

    def showBlock(self):
        print({'data': self.data, 'previousHash': self.previousHash, 'hash': self.hash})


# 链
class Chain:
    def __init__(self):
        self.chain = [self.ancestorBlock]

    @property
    def ancestorBlock(self):
        ancestor_block = Block('祖先区块', '')
        return ancestor_block

    @property
    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    def addBlockToChain(self, newBlock):
        newBlock.previousHash = self.getLatestBlock.hash
        newBlock.hash = newBlock.ComputeHash
        self.chain.append(newBlock)

    def showChain(self):
        for i in self.chain:
            i.showBlock()

    def validateChain(self):
        if len(self.chain) == 1:
            if self.chain[0].hash != self.chain[0].ComputeHash:
                return False
            return True

        for i in range(1, len(self.chain)):
            blockToValidate = self.chain[i]
            if (blockToValidate.hash) != blockToValidate.ComputeHash:
                print('数据被篡改')
                return False
            previousBlock = self.chain[i - 1]
            if blockToValidate.previousHash != previousBlock.hash:
                print('前后区块链接断裂')
                return False
        return True


block1 = Block('转账10', '')
block2 = Block('转账20', '')
bitChain = Chain()
bitChain.addBlockToChain(block1)
bitChain.addBlockToChain(block2)

bitChain.showChain()
print(bitChain.validateChain())

# {'data': '祖先区块', 'previousHash': '', 'hash': '4fed52ab5fe830c2e29def3b0de30430b43feb9583e6b9446e6cb1782e363615'}
# {'data': '转账10', 'previousHash': '4fed52ab5fe830c2e29def3b0de30430b43feb9583e6b9446e6cb1782e363615', 'hash': 'ac0c6fe9e0b06e4f8b73f7015336dd5eec4ebc9050f9274ba5d9e6dc6a3a5f86'}
# {'data': '转账20', 'previousHash': 'ac0c6fe9e0b06e4f8b73f7015336dd5eec4ebc9050f9274ba5d9e6dc6a3a5f86', 'hash': '72338ca77bb994b019f921533aecc1d72849253228b50254973d96b70abe29fa'}
# True

# 尝试篡改区块
bitChain.chain[1].data = '转账500'
# 尝试修正hash
bitChain.chain[1].hash = bitChain.chain[1].ComputeHash
bitChain.showChain()
print(bitChain.validateChain())

# {'data': '祖先区块', 'previousHash': '', 'hash': '4fed52ab5fe830c2e29def3b0de30430b43feb9583e6b9446e6cb1782e363615'}
# {'data': '转账500', 'previousHash': '4fed52ab5fe830c2e29def3b0de30430b43feb9583e6b9446e6cb1782e363615', 'hash': 'eb2a7f283d78892515d1ea7c7389889da6827df4c43de0c472ced9aa82ce2b43'}
# {'data': '转账20', 'previousHash': 'ac0c6fe9e0b06e4f8b73f7015336dd5eec4ebc9050f9274ba5d9e6dc6a3a5f86', 'hash': '72338ca77bb994b019f921533aecc1d72849253228b50254973d96b70abe29fa'}
# 前后区块链接断裂
# False
