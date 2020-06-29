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



class PyCryptodomeEncryption():

    def __init__(self):
        # 密钥key 长度必须为16（AES-128）、24（AES-192）或 32（AES-256）的Bytes长度
        self.aeskey = b'1234567890ABCDEF'
        # # 生成长度等于AES块大小的不可重复的密钥向量
        self.iv=Random.new().read(AES.block_size)
        self.aes=AES.new(self.aeskey,AES.MODE_CFB,self.iv)
        #  密钥：必须为8个字节
        deskey=b'12345678'
        # 使用 key 初始化 DES 对象，使用 DES.MODE_ECB 模式
        self.des=DES.new(deskey,DES.MODE_ECB)
        # 生成密钥对
        self.pubkey, self.prikey=rsa.newkeys(1024)


    '''Base64编码'''
    def b64encode(self,string):
        return base64.b64encode(string)

    '''Base64解码'''
    def b64decode(self,string):
        return base64.b64decode(string)


    '''MD5加密'''

    def MD5encryption(self,string):
        # 实例一个对象，使用new方法进行MD5加密算法
        m = hashlib.new("md5")
        # 生成一个使用该算法的Hash对象，data为bytes类型，内容为a123456
        m.update(string)
        # 　返回Hash算法计算得到的值(str类型)
        return m.hexdigest()


    '''对称加密DES'''

    def DESencrypt(self,string):

        # DES加密数据的长度须为8的的倍数，不够可以用其它字符填充
        text=string
        if len(text) % 8 !=0:
            text=text+"-"*(8 - len(text) % 8)
        # 密钥：必须为8个字节
        # 加密
        result=self.des.encrypt(text.encode())
        return result

    '''对称解密DES'''

    def DESdecrypt(self,string):
        decrypt_string = self.des.decrypt(string)
        return decrypt_string


    '''对称加密AES'''

    def AESencrypt(self,string):

        # DES加密数据的长度须为8的的倍数，不够可以用其它字符填充
        text=string
        # 加密
        result=self.aes.encrypt(text.encode())
        return result


    '''对称解密AES'''

    def AESdecrypt(self):
        # 解密
        decrypt_aes=AES.new(self.aeskey,AES.MODE_CFB,self.iv)
        return decrypt_aes

    '''非对称加密RSA'''

    def RSAencrypt(self,string):


        text=string

        # 加密：使用公钥
        encrypt_result=rsa.encrypt(text.encode(), self.pubkey)
        return encrypt_result,

    def RSAdecrypt(self, string):
        #解密，使用私钥
        decrypt_result=rsa.decrypt(string, self.prikey)
        return decrypt_result




if __name__=="__main__":
  encode_test=PyCryptodomeEncryption().b64encode(b"asd231231")
  decode_test=PyCryptodomeEncryption().b64decode(encode_test)
  print('编码：',encode_test)
  print('解码：',decode_test)
  encode_test_MD5=PyCryptodomeEncryption().MD5encryption(b"asd231231")
  print('MD5加密： ',encode_test_MD5)
  des_encrypt=PyCryptodomeEncryption().DESencrypt('Welcome_To_DES')
  print('DES加密：',binascii.b2a_hex((des_encrypt)))
  des_decrypt=PyCryptodomeEncryption().DESdecrypt(des_encrypt)
  print('DES解密：',des_decrypt)
  aes_encrypt=PyCryptodomeEncryption().AESencrypt('Welcome_To_DES')
  print('AES加密：',binascii.b2a_hex((aes_encrypt)))
  aes_decrypt=PyCryptodomeEncryption().AESdecrypt()
  print('AES解密：',aes_decrypt)
  rsa_encrypt=PyCryptodomeEncryption().RSAencrypt('Welcome_To_DES')
  print('RSA加密：',binascii.b2a_hex((rsa_encrypt)))
  rsa_decrypt=PyCryptodomeEncryption().RSAdecrypt(rsa_encrypt)
  print('RSA解密：',rsa_decrypt)



