from cryptography.fernet import Fernet
import base64

alphabet = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
payload = b'gAAAAABizIKoyFIV6UJ8RF63YVhgOYHMmXlD8q1kHAFGdqTD8DSgN5PANvhJnc9m0Z5P1J-1bc_rT8I041Od2ND4bfzoMsBWBFqj3qphw7xclxFMhehZPrn2qlqKN7_3TYb8cBetpp0WYKzZXfYx4ukxMxidJyzZAkaTO1DNOqkWDagt8P_r_jw4COxjV3DAdVu5G9VbTz-fBsh9ySPYB2NhnZP546ppREVosfYjokgK-w-xgZLhywP8iSaVpFtX6ZE8X6ODz_42jxHJhmFE1a1HdT1HH8RWybWZfmqr_ce-IpjzWQwVLEBELOz_X3LQaZlaE96-OJW1rE_gVLUvB1GRpMhYO0TgOpzXVGNnRkT4Qb0aERiTNMTJDA6YsapJ5sSuGY5TXOqGM_iMsQ2pv6oo98sm7SHfVMVvUCNeBpl9diqktzBAWZjhXW0pdEpVQPKA6S7oMrdfQ62oHj7Smm61crAmUo-v8hMTZI4IesBtAXMwPC-RV-gMtAX0JuwPHG85Bxpi01Y4ZzUQsVyaYn2b89g08R31sQLJYhV0N50CqtQwM7-mXdNO_sEfoGxt7f_7jUarM3No-wvEf6tz7yCIflQe0a59mA=='


def derivePassword():
    kw = ['~#+', 'v~s', 'r~st', '%xvt#', 'st%tr%x\'t']
    retrievePasswordKey = list(map(int, list(input('Enter the key: '))))  # 7-digit integer
    # retrievePasswordKey = list(str(10*0) + len(kw[2]) + str(2**0) + len(kw[0]) + '2' + len("orz) + '0')

    if len(retrievePasswordKey) == 7:
        ct = kw[retrievePasswordKey[0]] + kw[retrievePasswordKey[1]] + kw[retrievePasswordKey[2]] + \
            kw[retrievePasswordKey[3]] + kw[retrievePasswordKey[4]] + \
            kw[retrievePasswordKey[5]] + kw[retrievePasswordKey[6]]
        # return ROT(ct, s)


key_str = derivePassword()
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
d = f.decrypt(payload)

with open('./decrypt.py', 'w') as f:
    f.write(d.decode())


def ROT(ct, s):
    pt = ''
    for c in ct:
        index = alphabet.find(c)
        original_index = (index + s) % len(alphabet)
        pt = pt + alphabet[original_index]
    return pt
# s = 1 (mod 2), s = 7 (mod 11), 7 < |s| < 29
# ROT|s| used to create password ciphertext
