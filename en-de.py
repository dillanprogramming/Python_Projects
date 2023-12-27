import os

class cryptor:
    def __init__(self, text, mode=1):
        self.mode = mode
        self.text = text
    def encrypt_file(self, key, path):
        if os.path.exists(path):
            key_len = len(key)
            key_count = 0

            towrite = path+".encrypted"

            read_file = open(path, "r")
            write_file = open(towrite, "w")
            
            string = read_file.read()
            string_len = len(string)

            for i in range(string_len):
                encrypt = ord(key[key_count]) ^ ord(string[i])
                write_file.write(chr(encrypt))
                key_count += 1
                if key_count == key_len:
                    key_count = 0

            read_file.close()
            write_file.close()

            if os.path.exists(towrite):
                return True
        else:
            return False
    def decrypt_file(self, key, path):
        if os.path.exists(path):
            key_len = len(key)
            key_count = 0
            
            towrite = path+".decrypted"
            
            read_file = open(path, "r")
            write_file = open(towrite, "w")
            
            string = read_file.read()
            string_len = len(string)
            
            for i in range(string_len):
                decrypt = ord(key[key_count]) ^ ord(string[i])
                write_file.write(chr(decrypt))
                key_count += 1
                if key_count == key_len:
                    key_count = 0
            
            read_file.close()
            write_file.close()
            
            if os.path.exists(write_file):
                return True
        else:
            return False