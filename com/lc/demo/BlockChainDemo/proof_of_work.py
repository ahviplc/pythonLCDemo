import hashlib

# 计算哈希值
sha256 = hashlib.sha256()
sha256.update('LC1'.encode('utf-8'))
res1 = sha256.hexdigest()

sha256.update('LC2'.encode('utf-8'))
res2 = sha256.hexdigest()
print(res1, res2)


def proof_of_work():
    data = 'LC'
    x = '1'
    sha256.update((data + x).encode('utf-8'))
    print(sha256.hexdigest())
    while True:
        if str(sha256.hexdigest())[0:1] != "0":
            x = str(int(x) + 1)
            print(x)
            if x == '10':
                print('End!', x)
                break
        else:
            print(str(sha256.hexdigest()))
            print(x)
            break


if __name__ == '__main__':
    proof_of_work()
