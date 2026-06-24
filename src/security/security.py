from pwdlib import PasswordHash



pwd_hash = PasswordHash.recommended() 


def hash_pwd(password):
    """hashea la pasword"""
    return pwd_hash.hash(password)



def verify_pwd(plain_pwd,  hashed_pwd):
    """valida la password"""
    return pwd_hash.verify(plain_pwd, hashed_pwd)





# print(hash_pwd("pasword"))