import base64
import hashlib
import binascii
import rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

''''Base64编码'''

# 编码
a=base64.b64encode(b"232131")
print(a)

# 解码
b=base64.b64decode(b'MjMyMTMx')

print(b)



'''MD5'''

# 实例一个对象，使用new方法进行MD5加密算法
m=hashlib.new("md5")
# 生成一个使用该算法的Hash对象，data为bytes类型，内容为a123456
m.update(b"a123456")
# 　返回Hash算法计算得到的值(str类型)
print(m.hexdigest())
# 返回Hash算法计算得到的值(bytes类型)
print(m.digest())




'''对称加密'''


# DES


# DES加密数据的长度须为8的的倍数，不够可以用其它字符填充
# text='Welcome_To_DES'
# if len(text) % 8 !=0:
#     text=text+"-"*(8 - len(text) % 8)
# # 密钥：必须为8个字节
# key=b'12345678'
# # 使用 key 初始化 DES 对象，使用 DES.MODE_ECB 模式
# des=DES.new(key,DES.MODE_ECB)
# # 加密
# result=des.encrypt(text.encode())
# res= binascii.b2a_hex(result)
#
# #解密
#
# decrypt_string=des.decrypt(result)
#
# print("加密后的数据{}".format(res))
# print("解密后的数据{}".format(decrypt_string))


#AES

#
# textaes="Welcome_To_AES"
# # 密钥key 长度必须为16（AES-128）、24（AES-192）或 32（AES-256）的Bytes长度
# key= b'1234567890ABCDEF'
# # 生成长度等于AES块大小的不可重复的密钥向量
# iv=Random.new().read(AES.block_size)
# # 使用key和iv初始化AES对象，使用AES.MODE_CFB模式
# aes=AES.new(key,AES.MODE_CFB,iv)
# # 加密
# result=aes.encrypt(textaes.encode())
# # 解密
# decrypt_aes=AES.new(key,AES.MODE_CFB,iv)
#
# print("密钥：",key)
# print("iv：",iv)
# print("十六进制的iv：",binascii.b2a_hex(iv))
# print("加密后的数据：",result)
# print("转为十六进制：",binascii.b2a_hex(result))
# print("解密后的数据：",decrypt_aes.decrypt(result))
#



'''非对称加密'''

# # RSA
#
# # 公钥加密、私钥解密
#
# text='Welcome to RSA'
# # 生成密钥对
# pubkey,prikey=rsa.newkeys(1024)
# # 加密：使用公钥
# encrypt_result=rsa.encrypt(text.encode(),pubkey)
# print('加密后的数据：',binascii.b2a_hex(encrypt_result))
#
# #解密，使用私钥
# decrypt_result=rsa.decrypt(encrypt_result,prikey)
# print('解密后的数据：',decrypt_result)


#创建公钥
#
# text='Welcome to RSA'
#
# # 公钥有两个值  n,e
# public_n = "e0b509f62a8fc9" * 4
# public_e = '010001'
#
#
# # n、e必须为整数
# # 将16进制的字符串转为整数
# rsa_n = int(public_n, 16)
# rsa_e = int(public_e, 16)
# print('n：{}\ne：{}'.format(rsa_n, rsa_e))
#
# # 创建公钥 rsa.PublicKey(n,e)
# pubkey=rsa.PublicKey(rsa_n,rsa_e)
# print('公钥类型：', type(pubkey))
# print('公钥：', pubkey)
# print('n:{}\n e:{}'.format(pubkey.n,pubkey.e))
# #加密
# encrypt_result=rsa.encrypt(text.encode(),pubkey)
# print('加密后的数据：', binascii.b2a_hex(encrypt_result))



# # 加签、验签
#
# pubkey, prikey = rsa.newkeys(1024)
#
# # 加签    rsa.sign(原信息，私钥，加密方式)  生成加签过后的信息
#
# signMessage=rsa.sign('何梅'.encode(),prikey,'MD5')
# print('验签信息',signMessage)
#
# # 验签    rsa.verify(需要验证的信息，加签过后的信息，公钥)
# # 如果需要验证的信息，是原信息，返回加密方式
#
# veri_1=rsa.verify('何梅'.encode(),signMessage,pubkey)
# print('何梅: ',veri_1)



