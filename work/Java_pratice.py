import jpype

class JaveEncrypt():
    def __init__(self):
        jvm_path = jpype.getDefaultJVMPath()
        jpype.startJVM(jvm_path, '-ea',
                       '-Djava.class.path=%s'%'D:/PythonDemo/Request/work/RSAEncrypt.jar',
                       '-Djava.ext.dirs=%s'%'D:/PythonDemo/Request/work;D:/softwareinstall/jdk1.8/jre/lib/ext/',
                       convertStrings=False
                       )
        # 创建类
        self.RSAEncrypt_calss = jpype.JClass('com.newdream.RSAEncrypt')
        # 通过类创建对象
        self.RSAEncrypt_object =  self.RSAEncrypt_calss()
        self.ps_key = self.RSAEncrypt_object.genKeyPair()

        '''加密处理'''
    def encode(self,string):
        encode_string = self.RSAEncrypt_object.encrypt(string,self.ps_key.get("pk"))
        return  str(encode_string)

        '''解密处理'''
    def decode(self,string):
        decode_string = self.RSAEncrypt_object.decrypt(string,self.ps_key.get("sk"))
        return str(decode_string)



if __name__=="__main__":
    string='a123456'
    test=JaveEncrypt()
    encode_string=test.encode(string)
    decode_string=test.decode(encode_string)
    print("加密字符串："+string)

    print("加密："+str(encode_string))
    print("解密："+str(decode_string))
